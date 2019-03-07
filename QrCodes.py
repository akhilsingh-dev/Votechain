# QrCodes.py
#code to generate and scan QR codes


from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
 
# construct the argument parser and parse the arguments
def qr_scan():
	
	# initialize the video stream and allow the camera sensor to warm up
	print("[INFO] starting video stream...")
	vs = VideoStream(src=0).start()
	time.sleep(1.0)
	breaker = False
	while True:
		# grab the frame from the threaded video stream and resize it to
		# have a maximum width of 400 pixels
		frame = vs.read()
		frame = imutils.resize(frame, width=400)
	 	
		# find the barcodes in the frame and decode each of the barcodes
		barcodes = pyzbar.decode(frame)


		# loop over the detected barcodes
		for barcode in barcodes:
			# extract the bounding box location of the barcode and draw
			# the bounding box surrounding the barcode on the image
			(x, y, w, h) = barcode.rect
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
	 
			# the barcode data is a bytes object so if we want to draw it
			# on our output image we need to convert it to a string first
			barcodeData = barcode.data.decode("utf-8")
			breaker = True
			barcodeType = barcode.type
	 
			# draw the barcode data and barcode type on the image
			text = "{} ({})".format(barcodeData, barcodeType)
			cv2.putText(frame, text, (x, y - 10),
				cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	 
			
		# show the output frame
		cv2.imshow("Barcode Scanner", frame)
		key = cv2.waitKey(1) & 0xFF
	 
		# if the `q` key was pressed, break from the loop
		if key == ord("q") or breaker==True:
			break
	 
	# close the output CSV file do a bit of cleanup
	print("[INFO] cleaning up...")
	cv2.destroyAllWindows()
	vs.stop()
	#print(type(barcode.data))
	return barcode.data								#This is the bytes object stroing the secretKey

if __name__ == "__main__":
	print(qr_scan())
	print(type(qr_scan()))
