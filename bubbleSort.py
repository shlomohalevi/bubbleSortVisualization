from turtle import Turtle,Screen
from PIL import Image, ImageDraw, ImageFont
import os
import tkinter as tk
import time
OFSSET_BETWEEN_TIMAG_IMAGES = 25
IMAGES_FOLDER_PATH = r'data structure\bubsort_images'
# global variable
imgCounter = 0

def on_escape():
    try:
        for file in os.listdir(IMAGES_FOLDER_PATH):
            file_path = os.path.join(IMAGES_FOLDER_PATH, file)
            os.remove(file_path)
    except Exception as e:
        print(e)
    try:
        Screen().bye()  
    except Screen().Terminator:
        pass  

def create_custom_shape(number):
    global imgCounter
    imgCounter+=1
    # Determine the image size based on the length of the input number
    image_size = (25 + 20 * len(str(number)), 50)  # Adjusted size for better visibility
    # Ensure the subfolder exists
    if not os.path.exists(IMAGES_FOLDER_PATH):
        os.makedirs(IMAGES_FOLDER_PATH)

    # Create a blank image
    img = Image.new("RGB", image_size, (255, 255, 255, 0))
    # Get a drawing context
    draw = ImageDraw.Draw(img)
    # Choose a font and size
    font_size = 40
    font = ImageFont.truetype("arial.ttf", font_size)
    # Choose the text color
    text_color = (0, 0, 0)
    # Draw the text on the image
    xoffset =  11
    yoffset = 3
    draw.text((xoffset, yoffset), str(number), font=font, fill=text_color)
    # Construct the full path to save the image in the subfolder
    image_path = os.path.join(IMAGES_FOLDER_PATH, f"custom_shape{imgCounter}.gif")
    # Save the image in the subfolder
    img.save(image_path, "GIF")
    # Register the custom shape
    Screen().addshape(image_path)


def getInitialTimage():
    t = Turtle()
    img_path = os.path.join(IMAGES_FOLDER_PATH, f'custom_shape{imgCounter}.gif')
    t.shape(img_path)
    t.speed('fastest')  
    t.penup()
    return t

def getImgSize():
    IMAGES_FOLDER_PATH = 'data structure/bubsort_images'
    img_path = os.path.join(IMAGES_FOLDER_PATH, f'custom_shape{imgCounter}.gif')
    image = Image.open(img_path)
    return image.size
def insertTImgObjToDataStructurs(tImg,currentTimgsize,timagarr ,dtImgObj):
    timagarr.append(tImg)
    dtImgObj[tImg] = dtImgObj.get(currentTimgsize[0],currentTimgsize[0])
def setInitialImagePos(tImg,index,currentimgsize,previmgsize,imgObjects,my_list):
    # Calculate the initial position based on the length of my_list
    initial_offset = len(my_list) // 2 * 85
    startPosx = - initial_offset
    tImg.setpos(x=startPosx, y=0)
    Screen().tracer(1)
    if index != 0:
        # psitioning calculations
        lastx = imgObjects[index-1].xcor()
        lastoffset = previmgsize[0] / 2
        newoffset = currentimgsize[0] / 2 + OFSSET_BETWEEN_TIMAG_IMAGES
        startPosx = lastx + lastoffset + newoffset
    tImg.setx(startPosx)
    previmgsize = currentimgsize
    return startPosx



def bubbleSort(my_list):
    global imgCounter
    imgCounter = 0
    imgObjects = []
    dImgObj = {}
    previmgsize = 0
    for index in range(len(my_list)):
        Screen().tracer(0)
        create_custom_shape(my_list[index])
        currentimgsize =  getImgSize()
        tImg = getInitialTimage()
        insertTImgObjToDataStructurs(tImg,currentimgsize,imgObjects,dImgObj)
        # set and calculate inithial turtle img pos based on several parameters
        setInitialImagePos(tImg,index,currentimgsize,previmgsize,imgObjects,my_list)
        previmgsize = currentimgsize
    time.sleep(1)
    for tImg in imgObjects:
        tImg.speed(1)
    for index in range(len(my_list)):
        for j in range(0, len(my_list)-index-1):
            # Swap if the element found is greater than the next element
            if my_list[j] > my_list[j+1]:
                tempx = dImgObj[imgObjects[j]] + OFSSET_BETWEEN_TIMAG_IMAGES
                imgObjects[j].forward(dImgObj[imgObjects[j+1]] + OFSSET_BETWEEN_TIMAG_IMAGES)
                imgObjects[j+1].backward(tempx)
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                imgObjects[j], imgObjects[j+1] = imgObjects[j+1], imgObjects[j]
        
def getInputFromUser():
    userinput = entry.get()
    try:
        userinput = [int(n) for n in userinput.split(',')]
    except ValueError as e:
        print(e)
        return
    finally:
        entry.delete(0, tk.END)
    for t in Screen().turtles():
        t.hideturtle()
    entry.config(state="disabled")
    bubbleSort(userinput)
    entry.config(state="normal")
def screenSetup():
    screen = Screen()
    screen.setup(width = 0.7, height = 0.7)
    screen.colormode(255)
    screen.bgcolor(11, 99,220)
    screen.onkey(on_escape, "Escape")
    screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", on_escape)
    # Listen for key events
    screen.listen()
        
screenSetup()
root = Screen()._root
labeltxt = tk.Label(root,text='please insert only numbers seperated by a coma',fg='blue', font=("Helvetica", 16))
labeltxt.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)
btn = tk.Button(root,text='insert numbers',command = getInputFromUser)
btn.pack(pady=10)
Screen().mainloop()
   


         



        




    







    

   
           
            




            









