import airsim

import pprint
import os
import time
import math
import tempfile
from pynput import keyboard
import numpy as np 
import random

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

def on_key_press(key_char):
    global i  
    executed = False   
    if key_char == 'w':    
        new_x = client.simGetVehiclePose().position.x_val + math.cos(math.radians(i*15))
        new_y = client.simGetVehiclePose().position.y_val + math.sin(math.radians(i*15))
      
        if -130.0 <= new_x <=130.0 and -130.0 <= new_y <=130.0:
            save_view(key_char)
            client.simSetVehiclePose(airsim.Pose(airsim.Vector3r( client.simGetVehiclePose().position.x_val + math.cos(math.radians(i*15)),  client.simGetVehiclePose().position.y_val + math.sin(math.radians(i*15)), -5), client.simGetVehiclePose().orientation), True)
            executed = True
               
    # if key_char == 's':
    #     save_view(key_char)
    #     client.simSetVehiclePose(airsim.Pose(airsim.Vector3r( client.simGetVehiclePose().position.x_val - math.cos(math.radians(i*15)),  client.simGetVehiclePose().position.y_val - math.sin(math.radians(i*15)), -5), client.simGetVehiclePose().orientation), True)
    
    
    if key_char == 'd':
        save_view(key_char)
        i= (i+1)%24
        client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(client.simGetVehiclePose().position.x_val, client.simGetVehiclePose().position.y_val, -5), airsim.to_quaternion(0, 0, math.radians(i*15))), True)
        executed = True   
    if key_char == 'a':
        save_view(key_char)
        i= (i-1)%24
        client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(client.simGetVehiclePose().position.x_val, client.simGetVehiclePose().position.y_val, -5), airsim.to_quaternion(0, 0, math.radians(i*15))), True)
        executed = True
    print(client.simGetVehiclePose())  
    return executed


number_of_dataset = 128000
keys = ['w','a','d']
current_i = 0 
while current_i<number_of_dataset:
    random_number = random.randint(0, 2)
    if on_key_press(keys[random_number]):
        current_i+=1


