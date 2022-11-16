import os
import time

dict={'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0}
def usbcheck():
    global USB
    for i in range(9):
        name = chr(i + ord('D')) + ':'
        print (name)
        if os.path.exists(name):
            dict[chr(i + ord('D'))] = 1
            print('disk exists ' + chr(i + ord('D')))

    while (1):
        for i in range(26):
            name = chr(i + ord('D')) + ':'
            if not os.path.exists(name):
                dict[chr(i + ord('D'))] = 0
            if os.path.exists(name) and dict[chr(i+ord('D'))]==0:
                USB = name
                print("USB stick detected", USB, 'is usb')

        print("No USB flash drive for the time being, start sleeping")
        time.sleep(1)# sleep time
        print("End of hibernation")
usbcheck()