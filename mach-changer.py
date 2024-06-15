#this is a very simple mac address changer

import subprocess
def manual_mac():
    intface = input("specify the interface: ")
    nmac = input("enter the new mac address: ")

    print(f'[+] changing mac_address to {nmac}\n')
    try:
        #.run([]), it is an alternate of .run("cmd", shell=True)
        #this is more secure, old run will let multiple cmnds go through it if used wit input (input>eth0;ls;)
        #the new one will only take the list[0] as a cmnd and others as a part of the cmnd(not a new cmnd)
        subprocess.run(["ifconfig", intface,  "down"])
        subprocess.run(["ifconfig", intface, "hw", "ether", nmac])
        subprocess.run(["ifconfig", intface,"up"])

    except:
        print(f'[-] An error occured')
