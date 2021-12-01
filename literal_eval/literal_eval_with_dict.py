# from ast import literal_eval
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
    print(x, y)
 
lora_outputs = {
"group_data_1": {
  "topic1": "battery_voltage",
  "topic2": "battery_temperature",
  "topic3": "motor1_temperature",
  "topic4": "motor2_temperature",
  "topic5": "jetson_temperature",
  "topic6": "emergency_button"
},
"group_data_2": {
  "topic1": "route_number",
  "topic2": "waypoint_namber",
  "topic3": "panoramic_status",
}}

dict_aux = {}

for key,value in lora_outputs.items():
    dict_aux[key] = {}
#   print(type(key))
#   print(type(value))
#   print(value["topic1"])
    for k,v in value.items():
        print(k,v)
        dict_aux[key][v] = 0


# for x, y in dict_aux.items():
#     print(x, y)

# print(dict_aux["group_data_1"])
print('\n')
for key,value in dict_aux.items():
    print(key)
    for k,v in value.items():
        print(k,v)