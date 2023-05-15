import os
import pandas as pd
import fnmatch
import shutil


# Set the directory containing the folders of CSV files
root_directory = 'data/all'
outcomes_dir = 'data/all/outcomes'
stop_dir = 'data/all/stop'
street_dir = 'data/all/street'
hp_dir = 'data/hp'

# Read CSV file
# df = pd.read_csv('data/salary/cleaned_salary.csv')

def clean_ocstr(path):
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

def clean_stop(path):
    temp_filepath = os.path.join(path, "cleaned")
    if not os.path.exists(temp_filepath):
        os.makedirs(temp_filepath)

        for filename in os.listdir(path):
            if filename.endswith(".csv"):
                filepath = os.path.join(path, filename)

                # Load CSV file into a Pandas DataFrame
                df = pd.read_csv(filepath)
                df = df.fillna(value='')

                # Remove rows where "Legislation" column does not contain "Police and Criminal Evidence Act 1984 (
                # section 1)"
                df = df[df["Object of search"].str.contains("Stolen")]
                df = df[~df["Outcome"].str.contains("further")]
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

def clean_pp(path):
    temp_filepath = os.path.join(path, "cleaned")
    if not os.path.exists(temp_filepath):
        os.makedirs(temp_filepath)

        for filename in os.listdir(path):
            if filename.endswith(".csv"):
                filepath = os.path.join(path, filename)

                # Load CSV file into a Pandas DataFrame
                df = pd.read_csv(filepath, header=None)
                df = df.fillna(value='')

                # # Remove rows where "LSOA name" column does not contain "Barnet"
                df = df[df.iloc[:, 11] == "BARNET"]
                df = df.drop(df.columns[[0, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]], axis='columns')
                # Save cleaned data to a new CSV file
                cleaned_filename = f"cleaned_{filename}"
                cleaned_filepath = os.path.join(temp_filepath, cleaned_filename)
                df.to_csv(cleaned_filepath, header=False, index=False)
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
            df_temp = df_temp.drop(df_temp.index[0])

            # Append the DataFrame to the merged DataFrame
            df_merged = pd.concat([df_merged, df_temp])
            df_merged = df_merged.drop_duplicates()

    # Save the merged DataFrame to a new CSV file
    output_filepath = os.path.join(temp_filepath, "cleaned.csv")
    df_merged.to_csv(output_filepath, header=False, index=False)
    return

def clean_hp(path):
    for filename in os.listdir(path):
        if filename.endswith(".csv"):
            filepath = os.path.join(path, filename)

            # Load CSV file into a Pandas DataFrame
            df = pd.read_csv(filepath)
            df = df.iloc[:, 3:]
            start_index = df.columns.get_loc('Year ending Dec 1995')
            end_index = df.columns.get_loc('Year ending Dec 2011')
            df = df.loc[:, ~df.columns.isin(df.columns[start_index:end_index + 1])]

                # Remove rows where "LSOA name" column does not contain "Barnet"
            df = df[df["LSOA name"].str.contains("Barnet")]
                # Save cleaned data to a new CSV file
            cleaned_filename = f"cleaned_{filename}"
            cleaned_filepath = os.path.join(path, cleaned_filename)
            df.to_csv(cleaned_filepath, header=True, index=False)
    # else:
    #     print("Cleaned directory already exists, skipping loop.")
    return

# Define function to remove pound sign and convert to float
def remove_pound_sign(df):
    for col in df.columns[1:]:
        df[col] = df[col].str.replace('£', '').str.replace(',', '').astype(float)
    return df

# Apply function to all cells in the DataFrame
# df = df.applymap(remove_pound_sign)

# clean_pp(root_directory)
# separate(root_directory)
# clean_ocstr(outcomes_dir)
# clean_stop(stop_dir)
# clean_ocstr(street_dir)
# clean_hp(hp_dir)







