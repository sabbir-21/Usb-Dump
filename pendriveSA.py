import tkinter
import os
from tkinter import filedialog as fd
import time
import datetime
copytime = str(round(time.time()))
cdate = str(datetime.datetime.now().date())
USB = 'F:'
SAVE = f'C:/USB/usb_{cdate}_{copytime}'
OLD=[]
dict={'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0}

def usbcopy():
    import shutil
    shutil.copytree(USB, SAVE)
    print('Done')

def getUsb(): #if copied files exists, stop the fn
    global OLD
    NEW=os.listdir(USB)
    if (len(NEW) == len(OLD)):
        print("The contents of the USB flash drive have not changed")
        return 0
    else:
        OLD = NEW
        return 1

def usbcheck():
    global USB
    for i in range(7):
        name = chr(i + ord('F')) + ':'
        print (name)
        if os.path.exists(name):
            dict[chr(i + ord('F'))] = 1
            print('disk exists' + chr(i + ord('F')))

    while (1):
        for i in range(7):
            name = chr(i + ord('F')) + ':'
            if not os.path.exists(name):
                dict[chr(i + ord('F'))] = 0
            if os.path.exists(name) and dict[chr(i+ord('F'))]==0:
                USB = name
                print("USB stick detected")
                if getUsb():
                    try:
                        usbcopy()
                    except Exception as e:
                        print(Exception, e)
        print("No USB flash drive for the time being, start sleeping")
        time.sleep(1)# sleep time
        print("End of hibernation")

def choseDir():
    global SAVE
    SAVE=fd.askdirectory(parent=root,initialdir="/",title='Pick a directory')+'/usbCopy'
    print('SAVE IN ' + SAVE)


def clickButton():
    root.withdraw()
    usbcheck()

if __name__ == '__main__':
    root=tkinter.Tk()
    #tmp = open("tmp.ico", "wb+")
    #tmp.write(base64. b64decode(img))
    #tmp.close()
    #root.iconbitmap("tmp.ico")
    root.title('USB Dumper')
    root.geometry('700x400')
    tkinter.Label(root,text=f' Modified by Sabbir: Original: \ngithub.com/Ginray/USB-Dumper/issues\n\n').pack()
    tkinter.Button(root,text='Change Save Directory',command=choseDir).pack()
    tkinter.Button(root,text='Start USB Dumper',command=clickButton).pack()
    root.mainloop()
