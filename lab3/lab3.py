LOG_FILE = "setupapi.dev.log"
DEVICE_USB_STR = "USBSTOR"
DEVICE_START_STR = "[Device Install (Hardware initiated)"
is_device_found = False

with open(LOG_FILE) as f:
    for line in f:
        if DEVICE_START_STR in line and DEVICE_USB_STR in line:
            usb_1 = line.split("#")[1].split("&")
            usb_2 = line.split("#")[2].strip()
            usb_3 = next(f).split("start")[1].strip()
            print("Vendor: ", usb_1[1])
            print("Product: ", usb_1[2])
            print("Revision: ", usb_1[3])
            print("Serial: ", usb_2)
            print("Time: ", usb_3)
            print("")
