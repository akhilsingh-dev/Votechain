import hashlib
import uuid
import datetime 
import sqlite3
import time
import names
from sqlite3 import Error
import Utility as util

admin = "admin" 
    
def new_entry(c,conn):
    #name=input("Enter name ")
    #v_id=input("Enter voter-id ")
    #hashed=hashlib.sha256(salt.encode() + v_id.encode()).hexdigest() + ':' + salt
    #dob=input("Enter date of birth in yyyy/mm/dd format ")
    #y,m,d=dob.split('/')
    #x=datetime.date(int(y),int(m),int(d))
    #date_list = [base - datetime.timedelta(days=x) for x in range(0, 5)]
    base = datetime.date.today()
    for _ in range(101,121):
        l=[]
        [sk,pk] = util.generateKeyPair()
        salt = uuid.uuid4().hex
        v_id=_
        l.append(str(v_id))
        name=names.get_full_name()
        l.append(name)
        dob=base - datetime.timedelta(days=_)
        l.append(str(dob))
        l.append(sk.to_string())
        with open('test_case.txt', 'a') as f:
            for item in l:
                f.write("%s\n" % item)
        hashed=hashlib.sha256(salt.encode() + str(v_id).encode()).hexdigest() + ':' + salt
        c.execute('INSERT INTO verify(id,name,dob,public_key) VALUES(?,?,?,?)',(hashed,name,dob,pk.to_string(),))
        
    f.close()
    conn.commit()
    return _

def create_connection():
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect("pythonsqlite.db")
        print(sqlite3.version)
    except Error as e:
        print(e)
        return
    finally:
        return conn


if __name__ == '__main__':
    conn=create_connection()
    c=conn.cursor()
    salt = uuid.uuid4().hex
    entry=input("Enter admin to create records ")
    if(entry==admin):
        x=new_entry(c,conn)
        print("Insertion of ",x-100," elements to database successful")
    else:
        print("nah nigga")
    conn.close()
    time.sleep(5)

    
