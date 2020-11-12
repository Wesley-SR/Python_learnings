# Pass tuple as a arguments
import threading

class my_class():
    def __init__(self):
        self._local_dragino_ID = 33333
        self._path_remote = '/var/iot/push/teste.json'

    def master(self, thisdict):
        my_msg = self.gera_msg(thisdict)
        print('\nMessage received: ', my_msg)
        dictionary_retuned  = self.read_msg(my_msg)
        print('\n')
        for x, y in dictionary_retuned.items():
            print(x, ': ', y)
        print('\nMessage to return: ', dictionary_retuned.get("message_toreturn"))

    def run_master(self, thisdict):
        t = threading.Thread(target = self.master,
            args=(thisdict, ))
        t.daemon = False
        t.start()


    def gera_msg(self, thisdict):
        payload = ''
        size = len(thisdict)
        counter = 1
        for x, y in thisdict.items():
            payload = payload + str(x) + '=' + str(y)
            if counter >= size: break
            payload = payload + '&'
            counter += 1
        
        # message = 'echo "{{\\"txpk\\":{{\\"imme\\":true,\\"tmst\\"'\
        #     ':50000000000,\\"freq\\":915.6,\\"powe\\":20,\\"datr\\":\\"'\
        #     'SF7BW125\\",\\"codr\\":\\"4/5\\",\\"ipol\\":false,\\"data\\"'\
        #     ':\\"<{ID}>{pld}\\"}}}}" >> {path}'\
        #     .format(ID=self._local_dragino_ID, pld=payload, path=self._path_remote)
        
        message = '{ID}:{pld}'.format(ID=self._local_dragino_ID, pld=payload) # Isso é como recebe
        
        return message


    def read_msg(self, msg_received):
        msg_received = bytes(msg_received, 'utf-8') # O Dragino recebe bytes
        msg_received = msg_received.decode('utf-8')
        msg_received = msg_received.translate({ord(i): None for i in '{\"}'})
        msg_received = msg_received.split(':')

        client_id = msg_received[0]
        payload = msg_received[1]
        message_toreturn = payload
        print('\nPayload received: ', payload)
        payload = payload.split('&')
        fields_number = len(payload)

        dictionary = {}
        for x in payload:
            field = x
            field = field.split('=')
            dictionary[str(field[0])] = str(field[1])
        
        dictionary["message_toreturn"] = message_toreturn
        
        return dictionary 


if __name__ == "__main__":

    thisdict =	{
    "Message_ID": 'Heart_Beat',
    "Temperature": 59.6,
    "Voltage": 12.4,
    "RSSI_wifi": -30
    }

    my_object = my_class()
    my_object.run_master(thisdict)
