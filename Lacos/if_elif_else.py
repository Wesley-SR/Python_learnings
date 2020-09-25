class StandardCommands():
    def __init__(self):
        self._data_write = [255, 1, 0, 0, 0, 0, 0]
        self._pan_right_byte = 2
        self._pan_left_byte = 4
        self._tilt_up_byte = 8
        self._tilt_down_byte = 16
        self._pan_right_and_tilt_up_byte = 10
        self._pan_right_and_tilt_down_byte = 12
        self._pan_left_and_tilt_up_byte = 18
        self._pan_left_and_tilt_down_byte = 20

    def teleoperation(self, operation_specification,
                      required_value):
        self._movement_orientation = operation_specification
        self._valid_command = False
        #print('valid_command initializes --> ', self._valid_command)
        
        try:
            self._speed = int(required_value) # Speed ranges from zero to sixty
            #print('self._speed = ', self._speed)

            if (self._speed >= 0 and self._speed <=60):
                #print('Speed is ok!')

                if self._movement_orientation == 'right':
                    self._data_write[3] = self._pan_right_byte
                    self._data_write[4] = self._speed
                    self._data_write[5] = 0
                    self._valid_command = True

                elif self._movement_orientation == 'left':
                    self._data_write[3] = self._pan_left_byte
                    self._data_write[4] = self._speed
                    self._data_write[5] = 0
                    self._valid_command = True

                elif self._movement_orientation == 'up':
                    self._data_write[3] = self._tilt_up_byte
                    self._data_write[4] = 0
                    self._data_write[5] = self._speed
                    self._valid_command = True

                elif self._movement_orientation == 'down':
                    self._data_write[3] = self._tilt_down_byte
                    self._data_write[4] = 0
                    self._data_write[5] = self._speed
                    self._valid_command = True

                elif self._movement_orientation == 'right_and_up':
                    self._data_write[3] = self._pan_right_and_tilt_up_byte
                    self._data_write[4] = self._speed
                    self._data_write[5] = self._speed
                    self._valid_command = True

                elif self._movement_orientation == 'right_and_down':
                    self._data_write[3] = self._pan_right_and_tilt_down_byte
                    self._data_write[4] = self._speed
                    self._data_write[5] = self._speed
                    self._valid_command = True

                elif self._movement_orientation == 'left_and_up':
                    self._data_write[3] = self._pan_left_and_tilt_up_byte
                    self._data_write[4] = self._speed
                    self._data_write[5] = self._speed
                    self._valid_command = True

                elif self._movement_orientation == 'left_and_down':
                    self._data_write[3] = self._pan_left_and_tilt_down_byte
                    self._data_write[4] = self._speed
                    self._data_write[5] = self._speed
                    self._valid_command = True
                else:
                    raise ValueError('The operation specification is not valid'
                                    '\n\t\t     Enter with a string')
            else:
                raise ValueError('Speed ranges from zero to sixty')

            # Send to pantilt
            if self._valid_command == True:
                # self._ser.write(self._data_write)
                print('Command is ok!')

        except ZeroDivisionError as error:
            print('ZeroDivisionError')
            print("Description error:  ", error)
        except ValueError as error:
            print('ValueError')
            print("Description error:  ", error)
        except TypeError as error:
            print('TypeError')
            print("Description error:  ", error)
        except Exception as error:
            print('Exception')
            print("Description error:  ", error)


objeto = StandardCommands()
objeto.teleoperation('up', 5)