# Tello
Tello is a mini-drone from DJI:

![images](https://github.com/user-attachments/assets/d93c2721-7a1e-4f18-a25a-a3d25786c33e)


## How to charge the Tello
To charge the Tello, the drone just needs to be connected to the user's PC through its default micro-USB cable. 

You can see where to connect the cable in the following image:

![Port](https://github.com/user-attachments/assets/e53976f5-3b7b-44a6-b0d2-17569b2e595d)

## How to command the Tello
Before getting into code, the user's PC must be connected to the Tello's custom WiFi network. In order to do that, the Tello must be turned on, it'll blink until the user must connect to its network, just like with any other WiFi network.

The Tello's network usually contains its a name and some idenfication.

Once the Tello's connected, the user can command it using a Python code. For that purpose, it's necessary to have the *socket* package:

    def send_command(drone_socket, drone_address, command):
	    try:
	        drone_command = command.encode()
	        drone_socket.sendto(drone_command, drone_address)
	        print(f"Command: {command}")
	    except:
	        print(f"Error at commanding")

Fortunately, socket is a built-in package in Python. You can see a full example code at:

Here are some commands for the Python code

|**Command**  | **Description** | 
|--|--|
| command |Enter SDK mode  |
|takeoff  | Auto takeoff |
| land | Auto landing |
| streamon | Enable video streamming |
| streamoff | Disable video streamming |
| emergency | Stop motors inmediately |
| up x | Ascend to "x" cm |
| down x | Descend to "x" cm |
| left x | Fly left for "x" cm |
| right x | Fly right for "x" cm |
| forward x | Fly forward for "x" cm |
| back x | Fly backward for "x" cm |
| cw x | Rotate "x" ° clockwise |
| ccw x | Rotate "x" ° counterclockwise |
| flip x | Flip in "x" direction |
| go x y z speed | Fly to "x" "y" "z" at "speed" cm/s |

Some details to note:

 - For any distance, the range's between 20 cm and 500 cm.
 - For any rotation, the range's between 1° and 360°.
 - For any speed, the range's between -500 cm/s and 500 cm/s

In case to user wants to know more commands, there's a PDF in this repositoy to check for more information.
