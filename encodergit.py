print("option 1 - type message")
print("option 2 - take the message from a text file")
choice = input("enter the option 1 or 2 ")
if choice == "1":
    message = input("Enter the message")
    if message == "":
        print("Error Message is empty")
        message = None
elif choice == "2":
    textfile = input("Enter text file")
    if not textfile.lower().endswith(".txt"):
        print("Error File needs to end with .txt")
        message = None
    else:
        try:
            f = open(textfile, "r" , encoding ="utf-8")
            message = f.read()
            f.close()

            if message == "":
                print("Error the file is empty")
                message = None
            else:
                print("Successfully took the message from file")
        except:
            print("Error Could not read the file")
            message = None
else:
    print("Error Invalid choice")
    message = None
print("Enter image")
imagefile = input("Enter BMP image file")
if imagefile == "":
    print("Error No image was enterted")
    imagefile = None
elif not (imagefile.lower().endswith(".bmp")):
    print("Error File needs to end with .bmp")
    imagefile = None
file_exists = True
try:
    f = open(imagefile, "rb")
    f.close()
except:
    print("Error the imagefile is not found or cannot be opened")
    file_exists = False
try:
    f = open(imagefile, "rb")
    image_byte = []
    byte = f.read(1)
    while byte != b"":
        image_byte.append(ord(byte))
        byte = f.read(1)
    f.close()
    if len(image_byte) < 100:
        print("Error Image is too small")
        image_byte = None
    else:
        print(f"sucessfully Read", len(image_byte), "bytes from image")
except:
    print("Error Could not read image bytes.")
    image_byte = None
end_of_message = ")))))"
message = message + end_of_message
binary_message = ''.join(format(ord(c), '08b') for c in message)
message_bits = len(binary_message)
print(f"Message length {len(message)}")
print(f"Binary bits needed {message_bits}")
if message_bits > len(image_byte):
        print("Error Message is too long for this image")
        print(f"Maximum message length: {len(image_byte) // 8} characters")
modified_bytes = image_byte.copy()
for bit_index in range(message_bits):
    message_bit = int(binary_message[bit_index])
    current_byte = modified_bytes[bit_index]
    if current_byte % 2 == 1:
        current_byte -= 1
    current_byte += message_bit
    modified_bytes[bit_index] = current_byte
print(f"Successfully embedded {message_bits} bits")
filename = "security.bmp"
try:
    f = open(filename, "wb")
    for byte in modified_bytes:
        f.write(bytes([byte]))
    f.close()
    print(f"Successfully saved as '{filename}'")
    successfully = True
except:
    print(f"Error Couldn't save the file '{filename}'")
    successfully = False