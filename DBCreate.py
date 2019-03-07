import hashlib
import uuid
import datetime 
import sqlite3
import time
import names
from sqlite3 import Error
import Accounts as acc
import Utility as util
import QRcodeGen as qrg


admin = "admin" 

def create_Accounts():              #creation of list of objects of all account in DB
    conn=create_connection()       #NOTE:voter-id not assigned from DB as it is hashed in DB and will be added in verifyDB() function in Accounts.py
    c=conn.cursor()
    VoterList=[]
    for i in range(1,21):
        c.execute('SELECT * FROM verify WHERE rowid=?',(i,))
        row=c.fetchone()
        VoterList.append(acc.Voter(row[1],str(row[2]),row[3]))
    return VoterList

def new_entry(c,conn):
    
    base = datetime.date.today()
    for _ in range(101,121):                       #creation of 20 records 
        l=[]
        [sk,pk] = util.generateKeyPair()
        salt = uuid.uuid4().hex                    #salt to be hashed with v_id
        v_id=_
        l.append(str(v_id))
        name=names.get_full_name()
        l.append(name)
        dob=base - datetime.timedelta(days=_)
        l.append(str(dob))
        l.append(sk.to_string())
        with open('test_case.txt', 'a') as f:            #name,dob,v_id,privatekey written in test_case.txt for future references and usage
            for item in l:
                f.write("%s\n" % item)
        hashed=hashlib.sha256(salt.encode() + str(v_id).encode()).hexdigest() + ':' + salt      #name,dob,hashed(v_id),publickey stored in DB
        c.execute('INSERT INTO verify(id,name,dob,public_key) VALUES(?,?,?,?)',(hashed,name,dob,pk.to_string(),))
        c.execute('INSERT INTO secretKey(private_key) VALUES(?)',(sk.to_string(),))
        qrg.qr_gen(str(v_id),str(v_id-100))

        
    f.close()
    conn.commit()
    return _

def create_connection():
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect("pythonsqlite.db")
    except Error as e:
        print(e)
        return
    finally:
        return conn


if __name__ == '__main__':
    conn=create_connection()
    c=conn.cursor()
    salt = uuid.uuid4().hex
    entry=input("Enter admin passcode to create records ")
    if(entry==admin):
        x=new_entry(c,conn)
        print("Insertion of ",x-100," elements to database successful")
    else:
        print("Wrong passcode")
    conn.close()
    time.sleep(5)


    
