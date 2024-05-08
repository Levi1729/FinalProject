import json
import unicodedata
from sklearn.model_selection import train_test_split

# Function to normalize and clean text
def normalize_text(text):
    # Convert escape sequences and normalize text
    text = text.encode("utf-8", errors="replace").decode("unicode_escape", errors="replace")
    text = unicodedata.normalize("NFKC", text)  # Normalize to NFC (canonical composition)
    return text

# Function to preprocess the dataset and handle missing keys
def read_and_fix_jsonl(input_jsonl):
    records = []

    # Read and preprocess the input JSONL (with utf-8-sig to handle BOM)
    with open(input_jsonl, "r", encoding="utf-8-sig", errors="replace") as infile:
        for line_num, line in enumerate(infile, start=1):
            try:
                record = json.loads(line.strip())
                # If `text` is missing but `clean_text` exists, use `clean_text`
                if "text" not in record and "clean_text" in record:
                    record["text"] = record["clean_text"]

                # Ensure `text` is available before adding
                if "text" in record:
                    record["text"] = normalize_text(record["text"])
                    records.append(record)
                else:
                    print(f"Skipping line {line_num} due to missing 'text' field")

            except json.JSONDecodeError:
                print(f"Skipping invalid line {line_num}: {line.strip()}")

    return records

# Function to split the dataset into train and test files
def preprocess_and_split_jsonl(input_jsonl, train_output_jsonl, test_output_jsonl, test_size=0.2):
    records = read_and_fix_jsonl(input_jsonl)

    # Check the count of valid records
    print(f"Total valid records found: {len(records)}")

    if not records:
        raise ValueError("No valid data found to process.")

    # Split the dataset into training and test sets
    train_data, test_data = train_test_split(records, test_size=test_size, random_state=42)

    # Write the train data to a JSONL file
    with open(train_output_jsonl, "w", encoding="utf-8") as train_file:
        for record in train_data:
            train_file.write(json.dumps(record) + "\n")

    # Write the test data to a JSONL file
    with open(test_output_jsonl, "w", encoding="utf-8") as test_file:
        for record in test_data:
            test_file.write(json.dumps(record) + "\n")

    print(f"Processed data saved to {train_output_jsonl} (train) and {test_output_jsonl} (test)")

# Example usage
input_jsonl_path = "annotations.jsonl"
train_jsonl_path = "train_data.jsonl"
test_jsonl_path = "test_data.jsonl"

preprocess_and_split_jsonl(input_jsonl_path, train_jsonl_path, test_jsonl_path, test_size=0.2)
