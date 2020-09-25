class CameraActionManager():
    def __init__(self):
        self.__status = None

    def go_to_monitor_position(self, camera_control):
        self.__camera_control = camera_control
        self.__camera_control.send_goto_preset()

    def check_status_monitor_position(self, camera_control):
        self.__camera_control = camera_control
        self.__camera_control.check_position()


class CameraController():
    def __init__(self, port, ip, model):
        self.__port = port
        self.__ip = ip
        self.__pan = None
        self.__tilt = None
        self.__model = model
        print("Construtor da classe mae CameraController")
        self.select_camera()

    def select_camera(self):
        if (self.__model == 1):
            print('A camera eh uma hikvision')
        
    def send_goto_preset(self):
        pass

    def check_position(self):
        pass

class PtzHikvisionController(CameraController):
    def __init__(self, port, ip, model):
        super().__init__(port, ip, model)
        print("E agora temos um objeto de controle dessa camera")

    def send_goto_preset(self):
        print('Send_goto_preset\n')



if __name__ == "__main__":
    port = '9501'
    ip = '192.168.10.15'
    model = 1

    manager = CameraActionManager()
    hikvision_obj = PtzHikvisionController(port, ip, model)
    manager.go_to_monitor_position(hikvision_obj)
