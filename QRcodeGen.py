#Library Required to Run this
import pyqrcode

#file will be generated inside the folder the script is in

#file_name should be first name of person or voter id whichever you prefer to implement
#data will be the private key which will be used generate the QR code of person


def qr_gen(file_name="temp", data="abc"):                                       #data is the private key to generate QR
    
    #Creating the QRCode object with proper specifications 
    big_code = pyqrcode.create(f"{data}", error='L', version=27, mode=None)

    #Converting it into png with provided filename and scale
    big_code.png(f"{file_name}.png" , scale = 4)


#Function Calling Example
#qr_gen("File Name","Private_Key")
