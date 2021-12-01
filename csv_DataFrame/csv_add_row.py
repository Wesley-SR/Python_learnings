from csv import writer
from csv import DictWriter
import datetime

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


def append_dict_as_row(folder,file_name, dict_of_elem, field_names):
    # Open file in append mode
    with open("{}/{}".format(folder,file_name), 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)

def create_file_name_dict(name) -> str: 
    current_date_and_time = datetime.datetime.now()
    current_date_and_time_string = str(current_date_and_time)
    file_name =  name + "_" + current_date_and_time_string + ".csv"
    return file_name


""" Append List """
row_contents = [55,'Shauns','Java','Tokyo','Morning']
append_list_as_row("students.csv", row_contents)



# """ Append Dictionary """
# dictionary = {
#     "tx_count": 0,
#     "client_id": 12345,
#     "rssi": -31,
#     "return": 0
# }
# path = 'dict.csv'
# append_dict_as_row(path, dictionary, dictionary.keys())

dictionary = {
    "time": 0,
    "RSSI_tx": 0,
    "RSSI_rx": 0,
    "counter": 0
}
name = "teste"
folder = "data"
file_name = create_file_name_dict(name)
print(file_name)
append_dict_as_row(folder,file_name, dictionary, dictionary.keys())

for i in range (1,10):
    dictionary["counter"] = dictionary["counter"] + 1
    append_dict_as_row(folder,file_name, dictionary, dictionary.keys())
