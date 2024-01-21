from bubbleSortGui import BubbleSortGui
from bubbleSortLogic import BubbleSortLogic
from turtleImage import TurtleImage
import tkinter as tk
import time

def bubbleSortProcess(bsGui):
    numbers = bsGui.entry.get()
    try:
        numbers = [int(n) for n in numbers.split(',')]
    except ValueError as e:
        print(e)
        return
    finally:
        bsGui.entry.delete(0, tk.END)
    bsGui.entry.config(state="disabled")
    for t in bsGui.screen.turtles():
        t.hideturtle()
    bsLogic = BubbleSortLogic()
    bsGui.screen.tracer(0)
    for index in range(len(numbers)):
        tImg = TurtleImage(numbers[index])
        bsLogic.tImgArr.append(tImg)
        bsLogic.inithilizeTimagesPos(index=index,userNumbers=numbers,tImg=tImg)
        bsLogic.setTimagesSpeed(1)

    bsGui.screen.tracer(1)
    time.sleep(1)
    bsLogic.swapTimages(numbers)
    bsGui.entry.config(state = 'normal')

def main():
    bsGui = BubbleSortGui()
    bsGui.btn.config(command=lambda:bubbleSortProcess(bsGui))
    bsGui.screen.mainloop()
main()
   



