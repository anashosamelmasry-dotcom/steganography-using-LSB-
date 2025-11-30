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
bits = ""
for byte in image_byte:
    bits += str(byte % 2)
message = ""
for i in range(0, len(bits), 8):
    byte_ch = bits[i:i+8]
    if len(byte_ch) < 8:
        break
    character = chr(int(byte_ch, 2))
    message += character
    if ")))))" in message:
        break
message = message.replace(")))))", "")
print(message) 