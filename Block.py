# Block.py
# This file defines a block of transactions for mining and adding to blockchain purposes

import Transaction as Tx
import TransactionOutput as TxOut
import Utility as util
import DBQuery as dbq
import Accounts as ac

class Block:
	def __init__(self,transactions):		#Transactions is a list of Tx
		self.tx = transactions
		self.previousHash = 0
		self.hash = 0
		self.nonce = 0

	def __repr__(self):
		return("\n\nBlock:\nPrevious Hash : " + str(self.previousHash) + "\nHash : " + str(self.hash)+"\n\n")



	def link(self,prevhash,diff):
		self.previousHash = prevhash

		self.hash = self.mineBlock(diff)			

	def calcHash(self,nonce):
		calculatedHash = util.applySHA256(str(self.tx[0]) + str(self.tx[1]) + str(self.previousHash) + str(nonce))
		return calculatedHash


	def mineBlock(self,difficulty):
		target = "0" * difficulty
		self.hash = self.calcHash(self.nonce)
		while target not in self.hash:
			self.nonce+=1
			self.hash = self.calcHash(self.nonce)
		
		print("Block mined at diffculty: "+ str(difficulty) +"\nHash = " + self.hash + "\n" )
		print("Nonce = "+str(self.nonce))
		return self.hash


if __name__ == "__main__":
	v1 = ac.Voter("Nicole Okeeffe","2018-11-26",dbq.getpublicKey("Nicole Okeeffe","2018-11-26"))
	p1 = ac.Party(103,"BJP")
	v2 = ac.Voter("Kenneth Alvarado","2018-11-25",dbq.getpublicKey("Kenneth Alvarado","2018-11-25"))
	p2 = ac.Party(101,"INC")
	tr1 = Tx.Transaction(v1,p1)
	tr2 = Tx.Transaction(v2,p1)
	txQueue = [tr1,tr2]
	diff = 5


	genBlock = Block([0,0])
	genBlock.link(0)
	print("\n\n")

	block1 = Block(txQueue)
	block1.link(genBlock.previousHash)
	print("\n\n")
	