from turtle import Turtle,Screen
from PIL import Image, ImageDraw, ImageFont
import os


IMAGES_FOLDER_PATH = r'data structure\bubsort_images'
imgCounter = 0
class TurtleImage(Turtle):
    def __init__(self, number):
        super().__init__()
        self.number = number
        # Determine the image size based on the length of the input number
        image_size = (25 + 20 * len(str(number)), 50)  # Adjusted size for better visibility
        self.imageSize = image_size
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
        # the counter desgined to diffrenthiate each image
        global imgCounter
        imgCounter += 1
        image_path = os.path.join(IMAGES_FOLDER_PATH, f"custom_shape{imgCounter}.gif")
        # Save the image in the subfolder
        img.save(image_path, "GIF")
        # Close the image
        img.close()
        # Register the custom shape
        Screen().addshape(image_path)
        self.penup()
        self.shape(image_path)
        self.speed('fastest')  
    def getImgWidth(self):
        return self.imageSize[0]










