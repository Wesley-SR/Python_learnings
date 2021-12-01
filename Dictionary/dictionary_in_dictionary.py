# Pass tuple as a arguments
from ast import literal_eval

class my_class():
    def __init__(self):
        self._local_dragino_ID = 33333
        self._path_remote = '/var/iot/push/teste.json'

    def convert_lora_message_to_dictionary(self,
                                           message_received: bytes) -> dict:
        """
            This function will extract and separate the contained in the message.
            Observation: The message format can be change depending of the dragino
            firmware version.

        Args:
            message_received (str): Complete message

        Returns:
            data_on_dictionary (dict): Dictionary with all fields contained in the received message
        """

        message_received = message_received.decode('utf-8')  # Decoce message
        fields = message_received.split(',', 2)
        data_on_dictionary = {}
        data_on_dictionary["time"] = fields[0]
        data_on_dictionary["RSSI"] = fields[1]
        data_on_dictionary["data"] = literal_eval(fields[2])
        return data_on_dictionary

    def read_payload(self, payload: dict):
        type_msg = {}
        to_read = {}
        to_write = {}

        payload_message = ''
        size = len(payload)
        counter = 1
        type_msg = payload.values[1]
        to_read = payload[2]
        to_write = payload[3]

        print(type_msg)
        print(to_read)
        print(to_write)

    def convert_dictionary_to_lora_send_command(self, lora_id: int, payload: dict) -> str:
        """
            This function takes a dictionary and turns it into a echo string command.
            The message will be a ssh command that will create a file in dragino.

        Args:
            lora_id (int): ID to send the message.
            data (dict): payload with the custom message.
        Returns:
            echo_command : echo command to sent to Dragino system
        """

        payload_message = ''
        size = len(payload)
        counter = 1
        for payload_id, value in payload.items():
            payload_message = payload_message + \
                str(payload_id) + '=' + str(value)
            if counter >= size:
                break
            payload_message = payload_message + '&'
            counter += 1

        echo_command = 'echo "{{\\"txpk\\":{{\\"imme\\":true,\\"tmst\\"'\
                       ':50000000000,\\"freq\\":915.0,\\"powe\\":20,\\"datr\\":\\"'\
                       'SF7BW125\\",\\"codr\\":\\"4/5\\",\\"ipol\\":false,\\"data\\"'\
                       ':\\"<{ID}>{pld}\\"}}}}" > /var/iot/push/send'\
            .format(ID=lora_id, pld=payload)

        return echo_command


if __name__ == "__main__":

    thisdict =	{
    "Message_ID": 'Heart_Beat',
    "Temperature": 59.6,
    "Voltage": 12.4,
    "RSSI_wifi": -30
    }

    thisdict = {"type_msg":{"Direction":"forward","ID":"1"},
                    "read":{"sensor":"temp_bat", "sensor":"temp_motor", "sensor":"voltage_bat"},
                    "write":{"stop":"False", "go_home":"True"}}

    my_object = my_class()
    my_object.run(thisdict)
