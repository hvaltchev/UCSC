#!/usr/bin/env python3
"""lab15_3.py (Optional)
Finds and reports the OS and IP address of this machine.
"""
import subprocess
import sys

def GetLinuxIP():
    """Returns the IP address for Linux machines."""
    for line in GetOutput("inet addr:").split('\n'):
        address_at = line.find("inet addr:")
        if address_at == -1:
            continue
        return line[address_at + 10:].split()[0]

def GetOS_X_IP():
    """Returns the IP address for Apple machines."""
    output = GetOutput("/sbin/ifconfig")
    inet_at = output.rfind("inet ") + 5
    inet_end = output.find(" ", inet_at)
    return output[inet_at:inet_end]

def GetOutput(command):
    with subprocess.Popen(command, stdout=subprocess.PIPE) as popen_obj:
        # bytes are delivered - converting to str
        return str(popen_obj.stdout.read()) 




    
def GetWindowsIP():
    """Returns the IP address for Windows machines."""

    for line in GetOutput(("c:\windows\system32\ipconfig.exe",
                           "/all")).split('\n'):
        address_at = line.find("IPv4 Address")
        if address_at == -1:
            continue
        ip_address = line.split()[-1]
        if ip_address[-1] == ')':
            ip_address = ip_address[:ip_address.index('(')]
        return ip_address

def main():                          
    this_os = sys.platform            
    print("Platform is", this_os)
    if this_os in ("darwin",):
        print(GetOS_X_IP())
    elif this_os.find("win") > -1:
        print(GetWindowsIP())      
    elif this_os.find("linux") > -1:
        print(GetLinuxIP())          
    else:                           
        print("Unknown OS")          
                                    
if __name__ == "__main__":          
    main()                          
