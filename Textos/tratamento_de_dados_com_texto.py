line = 'status.Postion[0]=108.390000'
#       0123456789012345678901234567

num_of_dots = line.count('') # Conta quantos pontos tem na string
print(num_of_dots)

dots_position = line.find('=') # Onde ele vai encontrar o '.'
print(dots_position)
# Se o retorno for -1 quer dizer que não foi encontrado

""" linha_separada = line.split('=')
print(linha_separada)
print(linha_separada[1]) """

responde = '''status.Action=Preset
status.ActionID=1   
status.Focus.FocusPosition=1391.830078
status.Focus.Status=Idle
status.FocusMapValue=8968
status.Iris.IrisValue=0.000000
status.Iris.Status=Idle
status.MoveStatus=Idle
status.PanTiltStatus=Idle
status.Postion[0]=108.390000
status.Postion[1]=2.750000
status.TaskName=AutoMovement
status.TrackStatus=Idle
status.ZoomValue=1350'''

status.Action=Preset
status.ActionID=1
status.Focus.FocusPosition=1391.830078
status.Focus.Status=Idle
status.FocusMapValue=8968
status.Iris.IrisValue=0.000000
status.Iris.Status=Idle
status.MoveStatus=Idle
status.PanTiltStatus=Idle
status.Postion[0]=108.390000
status.Postion[1]=2.750000
status.Postion[2]=94.208000
status.PresetID=1
status.TaskName=AutoMovement
status.TrackStatus=Idle
status.ZoomMapValue=15588
status.ZoomStatus=Idle
status.ZoomValue=1350

""" linhas = responde.splitlines()
horizontal_line = linhas[9]
linha_serp = horizontal_line.split('=')
horizontal_angle = float(linha_serp[1])
print("horizontal_angle = ", horizontal_angle) """

horizontal_angle = float(responde.splitlines()[9].split('=')[1])
print("horizontal_angle = ", horizontal_angle)

vertical_angle = float(responde.splitlines()[10].split('=')[1])
print("vertical_angle = ", vertical_angle)

zoom_value = float(responde.splitlines()[13].split('=')[1])
print("ZoomValue = ", zoom_value)

focus_position = float(responde.splitlines()[2].split('=')[1])
print("FocusPosition = ", focus_position)

focu_status = str(responde.splitlines()[3].split('=')[1])
print("Focu_status = ", focus_position)

iris_status = str(responde.splitlines()[6].split('=')[1])
print("Iris_status = ", focus_position)

move_status = str(responde.splitlines()[7].split('=')[1])
print("Move_status = ", focus_position)

pantilt_status = str(responde.splitlines()[8].split('=')[1])
print("pantilt_status = ", focus_position)
