import hashlib
import uuid
import datetime as dt
import sqlite3
from sqlite3 import Error


def verify(name,dob,v_id):
	try:
		conn = sqlite3.connect("pythonsqlite.db")
    except Error as e:
		print(e)
	finally:
		c=conn.cursor()


	a,b,d=dob.split('-')
	dob=dt.date(int(a),int(b),int(d))
	try:
		c.execute('SELECT * FROM verify WHERE name=? AND dob=?',(name,dob,))
		row=c.fetchone()
		password,salt=row[0].split(':')
		return (password==hashlib.sha256(salt.encode() + str(v_id).encode()).hexdigest())

	except (RuntimeError,NameError,TypeError):
		return False
		

def deleteData(name,dob,v_id):
	try:
		conn = sqlite3.connect("pythonsqlite.db")
    except Error as e:
		print(e)
	finally:
		c=conn.cursor()
	a,b,d=dob.split('-')
	dob=dt.date(int(a),int(b),int(d))
		
	try:
		c.execute('DELETE FROM verify WHERE name=? AND dob=?',(name,dob,))
	except(RuntimeError,NameError,TypeError):
		print("Data not found!")



if __name__ == '__main__':
	print(verify("Polly Robertson","2018-11-12",104))


