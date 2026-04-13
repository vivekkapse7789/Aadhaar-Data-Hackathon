import pandas as pd
from mappings import STATE_MAP, DISTRICT_MAP

files = [
    'api_data_aadhar_demographic_0_500000.csv',
    'api_data_aadhar_demographic_500000_1000000.csv',
    'api_data_aadhar_demographic_1000000_1500000.csv',
    'api_data_aadhar_demographic_1500000_2000000.csv',
    'api_data_aadhar_demographic_2000000_2071700.csv'
]

def clean_val(v, mapping):
    if pd.isna(v): return v
    # 1. Remove asterisk and trim
    s = str(v).replace('*', '').strip()
    # 2. Apply Mapping
    if s in mapping: return mapping[s]
    # 3. Handle Title Case for items not in mapping
    return s.title()

# Load all data with sequence
print("Loading all data...")
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
df['seq'] = range(len(df))

# Standardize
print("Applying standardization...")
df['state'] = df['state'].apply(lambda x: clean_val(x, STATE_MAP))
df['district'] = df['district'].apply(lambda x: clean_val(x, DISTRICT_MAP))

# Find 'True' Pincode Mapping (New Data Logic)
print("Analyzing pincode-location consistency...")
freq = df.groupby(['pincode', 'state', 'district']).size().reset_index(name='c')
master = freq.sort_values('c', ascending=False).drop_duplicates('pincode')
df = df.merge(master[['pincode', 'state', 'district']], on='pincode', suffixes=('', '_true'), how='left')

# Separate 'Clean' and 'New Data' (Mismatches)
df['is_new'] = (df['state'] != df['state_true']) | (df['district'] != df['district_true'])

clean_data = df[~df['is_new']].copy()
new_data = df[df['is_new']].copy()

# Save split files
clean_data.to_csv('cleaned_data.csv', index=False)
new_data.to_csv('new_data_mismatches.csv', index=False)

# Merge back in sequence
final = pd.concat([clean_data, new_data]).sort_values('seq')
final.drop(columns=['seq', 'state_true', 'district_true', 'is_new'], inplace=True)
final.to_csv('standardized_final_merged.csv', index=False)

print(f"Done! Processed {len(df)} rows.")
print(f"Clean: {len(clean_data)} | New Data (Mismatches): {len(new_data)}")
