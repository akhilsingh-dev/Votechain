# Blockchain.py
# This file houses the blockchain forming and validation logic 

import Block
import Transaction as Tx
import TransactionOutput as TxOut
import Utility as util
import DBQuery as dbq
import Accounts as ac


class Blockchain:

	def __init__(self,diff):
		print("\n\n[INFO] : Creating Blockchain...\n\n")
		self.blockchain = []							#create a list called blockchain filling it with transaction data
		genBlock = Block.Block([0,0])
		self.difficulty = diff
		self.blockchain.append(genBlock)				#initialize the chain with a block
		self.blockchain[0].link(0,self.difficulty)
		
		

	def addBlock(self, block):												#HASH IS NOT GETTING ASSIGNED
		
		block.link(self.blockchain[-1].hash, self.difficulty)				#link the last block's hash
		self.blockchain.append(block)										#append it to the list
				


	def validate(self):
		target = "0"*self.difficulty
		for i in range(1, len(self.blockchain), 1):
			prevblock = self.blockchain[i-1]
			currblock = self.blockchain[i]
			currblock.mineBlock(self.difficulty)						#remine a copy of the block
			
			for j in range(len(self.blockchain[i].tx)):
				if self.blockchain[i].tx[j].txoutput.receptor != self.blockchain[i].tx[j].recept:
					print("\n\n[ERROR] : Transaction output Mismatch!")
					return False
			

			if currblock.hash != self.blockchain[i].hash:				#check for data changes
				print("\n\n[ERROR] : Current Hash Mismatch!\n\n")
				return False
			
			if self.blockchain[i-1].hash != self.blockchain[i].previousHash:				#check for linkage errors
				print("\n\n[ERROR] : Chain linking Mismatch!\n\n")
				return False
			
			if target not in self.blockchain[i].hash:							#check if block is unmined
				print("\n\n[ERROR] : Block is not mined!\n\n")
				return False

			##FOLLOWING LINES ARE TO BE INCLUDED AFTER DESIGNING SIGNING LOGIC...
			for transac in currblock.tx:
				if not transac.is_proc:
					print("Transaction not processed")
					return False

		print("\n\n[INFO] : Blockchain is Valid!\n\n")
		return True



if __name__ == "__main__":
	session1 = Blockchain(4)						#init a session with difficulty 4
	
	v1 = ac.Voter("Nicole Okeeffe","2018-11-26",dbq.getpublicKey("Nicole Okeeffe","2018-11-26"))
	p1 = ac.Party(103,"BJP")
	v2 = ac.Voter("Kenneth Alvarado","2018-11-25",dbq.getpublicKey("Kenneth Alvarado","2018-11-25"))
	p2 = ac.Party(101,"INC")
	v3 = ac.Voter("Alex Scott","2018-11-24",dbq.getpublicKey("Alex Scott","2018-11-24"))
	v4 = ac.Voter("Isaac Carty","2018-11-23",dbq.getpublicKey("Isaac Carty","2018-11-23"))

	tr1 = Tx.Transaction(v1,p1)
	tr2 = Tx.Transaction(v2,p2)

	tr3 = Tx.Transaction(v3,p2)
	tr4 = Tx.Transaction(v4,p1)
	
	txQueue = [tr1,tr2]
	txQueue2 = [tr3,tr4]
	
	b1 = Block.Block(txQueue)					
	b2 = Block.Block(txQueue2)
	
	session1.addBlock(b1)				#calls link which sets prevhash and mines the block 
	
	session1.addBlock(b2)
	print("The chain validation is: " + str(session1.validate()))
	
	session1.blockchain[1].tx[0].recept = p2
	
	
	print("\n\nThe chain validation is: " + str(session1.validate()))
