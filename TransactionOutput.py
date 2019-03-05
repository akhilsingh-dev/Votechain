#TransactionOutput.py
#Houses the class storing change details of each transaction

import Utility as util


class TxOutput:
    def __init__(self,party,tranID):
        self.receptor = party
        self.txid = tranID

    def isMine(self,publicKey):
        return (publicKey == self.receptor.pk)

    def __repr__(self):
    	return ("="*60+"\n<TxOut> : At the end of this transaction, " + self.receptor.name + " Got a vote\n"+"="*60)



## TESTING...
if __name__ == "__main__":
    sk,pk = util.generateKeyPair()
    to1 = TxOutput(pk,101)
    print(to1.isMine(pk))