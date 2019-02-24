# Accounts.py
# This file holds the different types of accounts which will be used to model the voters and parties
# Voter: vid(Voter ID) | 
#

import Utility as util

#class Party:

class Voter:
	def __init__(self,vid,title,dat):
		self.sk,self.pk = util.generateKeyPair()								#Generates a key pair for every voter
		self.voterID = vid  													#voterID links to database
		self.name = title
		self.dob = dat


	def castVote(self,party):
		if self.getBalance() != 1:												#if the voter doesnt have a vote to give
			print("Sorry! You don't have vote to cast!")
			raise Exception("NoBalance")
			return None
		else:

			pass




	def __repr__(self):
		return ( "Name: " + self.name + "\nVoter ID: " + str(self.voterID))

	def getBalance(self):
		pass

	def sendSk(self):
		return (self.sk.to_string())



if __name__=="__main__":
	v1 = Voter(6969,"Akhil Singh","12-12-2012")
	print(v1)





