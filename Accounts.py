# Accounts.py
# This file holds the different types of accounts which will be used to model the voters and parties
# Voter: vid(Voter ID) | 
#

import Utility as util
import Transaction as Tx
import DBCreate as dbc
import DBQuery as dbq
import QrCodes 
import ecdsa
import Blockchain as Bch
import Block
import TransactionOutput


class Party:
	def __init__(self,pid,title):
		self.sk,self.pk = util.generateKeyPair()
		self.partyID = pid
		self.name = title

	def __repr__(self):
		return ("Party Name: " + str(self.name) + "\nParty ID: " + str(self.partyID))

	def __str__(self):
		return (str(self.name) + str(self.partyID))



	def countVotes(self,session):
		count = 0
		isvalid = session.validate()
		if isvalid:
			for i in range(1,len(session.blockchain)):								
				for j in range(len(session.blockchain[i].tx)):					
					if session.blockchain[i].tx[j].txoutput.isMine(self.pk):		#check if the vote is yours
						count += 1													#if yes, add one to count
		else:
			print("[ERROR] : Blockchain tampered!")		
		isvalid = session.validate()
		return count



class Reaper:
	def __init__(self):
		print("A Reaper is born!!!")

	def donate(self,voter):
		voter.balance = True

	def snatch(self,voter):
		voter.balance = False
		pass



class Voter:
	def __init__(self,title,dat,pk):
		self.sk=None                             #initially set to None and only assigned after QR Code scanning
		self.pk = pk								
		self.voterID = 0                         #asked from voter along with name, dob and assigned only after verifying from DB 
		self.name = title
		self.dob = dat
		self.balance = True


	def sk_QRCode(self):
		#Parsing value of self.sk(secret key) from QR Code
		#NOTE: value should be a string of the key itself as all further signing and verifying funtions uses from_string() function 
		x = QrCodes.qr_scan()
		self.sk = dbq.getprivateKey(int(x))
		

	
	def castVote(self,party):
		if self.balance != True:												#if the voter doesnt have a vote to give
			print("Sorry! You don't have vote to cast!")
			raise Exception("NoBalance")
			return None
		else:
			t1 = Tx.Transaction(self,party)
			t1.signTransaction()
			is_proc = t1.processTransaction()
			if is_proc:
				self.balance = False
				print("Your vote has been casted successfully!")
				return t1
			else:
				print("Sorry! Your vote could not be processed!")
				return None

	
	#def __del__(self):
	#	dbq.deleteData(self.name,self.dob,self.voterID)
	#	print("This account is now deleted!")


	def __repr__(self):
		return ( "Name: " + self.name + "\nVoter ID: " + str(self.voterID))


	def __str__(self):
		return (str(self.voterID))



if __name__=="__main__":


	session1 = Bch.Blockchain(4)

	v1 = Voter("Nicole Okeeffe","2018-11-26",dbq.getpublicKey("Nicole Okeeffe","2018-11-26"))
	v2 = Voter("Kenneth Alvarado","2018-11-25",dbq.getpublicKey("Kenneth Alvarado","2018-11-25"))
	v3 = Voter("Alex Scott","2018-11-24",dbq.getpublicKey("Alex Scott","2018-11-24"))
	v4 = Voter("Isaac Carty","2018-11-23",dbq.getpublicKey("Isaac Carty","2018-11-23"))

	voterList = [v1,v2,v3,v4]
	transactionList = []

	bjp = Party(103,"BJP")
	inc = Party(101,"INC")

	for i in range(len(voterList)):
		print("Please Show your QR Code...")
		voterList[i].sk_QRCode()
		transactionList.append(voterList[i].castVote(bjp))

	
	
	b1 = Block.Block(transactionList[0:2])					
	
	b2 = Block.Block(transactionList[2:4])
	
	session1.addBlock(b1)				#calls link which sets prevhash and mines the block 
	session1.addBlock(b2)
	
	#session1.blockchain[1].tx[1].txoutput.receptor = bjp 			#trying to tamper the data
	
	print("\n\nBJP GOT "+ str(bjp.countVotes(session1))+" VOTES!\n\n")
	print("\n\nINC GOT "+ str(inc.countVotes(session1)) +" VOTES!\n\n")

	



