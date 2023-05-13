import json
import csv

def json_to_csv(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)

        # 全てのデータ行を書き込む
        for item in data:
            row = []
            flatten(item, row)
            writer.writerow(row)

def flatten(data, row, parent_key=''):
    if isinstance(data, dict):
        for key in data:
            new_key = parent_key + '.' + key if parent_key else key
            flatten(data[key], row, new_key)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_key = parent_key + '.' + str(i) if parent_key else str(i)
            flatten(item, row, new_key)
    else:
        row.append(data)

# 使用例
json_to_csv('input.json', 'output.csv')
