import time
from pynput.mouse import Controller
import win32api
import win32con
import mouse

position = []
i = 0
other = True


def setPosition():
    global other
    if other:

        print("Position saved: " + str(mouse.get_position()[0]) + "," + str(mouse.get_position()[1]))
        position.append(mouse.get_position()[0])
        position.append(mouse.get_position()[1])
        position.append(input("time: "))
        temp = input("Other movement(Y/N): ")
        if temp == 'N':
            other = False


mouse.on_middle_click(lambda: setPosition())
while other:
    if other == False:
        break;
k = True
time.sleep(5)
while (k < 10):
    j = 0
    while j < len(position):
        mouse.move(position[j] - mouse.get_position()[0], position[j + 1] - mouse.get_position()[1], absolute=False,
                   duration=0.2)
        mouse.click()
        time.sleep(float(position[j + 2]))
        j = j + 3
    time.sleep(30)
    k = k + 1
