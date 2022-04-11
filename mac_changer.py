import subprocess

interface_name = input("Enter the interface name you want to change MAC address:\n")

subprocess.call("ifconfig " + interface_name + " down", shell = True)
print("ifconfig " + interface_name + " down")

new_mac_address = input("Enter the new MAC address:\n")

subprocess.call("ifconfig " + interface_name + " hw ether " + new_mac_address, shell = True)
print("ifconfig " + interface_name + " hw ether " + new_mac_address)
subprocess.call("ifconfig " + interface_name + " up", shell = True)
print("ifconfig " + interface_name + " up")
