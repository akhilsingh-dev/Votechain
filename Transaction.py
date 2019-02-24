# Transaction.py
# This file handles all the transactions done from one account to another
#
#

import Utility as util
import Accounts as ac

class Transaction:
	def __init__(self,giver,taker):
		self.value = 1
		self.sender = giver						#objects of one of classes in Accounts.py
		self.recept = taker						#objects of one of classes in Accounts.py
		self.is_proc = False
		self.signature = None


	def __repr__(self):
		if self.is_proc == True:
			return (str(self.sender) + " gave " + str(self.recept) + " a vote!")
		else:
			return ("Transaction under process or not defined!")

	def signTransaction(self):
		data = self.sender.pk + self.recept.pk
		self.signature = util.applySignature(self.sender.sk,data)
		if self.signature == None:										#signing failed
			return False
		else:															#signed successfully
			print("The Transaction was signed successfully!")
			return True

	def processTransaction(self):
		publicKey = getpublicKey(self.sender.name,self.sender.dob)
		if util.verifySignature(publicKey, , self.signature):


if __name__ == "__main__":
	v1 = ac.Voter(102)
	v2 = ac.Voter(103)
	tr1 = Transaction(v1,v2)
	print(tr1) 
	print(tr1.is_proc)
