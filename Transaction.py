# Transaction.py
# This file handles all the transactions done from one account to another
#
#

import Utility as util
import Accounts as ac
import DBQuery as dbq
import TransactionOutput as TxOut

class Transaction:

	txcount = 0

	def __init__(self,giver,taker):		#output is of type TxOutputs
		#self.value = 1
		self.sender = giver						#objects of one of classes in Accounts.py
		self.recept = taker						#objects of one of classes in Accounts.py
		self.txid = self.calcID()
		self.is_proc = False
		self.signature = None

		#UNCOMMENT THIS LINE FOR TESTING Party.countVotes()...
		#self.txoutput = TxOut.TxOutput(self.recept,self.txid)


	def __repr__(self):
		if self.is_proc == True:
			return (str(self.sender) + " gave " + str(self.recept) + " a vote!")
		else:
			return ("Transaction under process or not defined!")

	def __str__(self):
		return (str(self.sender)+str(self.recept))



	def calcID(self):									#Hashed transactionID (txid) to be given to TOuput
		Transaction.txcount += 1
		#print(str(type(self.sender.pk +"\n\n" + str(type(self.recept.pk)))
		return util.applySHA256(str(self.sender.pk) + str(self.recept.pk.to_string()) +str(Transaction.txcount))

	def signTransaction(self):
		data = self.sender.pk + self.recept.pk.to_string()
		self.signature = util.applySignature(self.sender.sk,data)
		if self.signature == None:											#signing failed
			return False
		else:																#signed successfully
			print("The Transaction was signed successfully!")
			return True

	def processTransaction(self):
		data = self.sender.pk + self.recept.pk.to_string()
		publicKey = dbq.getpublicKey(self.sender.name,self.sender.dob)
		
		if util.verifySignature(publicKey, data, self.signature):
			print("Tranasaction Signature Validated!")
			self.txoutput = TxOut.TxOutput(self.recept,self.txid)
			self.is_proc = True
		else:
			print("Transaction Signature Not Valid!")
			self.is_proc = False

		return self.is_proc


if __name__ == "__main__":

	v1 = ac.Voter("Polly Robertson","2018-11-12",dbq.getpublicKey("Polly Robertson","2018-11-12"))
	p1 = ac.Party(103,"BJP")
	

	tr1 = Transaction(v1,p1)
	tr1.signTransaction()	
	tr1.processTransaction()


	print(tr1.txid) 
	print(tr1.is_proc)
