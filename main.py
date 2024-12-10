#!/usr/bin/env python
import socket
import time

def send_command(drone_socket, drone_address, command):
    try:
        drone_command = command.encode()
        drone_socket.sendto(drone_command, drone_address)
        print(f"Command: {command}")
    except:
        print(f"Error at commanding")

if __name__ == '__main__':
    tello_ip = '192.168.10.1' # Tello's IP
    tello_port = 8889 # Tello's Port
    tello_address = (tello_ip, tello_port)

    # Socket opens
    tello_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Let's begin!")

    # Enviar el comando de inicio
    send_command(tello_socket, tello_address,'command')
    time.sleep(1) # Wait for next command

    # Drone takes off
    send_command(tello_socket, tello_address,'takeoff')
    time.sleep(3) # Wait for next command

    # Drone translates 50 cm forward
    send_command(tello_socket, tello_address, 'forward 50')
    time.sleep(3) # Wait for next command

    # Drone rotates 90 ° clockwise
    send_command(tello_socket, tello_address, 'cw 90')
    time.sleep(3) # Wait for next command

    # Drone lands
    send_command(tello_socket, tello_address, 'land')

    # Socket closes
    tello_socket.close()
    print("Let's finish!")
