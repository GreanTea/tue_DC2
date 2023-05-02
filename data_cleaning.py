import os
import pandas as pd
import fnmatch
import shutil

# Set the directory containing the folders of CSV files
root_directory = 'data/all'
outcomes_dir = 'data/all/outcomes'
stop_dir = 'data/all/stop'
street_dir = 'data/all/street'


def clean_datasets(path):
    temp_filepath = os.path.join(path, "cleaned")
    if not os.path.exists(temp_filepath):
        os.makedirs(temp_filepath)

        for filename in os.listdir(path):
            if filename.endswith(".csv"):
                filepath = os.path.join(path, filename)

                # Load CSV file into a Pandas DataFrame
                df = pd.read_csv(filepath)
                df = df.fillna(value='')

                # Remove rows where "LSOA name" column does not contain "Barnet"
                df = df[df["LSOA name"].str.contains("Barnet")]

                # Save cleaned data to a new CSV file
                cleaned_filename = f"cleaned_{filename}"
                cleaned_filepath = os.path.join(temp_filepath, cleaned_filename)
                df.to_csv(cleaned_filepath, index=False)
    else:
        print("Cleaned directory already exists, skipping loop.")

    # Initialize an empty DataFrame to store the merged data
    df_merged = pd.DataFrame()

    # Loop through each file in the directory
    for filename in os.listdir(temp_filepath):
        if filename.endswith(".csv"):
            filepath = os.path.join(temp_filepath, filename)

            # Load CSV file into a Pandas DataFrame
            df_temp = pd.read_csv(filepath)

            # Append the DataFrame to the merged DataFrame
            df_merged = pd.concat([df_merged, df_temp])
            df_merged = df_merged.drop_duplicates()

    # Save the merged DataFrame to a new CSV file
    output_filepath = os.path.join(temp_filepath, "cleaned.csv")
    df_merged.to_csv(output_filepath, index=False)
    return


def separate(path):
    # Loop through all the directories in the root directory
    for dirpath, dirnames, filenames in os.walk(path):
        # Find all CSV files in the directory
        csv_files = fnmatch.filter(filenames, '*.csv')

        # Loop through the CSV files and remove the ones that don't contain 'metropolitan'
        for file in csv_files:
            if 'metropolitan' not in file:
                os.remove(os.path.join(dirpath, file))

    for root, dirs, files in os.walk(path):
        for file in files:
            # Check if the file is a CSV file
            if file.endswith('.csv'):
                # Check if the filename contains 'outcomes', 'stop', or 'street'
                if 'outcomes' in file:
                    # Move the file to the outcomes directory
                    shutil.move(os.path.join(root, file), os.path.join(outcomes_dir, file))
                elif 'stop' in file:
                    # Move the file to the stop directory
                    shutil.move(os.path.join(root, file), os.path.join(stop_dir, file))
                elif 'street' in file:
                    # Move the file to the street directory
                    shutil.move(os.path.join(root, file), os.path.join(street_dir, file))
    return


separate(root_directory)
clean_datasets(outcomes_dir)
clean_datasets(street_dir)
