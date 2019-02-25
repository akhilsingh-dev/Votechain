# DBQuery.py
# Houses connections to database to query a voter's details from database


import hashlib
import uuid
import datetime as dt
import sqlite3
from sqlite3 import Error
import os
import Utility as util



def create_connection():
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect("pythonsqlite.db")
    except Error as e:
        print(e)
        return
    finally:
        return conn

def getpublicKey(name,dob):
	conn=create_connection()
	c=conn.cursor()
	print(dob)
	a,b,d=dob.split('-')
	dob=dt.date(int(a),int(b),int(d))
	try:
		c.execute('SELECT * FROM verify WHERE name=? AND dob=?',(name,dob,))
		row=c.fetchone()
		dx = row[3]
		conn.commit()
		conn.close()
		return dx
	except (RuntimeError,NameError,TypeError):
		conn.commit()
		conn.close()
		print("Public key missing!")
		return None


def verify(name,dob,v_id):
	conn=create_connection()
	c=conn.cursor()

	a,b,d=dob.split('-')
	dob=dt.date(int(a),int(b),int(d))
	try:
		c.execute('SELECT * FROM verify WHERE name=? AND dob=?',(name,dob,))
		row=c.fetchone()
		password,salt=row[0].split(':')
		conn.commit()
		conn.close()
		return (password==hashlib.sha256(salt.encode() + str(v_id).encode()).hexdigest())

	except (RuntimeError,NameError,TypeError):
		conn.commit()
		conn.close()
		return False


		

def deleteData(name,dob,v_id):
	conn=create_connection()
	c=conn.cursor()

	a,b,d=dob.split('-')
	dob=dt.date(int(a),int(b),int(d))
		
	try:
		c.execute('DELETE FROM verify WHERE name=? AND dob=?',(name,dob,))
		conn.commit()
		conn.close()
	except(RuntimeError,NameError,TypeError):
		conn.commit()
		conn.close()
		print("Data not found!")



##TESTING...

if __name__ == '__main__':

	privateKey = b"\xad\xd1\xdb\xe86\x07\xc4\x1b\x18\x9b\xaa\x98\x85v|U\xf8\xfa\xad \x11\xeb\x8a\x1f\x1d/\x13\xf5\xe86\xb1\xed"
	publicKey = getpublicKey("Polly Robertson","2018-11-12")
	data = "Hello World"
	sign = util.applySignature(privateKey,data)
	print(util.verifySignature(publicKey,"Hello World",sign))

