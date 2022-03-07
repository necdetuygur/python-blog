import json


def ResJson(data, row_headers):
    json_data = []
    for result in data:
        json_data.append(dict(zip(row_headers, result)))
    return json.dumps(json_data)


def ResJsonOne(data, row_headers):
    return json.dumps(dict(zip(row_headers, data)))
