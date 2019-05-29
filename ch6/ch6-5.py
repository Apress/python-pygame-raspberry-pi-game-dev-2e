#!/usr/bin/python

cmd = input("Command: ")
while cmd != 'quit':
    if cmd == 'help':
        print("Put help here")
    elif cmd == 'list':
        print("Put list here")
    else:
        print("Invalid command!")
    cmd = input("Command: ")
