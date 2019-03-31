#Library Required to Run this
import pyqrcode

#file will be generated inside the folder the script is in

#file_name should be first name of person or voter id whichever you prefer to implement
#data will be the private_key id which will be used generate the QR code of person


def qr_gen(file_name="temp", data="abc"):                                       #data is the private_key id to generate QR
    
    #Creating the QRCode object with proper specifications 
    big_code = pyqrcode.create(data, error='L', version=2, mode=None)

    #Converting it into png with provided filename and scale
    big_code.png(f"{file_name}.png" , scale = 7)


#Function Calling Example
#qr_gen("File name","data")
