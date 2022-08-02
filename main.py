import time
from pynput.mouse import Controller
import win32api
import win32con
import mouse

position = []
i = 0

other = True
mouse.on_right_click(lambda: print(mouse.get_position()))
while 1:
    1
'''
while other:
    position.append(input("Position x: "))
    position.append(input("Position Y: "))
    position.append(input("time: "))
    temp = input("Other movement(Y/N): ")
    if temp == 'N':
        other = False
j = 0
while j < len(position):
    mouse.move(position[j], position[j + 1], absolute=False, duration=0.2)
    time.sleep(float(position[j + 2]))
    j = j + 3
'''