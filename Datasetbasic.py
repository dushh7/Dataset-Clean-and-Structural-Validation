import pandas as pd

# Load dataset
df = pd.read_csv("raw_data.csv")

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.fillna(method='ffill')

# Standardize column names
df.columns = df.columns.str.strip().str.lower()

# Convert text to proper format
df['name'] = df['name'].str.title()

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("Data cleaning completed successfully!")
