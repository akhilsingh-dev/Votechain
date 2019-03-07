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




class Voter:
	def __init__(self,title,dat,pk):
		self.sk=None                             #initially set to None and only assigned after QR Code scanning
		self.pk = pk								
		self.voterID = 0                         #asked from voter along with name, dob and assigned only after verifying from DB 
		self.name = title
		self.dob = dat
		self.balance = True

	def verifyaccount(self,vt,name,dob):           #verifying voter from voterlist
		present=0
		for i in vt:
			flag1=(i.name==name)
			flag2=(i.dob==dob)
			if((flag1 and flag2)==True):
				present=1
				return [(flag1 and flag2),i]
			else:
				continue                          #continues till voter not found in VoterList
		if(present==0):
			return [False,None]

	def verifyDB(self):                               #verifying from database and assigning value of self.voterID post verification
		vid=int(input("Enter your voter-id "))
		if(dbq.verify(self.name,self.dob,vid)):
			self.voterID=vid
			return True
		else:
			print("Record not found in DB!")
			return False


	def sk_QRCode(self):
		#Parsing value of self.sk(secret key) from QR Code
		#NOTE: value should be a string of the key itself as all further signing and verifying funtions uses from_string() function 
		#signKey is <bytes>
		signKey = QrCodes.qr_scan()
		#strSK is <string> 
		strSK = signKey.decode().replace("\\",'\'')
		signKey = strSK.encode()

		print(type(signKey))
		print(len(signKey))
		
		_signKey = b'\xad\xd1\xdb\xe86\x07\xc4\x1b\x18\x9b\xaa\x98\x85v|U\xf8\xfa\xad \x11\xeb\x8a\x1f\x1d/\x13\xf5\xe86\xb1\xed'
		print(_signKey)
		print(signKey)

		self.sk = ecdsa.SigningKey.from_string(signKey, curve = ecdsa.SECP256k1)
		

	
	def castVote(self,party):
		if self.balance != True:												#if the voter doesnt have a vote to give
			print("Sorry! You don't have vote to cast!")
			raise Exception("NoBalance")
			return None
		else:
			t1 = trans.Transaction(self,party)
			t1.signTransaction()
			is_proc = t1.processTransaction()
			if is_proc:
				self.balance = False
				print("Your vote has been casted successfully!")
				return t1
			else:
				print("Sorry! Your vote could not be processed!")
				return None


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

	bjp = Party(103,"BJP")
	inc = Party(101,"INC")

	tr1 = Tx.Transaction(v1,bjp)
	tr2 = Tx.Transaction(v2,inc)
	tr3 = Tx.Transaction(v3,inc)
	tr4 = Tx.Transaction(v4,inc)
	
	txQueue = []
	txQueue.append(tr1)
	txQueue.append(tr2)
	b1 = Block.Block(txQueue)					
	
	txQueue2 = []
	txQueue2.append(tr3)
	txQueue2.append(tr4)
	b2 = Block.Block(txQueue2)
	
	session1.addBlock(b1)				#calls link which sets prevhash and mines the block 
	session1.addBlock(b2)
	
	#session1.blockchain[1].tx[1].txoutput.receptor = bjp 			#trying to tamper the data
	
	print("\n\nBJP GOT "+ str(bjp.countVotes(session1))+" VOTES!\n\n")
	print("\n\nINC GOT "+ str(inc.countVotes(session1)) +" VOTES!\n\n")


