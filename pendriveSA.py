import os
import time
import shutil

USB = 'D:'
#SAVE = f'C:/USB/usb_data'
OLD=[]
dict={'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0}


def getUsb(): #if copied files exists, stop the fn
    global OLD
    NEW=os.listdir(USB)
    if (len(NEW) == len(OLD)):
        #print("The contents of the USB flash drive have not changed")
        return 0
    else:
        OLD = NEW
        return 1

def usbcheck():
    global USB
    for i in range(9):
        name = chr(i + ord('D')) + ':'
        #print (name)
        if os.path.exists(name):
            dict[chr(i + ord('D'))] = 1
            #print('disk exists' + chr(i + ord('F')))
    while (1):
        for i in range(9):
            name = chr(i + ord('D')) + ':'
            if not os.path.exists(name):
                dict[chr(i + ord('D'))] = 0
            if os.path.exists(name) and dict[chr(i+ord('D'))]==0:
                USB = name
                #print("USB stick detected")
                if getUsb():
                    try:
                        output_dirname = USB.split(":")[0]
                        SAVE = f'C:/USB/usb_disk_{output_dirname}'
                        shutil.copytree(USB, SAVE, dirs_exist_ok=True)
                        #print(USB)
                    except Exception as e:
                        print(f'Not copied {e}')
                        
        #print("No USB flash drive for the time being, start sleeping")
        time.sleep(2)# sleep time
        #print("End of hibernation")

usbcheck()
