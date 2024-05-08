import json

# Paths to the input and output filesC:\Users\joyvi\OneDrive\Desktop\Final Project
input_file = 'annotations.jsonl'
training_output_file = 'training_data.jsonl'
target_output_file = 'target_data.jsonl'

# The field name that holds the target labels in the input dataset
target_field = 'label'

# Initialize empty lists for the training and target data
training_data = []
target_data = []

# Read input `.jsonl` file and process each line
with open(input_file, 'r', encoding='utf-8') as infile:
    for line in infile:
        record = json.loads(line)
        # Copy the record and remove the target field to create the training data
        training_record = record.copy()
        target_labels = training_record.pop(target_field, None)
        
        # Add to the training data and target data respectively
        training_data.append(training_record)
        target_data.append({target_field: target_labels})

# Write the training data to the specified output file
with open(training_output_file, 'w', encoding='utf-8') as outfile_train:
    for record in training_data:
        outfile_train.write(json.dumps(record) + '\n')

# Write the target data to the specified output file
with open(target_output_file, 'w', encoding='utf-8') as outfile_target:
    for record in target_data:
        outfile_target.write(json.dumps(record) + '\n')

print("Data has been successfully split into training and target datasets.")
