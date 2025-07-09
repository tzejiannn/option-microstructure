import os
import pandas as pd

#Change path for option type
data_folder = os.path.join('option_data', 'puts', 'clean')
output_folder = os.path.join('option_data', 'puts', 'combined')
os.makedirs(output_folder, exist_ok=True)

csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]


df_list = []
for file in csv_files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)
    df_list.append(df)



combined_df = pd.concat(df_list, ignore_index=True)

# Step 5: Save the result
combined_file = os.path.join(output_folder, 'combined_puts.csv')
combined_df.to_csv(combined_file, index=False)

print(f"data successfully combined")