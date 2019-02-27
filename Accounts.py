# Accounts.py
# This file holds the different types of accounts which will be used to model the voters and parties
# Voter: vid(Voter ID) | 
#

import Utility as util
import Transaction as trans
import DBCreate as dbc
import DBQuery as dbq

class Party:
	def __init__(self,pid,title):
		self.sk,self.pk = util.generateKeyPair()
		self.partyID = pid
		self.name = title

	def __repr__(self):
		return ("Party Name: " + str(self.name) + "\nParty ID: " + str(self.partyID))

	def countVotes(self):
		pass


class Reaper:
	def __init__(self):
		print("A Reaper is born!!!")

	def donate(self,voter):
		voter.balance = True





class Voter:
	def __init__(self,title,dat,pk):
		self.sk,self.pk = util.generateKeyPair()
		
		#self.sk=None                             #initially set to None and only assigned after QR Code scanning
		#self.pk = pk								
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
		else:
			print("Record not found in DB!")
	
	def sk_QRCode(self):
		#Parsing value of self.sk(secret key) from QR Code
		#NOTE: value should be a string of the key itself as all further signing and verifying funtions uses from_string() function 
		pass
	
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




if __name__=="__main__":

	vt=dbc.create_Accounts()           #creation of accounts of all voters from DB
	n=input("Enter your full name ")
	d=input("Enter your DoB in yyyy-mm-dd format ")
	[boolean,obj]=Voter.verifyaccount(None,vt,n,d)
	if(boolean==True):
		#code for further transaction of voter if it exists, until destructor of object called
		obj.verifyDB()
		print("ulala lala le o ula la lalala le o")
	
		
	else:
		print("Voter not found in Accounts")
		              
	


	''''v1 = Voter(6969,"Akhil Singh","12-12-2012")
	p1 = Party(101,"BJP")
	v1.castVote(p1)
	print(v1)'''





