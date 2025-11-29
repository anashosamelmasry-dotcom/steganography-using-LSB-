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
    image_byte = None
