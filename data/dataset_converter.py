import spacy
import json
from spacy.tokens import DocBin
from pathlib import Path

# Load a blank spaCy model
nlp = spacy.blank("en")  # Adjust language model accordingly

# Define paths for input JSONL and output .spacy files
input_jsonl_path = Path("./test_annot.jsonl")
output_spacy_path = Path("./test_annot.spacy")

# Initialize a DocBin object to store the converted Doc objects
doc_bin = DocBin()

# Function to convert JSON data into spaCy Docs
def create_doc(text, labels):
    doc = nlp.make_doc(text)
    doc.cats = labels
    return doc

# Read the JSONL file and process each example
with input_jsonl_path.open("r", encoding="utf-8") as file:
    for line in file:
        data = json.loads(line)
        text = data["text"]
        accepted_labels = data["accept"]
        
        # Initialize a dictionary of all possible labels with False
        label_dict = {option["id"]: False for option in data["options"]}
        
        # Set True for accepted labels
        for label in accepted_labels:
            label_dict[label] = True

        # Create a Doc object with multi-label categories
        doc = create_doc(text, label_dict)
        doc_bin.add(doc)

# Save the DocBin object to a .spacy file
with output_spacy_path.open("wb") as out_file:
    out_file.write(doc_bin.to_bytes())

print(f"Dataset successfully converted to {output_spacy_path}")
