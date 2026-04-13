import pandas as pd
import os

# ==========================================
# 1. ADD YOUR INPUT FILE PATH HERE
# ==========================================
# Use the 'r' before the quotes to handle Windows backslashes correctly
input_file_path = r'C:\Users\pradn\OneDrive\Desktop\data\cleaned_state.csv'
output_folder = r'C:\Users\pradn\OneDrive\Desktop\data'

# Check if the file exists before starting
if not os.path.exists(input_file_path):
    print(f"❌ Error: Could not find the file at {input_file_path}")
else:
    # Load the dataset
    df = pd.read_csv(input_file_path)


    def standardize_district(name):
        if not isinstance(name, str):
            return name

        # Pre-clean: lowercase, remove symbols like *, and strip spaces
        clean_name = name.lower().strip().replace('*', '').replace('dist :', '').strip()

        # Mapping to Standard/New Official Names
        mapping = {
            'ahmednagar': 'Ahilyanagar',
            'ahmed nagar': 'Ahilyanagar',
            'ahmadnagar': 'Ahilyanagar',
            'ahilyanagar': 'Ahilyanagar',

            'aurangabad': 'Chhatrapati Sambhajinagar',
            'chatrapati sambhaji nagar': 'Chhatrapati Sambhajinagar',
            'chhatrapati sambhajinagar': 'Chhatrapati Sambhajinagar',

            'osmanabad': 'Dharashiv',
            'dharashiv': 'Dharashiv',

            'bid': 'Beed',
            'beed': 'Beed',

            'buldana': 'Buldhana',
            'buldhana': 'Buldhana',

            'gondiya': 'Gondia',
            'gondia': 'Gondia',

            'raigarh': 'Raigad',
            'raigad': 'Raigad',
            'raigarh(mh)': 'Raigad',
            'raigarh(mg)': 'Raigad',

            'thane': 'Thane',
            'washim': 'Washim',
            'nandurbar': 'Nandurbar',

            'mumbai( sub urban )': 'Mumbai Suburban',
            'mumbai city': 'Mumbai City',
            'mumbai': 'Mumbai City'
        }

        return mapping.get(clean_name, clean_name.title())


    # 2. Apply the cleanup
    df['district_standardized'] = df['district'].apply(standardize_district)

    # 3. Aggregate the data
    comparison_df = df.groupby(['state', 'district_standardized']).agg({
        'demo_age_5_17': 'sum',
        'demo_age_17_': 'sum',
        'total_updates': 'sum'
    }).reset_index()

    # 4. Sort by total_updates in Ascending Order
    comparison_df = comparison_df.sort_values(by='total_updates', ascending=True)

    # 5. Save the resulting CSV document
    comparison_df.columns = ['state', 'district', 'demo_age_5_17', 'demo_age_17_', 'total_updates']

    output_path = os.path.join(output_folder, 'clean_state.csv')
    comparison_df.to_csv(output_path, index=False)

    print(f"✅ Process Complete. File saved as: {output_path}")