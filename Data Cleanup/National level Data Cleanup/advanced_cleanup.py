import pandas as pd
import re

# File path
file_path = r"D:\~Projects\Hackathon\UDAI Data Hackathon\Datasets\Complete Download Big Data\2. Aadhaar Demographic Update dataset\api_data_aadhar_demographic\standardized_final_merged.csv"

print(f"Loading file: {file_path}")

try:
    combined_df = pd.read_csv(file_path)
    print(f"Initial row count: {len(combined_df)}")
except FileNotFoundError:
    print("Error: The file was not found.")
    exit()

# 5️⃣ PRE-STEP: Fix column names (Do this first so numeric conversion works)
if 'demo_age_17_' in combined_df.columns:
    combined_df.rename(columns={'demo_age_17_': 'demo_age_17_plus'}, inplace=True)

# 6️⃣ PRE-STEP: Numeric conversion
# We need numbers before we can calculate the total
for col in ['demo_age_5_17', 'demo_age_17_plus']:
    if col in combined_df.columns:
        combined_df[col] = pd.to_numeric(combined_df[col], errors='coerce')

# 7️⃣ PRE-STEP: Create total_updates column (Calculated from brackets)
# This ensures the column EXISTS before we try to drop NAs from it
combined_df['total_updates'] = combined_df['demo_age_5_17'] + combined_df['demo_age_17_plus']

# 1️⃣ Remove duplicates
combined_df.drop_duplicates(inplace=True)

# 2️⃣ Handle missing/null values 
# Now 'total_updates' exists, so this won't crash
combined_df.dropna(subset=['state', 'district', 'total_updates'], inplace=True)

# 3️⃣ Text normalization
def normalize_text(text):
    if pd.isna(text): return text
    text = str(text).lower().strip()
    text = re.sub(r'[^\w\s]', '', text)
    return text

combined_df['state'] = combined_df['state'].apply(normalize_text)
combined_df['district'] = combined_df['district'].apply(normalize_text)

# 4️⃣ State and district standardization
def standardize_state(state):
    mapping = {"orissa": "odisha"} 
    return mapping.get(state, state)

def standardize_district(district):
    mapping = {
        "ahmed nagar": "ahmadnagar",
        "aurangabad": "chhatrapati sambhajinagar"
    }
    return mapping.get(district, district)

combined_df['state'] = combined_df['state'].apply(standardize_state)
combined_df['district'] = combined_df['district'].apply(standardize_district)

# 8️⃣ Date cleaning
combined_df['date'] = pd.to_datetime(combined_df['date'], format='%d-%m-%Y', errors='coerce')

# 9️⃣ Final Row removal 
final_df = combined_df.dropna(subset=['state', 'district', 'demo_age_5_17', 'demo_age_17_plus', 'total_updates', 'date'])

print("-" * 30)
print(f"Cleanup finished.")
print(f"Rows remaining: {len(final_df)}")
print(f"Total rows removed: {len(combined_df) - len(final_df)}")
print("-" * 30)

# Save the cleaned file
output_path = file_path.replace(".csv", "_cleaned.csv")
final_df.to_csv(output_path, index=False)
print(f"Saved cleaned data to: {output_path}")