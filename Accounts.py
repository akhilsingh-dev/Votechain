# Accounts.py
# This file holds the different types of accounts which will be used to model the voters and parties
# Voter: vid(Voter ID) | 
#

import Utility as util
import Transaction as trans

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
	def __init__(self,vid,title,dat):
		self.sk,self.pk = util.generateKeyPair()								#Generates a key pair for every voter
		self.voterID = vid  													#voterID links to database
		self.name = title
		self.dob = dat
		self.balance = True

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


	def sendSk(self):
		return (self.sk.to_string())



if __name__=="__main__":
	v1 = Voter(6969,"Akhil Singh","12-12-2012")
	p1 = Party(101,"BJP")
	v1.castVote(p1)
	print(v1)





