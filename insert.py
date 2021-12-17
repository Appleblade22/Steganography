import os
import io
import shutil

import PIL.Image
from datetime import date

today = date.today()


def insert_message(ifile, smessage, ofile):
    shutil.copyfile(ifile, ofile)
    with open(ofile, "ab") as f:
        f.write(bytes(smessage, "utf-8"))


def open_message(ifile):
    with open(ifile, "rb") as f:
        data = f.read()
        offset = data.index(bytes.fromhex('FFD9'))

        f.seek(offset + 2)
        print(f.read())


def insert_images(ifile, smessage, ofile):
    shutil.copyfile(ifile, ofile)
    Img = PIL.Image.open(smessage)
    byte_array = io.BytesIO()
    Img.save(byte_array, format="JPEG")

    with open(ofile, "ab") as f:
        f.write(byte_array.getvalue())


def decode(iname):
    # for image
    try:
        with open(iname, "rb") as f:
            data = f.read()
            offset = data.index(bytes.fromhex('FFD9'))

            f.seek(offset + 2)
            new_img = PIL.Image.open(io.BytesIO(f.read()))
            new_img.save("output.png")
            print("Image injection found!")
            print("Image saved as output.png")
            return
    except PIL.UnidentifiedImageError:
        print("No image injection found")
    except FileNotFoundError:
        print("File not found")

    # for text
    try:
        with open(iname, "rb") as f:
            data = f.read()
            offset = data.index(bytes.fromhex('FFD9'))
            f.seek(offset + 2)
            with open("output.txt", "w") as f2:
                f2.write(f.read().decode("utf-8"))
            print("\nText Injection found")
            print("Text saved in output.txt")
            return
    except FileNotFoundError:
        print("File not found")


while True:
    print("1.) Insert message into Image file")
    print("2.) Insert Image into Image file")
    print("3.) Decode message from Image file")
    print("4.) Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Inserting message into Image file")
        print("Note That Image file should be in same directory as this python script is!")
        print("And Enter full Name of Image file with extension Like (new.png)")
        Found = False
        while not Found:
            print("\nEnter the name of the image file: ")
            image_file = input()
            if os.path.exists(image_file):
                Found = True
            else:
                print("Image file not found!")
                print("To exit enter 'q' else press any key to continue")
                if input() == "q":
                    exit()
        print("Enter your secret message: ")
        secret_message = input()
        output_file = 'M_' + today.strftime("%b-%d-%Y") + '.jpg'
        print("Inserting message into Image file")
        insert_message(image_file, secret_message, output_file)
        print("Message inserted successfully!")
        print("Output file is: ", output_file)
        print("\n")

    elif choice == "2":
        print("Inserting Image into Image file")
        print("Note That Image file should be in same directory as this python script is!")
        print("And Enter full Name of Image file with extension Like (new.png)")
        Found = False
        while not Found:
            print("\nEnter the name of the image file: ")
            image_file = input()
            if os.path.exists(image_file):
                Found = True
            else:
                print("Image file not found!")
                print("To exit enter 'q' else press any key to continue")
                if input() == "q":
                    exit()

        Found = False
        while not Found:
            print("\nEnter the name of the image file to be inserted: ")
            insert_image = input()
            if os.path.exists(insert_image):
                Found = True
            else:
                print("Image file not found!")
                print("To exit enter 'q' else press any key to continue")
                if input() == "q":
                    exit()
        output_file = 'I_' + today.strftime("%b-%d-%Y") + '.jpg'
        print("Inserting Image into Image file")
        insert_images(image_file, insert_image, output_file)
        print("Image inserted successfully!")
        print("Output file is: ", output_file)
        print("\n")

    elif choice == "3":
        print("Note That Image file should be in same directory as this python script is!")
        print("And Enter full Name of Image file with extension Like (new.png)")
        Found = False
        while not Found:
            print("\nEnter the name of the image file: ")
            image_file = input()
            if os.path.exists(image_file):
                Found = True
            else:
                print("Image file not found!")
                print("To exit enter 'q' else press any key to continue")
                if input() == "q":
                    exit()
        print("Decoding message from Image file")
        decode(image_file)

    elif choice == "4":
        print("Exiting")
        exit()
    else:
        print("Invalid choice")
        print("\n")
        continue


