from csv import DictWriter

class SaveDictInCSV():

    def append_dict_as_row(sefl, file_path, dictionary, keys_of_dict):
        # Open file in append mode
        with open(file_path, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            dict_writer = DictWriter(write_obj, fieldnames=keys_of_dict)
            # Add dictionary as wor in the csv
            dict_writer.writerow(dictionary)
