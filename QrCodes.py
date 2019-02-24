# QrCodes.py
#code to generate and scan QR codes


#import necessary libraries
from pyzbar import pyzbar
import argparse
import cv2


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())


#

