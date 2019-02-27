#TransactionOutput.py
#Houses the class storing change details of each transaction

import Utility as util


class TxOutput:
    def __init__(self,publicKey,tranID):
        self.receptor = publicKey
        self.txid = tranID

    def isMine(self,publicKey):
        return (publicKey == self.receptor)





## TESTING...
if __name__ == "__main__":
    sk,pk = util.generateKeyPair()
    to1 = TxOutput(pk,101)
    print(to1.isMine(pk))