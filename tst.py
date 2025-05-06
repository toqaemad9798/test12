import subprocess

user_input = input("Enter a command to run: ")
subprocess.call("echo " + user_input, shell=True)
