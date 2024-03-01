'''
Author(s): Lane Affield
Created: 02/28/2024
Last Update: 03/01/2024
Last Updated by: Lane Affield
Update Description: fixed code to actually blend the images.

Desrciption: Lane Affields Test Ground for The AI Capstone

'''
from PIL import Image
from randimage import get_random_image , show_array
import matplotlib
import os
#Finds and Retrieves the image dimensions
def image_size_retrieval(file_path):
    image = Image.open(file_path)
    print(image.size)
    #image.show()
    return image.size

#generates a random image that is the size of the image retrieved
def overlay_generator(original_image):
    overlay = get_random_image(original_image.size) #retrives image size, generates image
    #print("Done with step 1")
    matplotlib.image.imsave("overlay.jpeg", overlay) #saves image to use NOTE: possibly Change this, not sure how
    #print("Done with step 2")
    overlay = Image.open('overlay.jpeg')
    #print("Done with step 3")
    overlay.show()

#image_to_alter = Image.open("AffieldTestImage1.jpeg")
#overlay_generator(image_to_alter)


def blender(original_image): 
    image_to_alter = Image.open(original_image)
    overlay_generator(image_to_alter)
    overlay_image = Image.open("overlay.jpeg")
    image_to_alter = Image.open(original_image)
    print("loaded image to alter")
    overlay_image = overlay_image.resize(image_to_alter.size)
    print("overlay resized")
    blended_image = Image.blend(image_to_alter, overlay_image,.01)
    print("blended image created")
    blended_image.show(blended_image)
    os.remove("overlay.jpeg")



#blender("AffieldTestImage1.jpeg")
blender("/Users/laneaffield/Desktop/Capstones/DeepFakeCapstone/misc/photos/TestImage1.jpg")

