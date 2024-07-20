import csv
import json
def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


def json_to_csv(json_data, csv_filename):
    # Flatten the JSON data
    flat_data = [flatten_json(item) for item in json_data]

    # Extract the header from the flattened data
    header = set()
    for item in flat_data:
        header.update(item.keys())
    header = sorted(header)

    # Write the CSV file
    with open(csv_filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)  # Write the header
        for item in flat_data:
            row = [item.get(key, "") for key in header]
            csvwriter.writerow(row)