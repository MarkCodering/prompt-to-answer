# Open the file under /outputs/algebra
# Turn the files into jsonl format

import os
import json

num_files = 0

num_files = len(os.listdir('outputs/algebra'))

for i in range(num_files):
    # Convert the file to jsonl format
    with open(f'../outputs/algebra/{i}.json', 'r') as json_file:
        # Load the data from the JSON file
        data = json.load(json_file)
        
    with open(f'../outputs/algebra/fine-tune-{i}.jsonl', 'w') as jsonl_file:
        # If the data is a list of records, write each record on a new line
        if isinstance(data, list):
            for record in data:
                jsonl_file.write(json.dumps(record) + '\n')
        else:
            # If the data is a single record, just write it to the file
            jsonl_file.write(json.dumps(data) + '\n')
            
            