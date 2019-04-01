# DBQuery.py
# Houses connections to database to query a voter's details from database


import hashlib
import uuid
import datetime as dt
import sqlite3
from sqlite3 import Error
import os
import Utility as util
import QrCodes as qr
import Accounts as ac

def create_connection():
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect("pythonsqlite.db")
    except Error as e:
        print(e)
        return
    finally:
        return conn

def getprivateKey(rowid):
	conn=create_connection()
	c=conn.cursor()
	try:
		c.execute('SELECT * FROM secretKey WHERE rowid=?',(rowid,))
		row=c.fetchone()
		dx=row[0]
		conn.commit()
		conn.close()
		return dx
	except (RuntimeError,NameError,TypeError):
		conn.commit()
		conn.close()
		print("Private key missing!")
		return None

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

def verifyaccount(vt,name,dob):           #verifying voter from voterlist
	present=0
	for i in vt:
		flag1=(i.name==name)
		flag2=(i.dob==dob)
		if((flag1 and flag2)==True):
			present=1
			return [(flag1 and flag2),i]
		else:
			continue                          		#continues till voter not found in VoterList
	if(present==0):
		return [False,None]


def verifyDB(voter):                               #verifying from database and assigning value of self.voterID post verification
	vid=int(input("Enter your voter-id "))
	if(verify(voter.name,voter.dob,vid)):
		voter.voterID = vid
		return True
	else:
		print("Record not found in DB!")
		return False



def verify(name,dob,v_id):         #The case of multiple same names and DOBs also handled via v_id now
	conn=create_connection()
	c=conn.cursor()

	a,b,d=dob.split('-')					#UNCOMMENT IF RUNNING IN CONSOLE MODE!
	dob=dt.date(int(a),int(b),int(d))		#UNCOMMENT IF RUNNING IN CONSOLE MODE!
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
		c.execute('SELECT rowid FROM verify WHERE name=? AND dob=?',(name,dob,))
		row=c.fetchone()

		c.execute('DELETE FROM verify WHERE name=? AND dob=?',(name,dob,))
		c.execute('DELETE FROM secretKey WHERE rowid=?',(row[0],))
		conn.commit()
		conn.close()
	except(RuntimeError,NameError,TypeError):
		conn.commit()
		conn.close()
		print("Data not found!")



##TESTING...

if __name__ == '__main__':

	deleteData("Gail Branam","2018-11-26",101)