import airsim

import pprint
import os
import time
import math
import tempfile
from pynput import keyboard
import numpy as np 


client = airsim.VehicleClient()
client.confirmConnection()
client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(0, 0, -5), airsim.to_quaternion(0, 0, 0)), True)

i = 0 
image_index = 0

def save_view(pressed_key):
    global image_index
    responses = client.simGetImages([
        airsim.ImageRequest("0", airsim.ImageType.Scene, False, False),
    ])

    response = responses[0]
    
    # the original image has 4 channels. So the below code will make it RGB (3 channels)
    img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8)

    # reshape array to 3 channel image array H X W X 3
    img_rgb = img1d.reshape(response.height, response.width, 3) 

    # write to png 
    airsim.write_png(os.path.normpath('data\py' + str(image_index)+ '_'+ str(pressed_key)+ '.png'), img_rgb) 
    image_index+= 1

def on_key_press(key):
    global i
   
    try:
        # Retrieve the character representation of the key
        key_char = key.char
        if key_char == 'w':
            save_view(key_char)
            client.simSetVehiclePose(airsim.Pose(airsim.Vector3r( client.simGetVehiclePose().position.x_val + math.cos(math.radians(i*15)),  client.simGetVehiclePose().position.y_val + math.sin(math.radians(i*15)), -5), client.simGetVehiclePose().orientation), True)
           
        if key_char == 's':
            save_view(key_char)
            client.simSetVehiclePose(airsim.Pose(airsim.Vector3r( client.simGetVehiclePose().position.x_val - math.cos(math.radians(i*15)),  client.simGetVehiclePose().position.y_val - math.sin(math.radians(i*15)), -5), client.simGetVehiclePose().orientation), True)
        
        
        if key_char == 'd':
            save_view(key_char)
            i= (i+1)%24
            client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(client.simGetVehiclePose().position.x_val, client.simGetVehiclePose().position.y_val, -5), airsim.to_quaternion(0, 0, math.radians(i*15))), True)
            
        if key_char == 'a':
            save_view(key_char)
            i= (i-1)%24
            client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(client.simGetVehiclePose().position.x_val, client.simGetVehiclePose().position.y_val, -5), airsim.to_quaternion(0, 0, math.radians(i*15))), True)
        print(client.simGetVehiclePose())  

        
    except AttributeError:
        # Special keys like 'esc', 'enter', 'shift', etc.
        key_name = key.name
        print("Key pressed:", key_name)

def on_key_release(key):
    # Handle key release event if needed
    pass
listener = keyboard.Listener(
    on_press=on_key_press,
    on_release=on_key_release
)

# Start listening for keyboard events
listener.start()

# Keep the program running
listener.join()
