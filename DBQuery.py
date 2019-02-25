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


def verify(name,dob,v_id):         #The case of multiple same names and DOBs also handled via v_id now
	conn=create_connection()
	c=conn.cursor()

	a,b,d=dob.split('-')
	dob=dt.date(int(a),int(b),int(d))
	try:
		c.execute('SELECT * FROM verify WHERE name=? AND dob=?',(name,dob,))
		row=c.fetchall()
		for i in row:

			password,salt=i[0].split(':')
			flag=(password==hashlib.sha256(salt.encode() + str(v_id).encode()).hexdigest())
			if(flag==True):
				conn.commit()
				conn.close()
				return flag
			else:
				continue
		if(flag==False):
			conn.commit()
			conn.close()
			return False

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

	#print(verify("Shannon Reyes","2018-11-15","101"))
	
