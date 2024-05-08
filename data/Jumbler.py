import pandas as pd

# Load the JSON data into a DataFrame
df = pd.read_json(r'C:\Users\joyvi\OneDrive\Desktop\Final Project\ecfr-title-12.jsonl')

# Shuffle the DataFrame rows
shuffled_df = df.sample(frac=1).reset_index(drop=True)

# Save the shuffled DataFrame to a new JSON file
shuffled_df.to_json(r'C:\Users\joyvi\OneDrive\Desktop\Final Project\ecfr-title-12_jumbled.jsonl', orient='records')

print("The rows have been shuffled and saved to the new JSON file.")
