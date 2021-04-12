import json

dictionary = {
    "message_id": 'Test',
    "tx_count": 0,
    "Hello Robot": 'My name is Lactec'
}

my_json = json.dumps(dictionary)

print(dictionary)
print('\n')
print(my_json)

path = 'Desktop/Wesley/Python_learnings/json/test_file.json'
with open(path, 'w') as json_file:
    json.dump(dictionary, json_file, indent=4)