import os
import time
import wmi
import shutil

def usbcontent(USB, old_contents):
    new_contents = os.listdir(USB)
    if set(new_contents) == set(old_contents):
        print("The contents of the USB flash drive have not changed")
        return False, old_contents
    else:
        print("USB contents have changed")
        return True, new_contents

def usbcopy():
    c = wmi.WMI()
    print("Watching for USB devices...")
    old_contents = []
    while True:
        for disk in c.Win32_LogicalDisk():
            if disk.Description == "Removable Disk":
                USB = disk.DeviceID
                name = disk.VolumeName
                print("USB detected:", USB)
                changed, old_contents = usbcontent(USB, old_contents)
                if changed:
                    try:
                        save_path = f'D:/bo/usb_{name}'
                        try:
                            shutil.copytree(USB, save_path, dirs_exist_ok=True)
                            print('Done')
                        except Exception as e:
                            print(f'Not copied: {e}')
                    except Exception as e:
                        print(f"Error during USB copy: {e}")
        time.sleep(5)
        print("Checking for USB devices...")

usbcopy()
