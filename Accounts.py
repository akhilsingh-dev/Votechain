# Accounts.py
# This file holds the different types of accounts which will be used to model the voters and parties
# Voter: vid(Voter ID) | 
#

import Utility as util
import codecs


class Voter():
	def __init__(self,vid):
		self.sk,self.pk = util.generateKeyPair()								#Generates a key pair for every voter
		self.voterID = vid  													#voterID links to database


	def castVote(self,party):
		if self.getBalance() != 1:												#if the voter doesnt have a vote to give
			print("Sorry! You don't have vote to cast!")
		pass

	def __repr__(self):
		return ( "Voter ID: " + str(self.voterID) + self.sk)

	def getBalance(self):
		pass

	def sendSk(self):
		return (self.sk.to_string())




if __name__ == "__main__":
	v1 = Voter(696969)
	sign = util.applySignature(v1.sk,"BJP")
	try:
		print(util.verifySignature(v1.pk,"BJP",sign))
	except:	
		print(False)
	print(v1.sendSk())
	