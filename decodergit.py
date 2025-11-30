image = input("Enter BMP image file to decode ")
if not image.lower().endswith(".bmp"):
    print("Error file needs end with .bmp")
    exit()
try:
    f = open(image, "rb")
    image_byte = []
    byte = f.read(1)
    while byte != b"":
        image_byte.append(ord(byte))
        byte = f.read(1)
    f.close()
except:
    print("Error Can't read the file")
    exit()