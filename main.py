import time
import mouse


def setPosition_mouse():
    global other
    if other:

        print("Position saved: " + str(mouse.get_position()[0]) + "," + str(mouse.get_position()[1]))
        position.append(mouse.get_position()[0])
        position.append(mouse.get_position()[1])
        position.append(input("time: "))
        temp = input("Other movement(Y/N): ")
        if temp == 'N':
            other = False


def setPosition_():
    global other
    if other:

        position.append(int(input("Insert position x: ")))
        position.append(int(input("Insert position y: ")))
        position.append(input("time: "))
        print("Position saved: " + str(position[len(position)-3]) + "," +  str(position[len(position)-2]))
        temp = input("Other movement(Y/N): ")
        if temp == 'N':
            other = False


position = []
i = 0
other = True
choose = ""
repeat = True
while (choose != "E"):
    choose = input("Insert position/set position with mouse/Exit(I/M/E)")
    other = True
    repeat = True
    i = 0
    position = []
    if (choose == "M"):
        mouse.on_middle_click(lambda: setPosition_mouse())
        while other:
            if other == False:
                break;
        mouse.unhook_all()
        while (repeat == True):
            number_movements = input("Number movements: ")
            time_movements = input("Time between movements: ")
            k = 0
            time.sleep(5)
            while (k < int(number_movements)):
                j = 0
                while j < len(position):
                    mouse.move(position[j] - mouse.get_position()[0], position[j + 1] - mouse.get_position()[1],
                               absolute=False,
                               duration=0.2)
                    mouse.click()
                    time.sleep(float(position[j + 2]))
                    j = j + 3
                time.sleep(float(time_movements))
                k = k + 1
            temp = input("Do you want repeat?(Y/N): ")
            if temp == 'N':
                repeat = False
    elif (choose == "E"):
        break;
    else:
        while other:
            setPosition_()
            if other == False:
                break;
        while (repeat == True):
            number_movements = input("Number movements: ")
            time_movements = input("Time between movements: ")
            k = 0
            time.sleep(5)
            while (k < int(number_movements)):
                print("Start")
                j = 0
                while j < len(position):
                    mouse.move(position[j] - mouse.get_position()[0], position[j + 1] - mouse.get_position()[1],
                               absolute=False,
                               duration=0.2)
                    mouse.click()
                    time.sleep(float(position[j + 2]))
                    j = j + 3
                time.sleep(float(time_movements))
                k = k + 1
            temp = input("Do you want repeat?(Y/N): ")
            if temp == 'N':
                repeat = False
