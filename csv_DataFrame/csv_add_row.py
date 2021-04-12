from csv import writer
from csv import DictWriter


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


def append_dict_as_row(file_name, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)


""" Append List """
row_contents = [32,'Shaun','Java','Tokyo','Morning']
append_list_as_row('Desktop/Wesley/Python_learnings/csv_DataFrame/students.csv', row_contents)



""" Append Dictionary """
dictionary = {
    "tx_count": 0,
    "client_id": 12345,
    "rssi": -31,
    "return": 0
}
path = 'Desktop/Wesley/Python_learnings/csv_DataFrame/dict.csv'
append_dict_as_row(path, dictionary, dictionary.keys())

