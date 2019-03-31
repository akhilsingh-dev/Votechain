import Transaction as Tx
import TransactionOutput as TxOut
import Utility as util
import DBQuery as dbq
import Accounts as ac
import DBCreate as dbc
import Blockchain as Bch
import Block
import threading
import sys 



x=40


print("THIS SESSION WILL BE OF",x,"MINUTES")

VoterList=dbc.create_Accounts()
session=1
bjp = ac.Party(103,"BJP")
inc = ac.Party(101,"INC")
partyList = [bjp,inc]
season = Bch.Blockchain(4)
txStack = []



def ask_choice(partyList):
	print("Choose which party to vote for: ")
	for i in range(len(partyList)):
		print(str(i+1) + ". " + partyList[i].name)
	choice = int(input("Enter the number to vote: "))
	return (choice-1)



def session_breaker():
	global session



	session=0
	sys.stdout.flush()
	if(len(txStack)%2==1):
		sk,pk = util.generateKeyPair()
		dummy = ac.Voter("Lorem Ipsum","1000-10-10",pk.to_string())
		dummy.sk = sk.to_string()
		pty = ac.Party(0,"dummy party")
		empTx = Tx.Transaction(dummy,pty)
		empTx.is_proc=True
		empTx.txoutput = TxOut.TxOutput(pty,empTx.txid) 
		txStack.append(empTx)
		tempbl = Block.Block(txStack[-2:len(txStack):1])
		season.addBlock(tempbl)

    #for i in VoterList:
    #	del(i)
	print("\nALL RECORDS DELETED")
	print("\t\tRESULTS:\n")

	for party in partyList:
		print(party.name + " : " + str(party.countVotes(season)))
	sys.exit()
	


if __name__ == '__main__':
  
	timer = threading.Timer(x*60, session_breaker) 							
	timer.start()                                                    #timer started
	#print("Exit\n") 

	while(session==1):															#if a new voter comes...
		try:
			name=input("Enter your name: ")	
			if(session!=0):										#Get his name and DoB
				dob=input("Enter your DoB in yyyy-mm-dd format: ")
			[boo,vtr]=dbq.verifyaccount(VoterList,name,dob)						#get the index of voter in the list
			if(boo==True):															#if the voter is available in list...
				if(dbq.verifyDB(vtr)):									#...and if he is verified with the database...PublicKey are now in scope 
					vtr.sk_QRCode()									#Get the users QR Code...this gets the SecretKey in scope
					choice = ask_choice(partyList)									#Ask user for choice of party
					temp = vtr.castVote(partyList[choice])				#create a transaction by casting the vote
					if(temp!=None):													#if all goes well...a new Tx gets generated
						txStack.append(temp)										#append it to the stack

				if(len(txStack) % 2 == 0):												#if transaction stack becomes full...
					tempbl = Block.Block(txStack[-2:len(txStack):1])					#Add the stack to the block
					season.addBlock(tempbl)											#and add the block into the chain
					

			else:
				if(session!=0):
					print("Sorry! you are not registered for this voting Season!")
		except:
			if(session!=0):
				print("\ninvalid credentials!!")
				continue
			else:
				sys.exit()
				
		
		


	


