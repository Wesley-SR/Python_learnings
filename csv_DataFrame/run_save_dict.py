from SaveData import SaveDictInCSV

save_dict = SaveDictInCSV()

""" Append Dictionary """
dictionary = {
    "tx_count": 0,
    "client_id": 12345,
    "rssi": -31,
    "return": 0
}
path = "Desktop/Wesley/Python_learnings/csv_DataFrame/dict.csv"

save_dict.append_dict_as_row(file_path = path, dictionary = dictionary, keys_of_dict = dictionary.keys())

