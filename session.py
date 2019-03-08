import Transaction as Tx
import TransactionOutput as TxOut
import Utility as util
import DBQuery as dbq
import Accounts as ac
import DBCreate as dbc
import Blockchain as Bch
import Block
import threading 

VoterList=dbc.create_Accounts()
session=1

def ask_choice(partyList):
	print("Choose which party to vote for: ")
	for i in range(len(partyList)):
		print(str(i) + ". " + partyList[i].name)
	choice = int(input("Enter the number to vote: "))
	return (choice-1)



def session_breaker():
	global session
	global VoterList
	
	session=0
    #for i in VoterList:
    #	del(i)
	print("\nALL RECORDS DELETED")

if __name__ == '__main__':
  
	timer = threading.Timer(100.0, session_breaker) 							
	timer.start()                                                    #timer started
	bjp = ac.Party(103,"BJP")
	inc = ac.Party(101,"INC")
	partyList = [bjp,inc]
	season = Bch.Blockchain(5)
	txStack = []										 						
	
	#print("Exit\n") 
	
	while(session==1):															#if a new voter comes...
		name=input("Enter your name: ")											#Get his name and DoB
		dob=input("Enter your DoB in yyyy-mm-dd format: ")
		[boo,vtr]=dbq.verifyaccount(VoterList,name,dob)						#get the index of voter in the list
		if(boo==True):															#if the voter is available in list...
			if(dbq.verifyDB(vtr)):									#...and if he is verified with the database...PublicKey are now in scope 
				vtr.sk_QRCode()									#Get the users QR Code...this gets the SecretKey in scope
				choice = ask_choice(partyList)									#Ask user for choice of party
				temp = vtr.castVote(partyList[choice])				#create a transaction by casting the vote
				if(temp!=None):													#if all goes well...a new Tx gets generated
					txStack.append(temp)										#append it to the stack

			if(len(txStack)==2):												#if transaction stack becomes full...
				tempbl = Block.Block(txStack)									#Add the stack to the block
				season.addBlock(tempbl)											#and add the block into the chain
				#txStack.pop()													#remove them from the stack
				#txStack.pop()

		else:
			print("Sorry! you are not registered for this voting Season!")
		
		session=int(input("Continue? (1/0): "))


	print("\t\tRESULTS:\n")
	for party in partyList:
		print(party.name + " : " + str(party.countVotes(season)))


