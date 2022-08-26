from stegano import lsb

choice =int(input(""" Please choose from the bellow alternatives :
        1 Encode 
        2 Decode 
""")) 

def encode_message():
    secret_image = input(">> Specify the image you want to use: ")
    secret_message = input(">> What is the message you want to encode: ")
    secret = lsb.hide(secret_image, secret_message) 
    secret.save("encoded_image.png")
def decode_message():
    clear_message = lsb.reveal("encoded_image.png")
    print(clear_message) 
    
if choice == 1:
    encode_message()
elif choice == 2:
    decode_message()
else:
    print("Wrong input please try again")   