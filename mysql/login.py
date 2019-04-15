import mysql.connector as con
import sys

global mydb

def luoUser(mydb):
	print("#"*25)
	luoja = mydb.cursor()
	userName = input("Nimi:")
	passwordi = input("Salasana:")
	sql = "INSERT INTO users (username, pass) VALUES (%s,%s)"
	values = (userName, passwordi)
	luoja.execute(sql, values)
	mydb.commit()


def connectMysql():
	mydb = con.connect(host="127.0.0.1", user="**", passwd="**", database="my_db")
	return mydb

def clears():
	for i in range(25):
		print("\n\n\n\n")


def loginLoop(mydb):
	while (1):
		clears()
		print("#"*25)
		print("[0] - Luo käyttäjä")
		print("[1] - Login")
		print("[2] - UnsafeLogin")
		print("[3] - Exit")
		valinta = input("")
		if valinta == '0':
			luoUser(mydb)
		if valinta == '1':
			safeLogin(mydb)
		if valinta == '2':
			unSafeLogin(mydb)
		if valinta == '3':
			break
		else:
			continue
	print("Kiitos käynnistä.\n")
	mydb.close()

def unSafeLogin(mydb):
	while(1):
		res = []
		clears()
		print("#"*25)
		user = input("Anna käyttäjänimi:")
		password = input("\nAnna salasana:")
		kursori = mydb.cursor()
		sql = "SELECT username FROM users WHERE username='" + user + "' AND pass='" + password + "'"
		try:
			kursori.execute(sql)
		except:
			input("login failed")
			continue
		res = kursori.fetchall()
		if len(res) < 1:
			print("login failed")
			input("")
			continue
		else:
			print("login success as")
			for r in res:
				print(r[0])
			input("")
		break



def safeLogin(mydb):
	while(1):
		res = []
		clears()
		print("#"*25)
		user = input("Anna käyttäjänimi:")
		password = input("\nAnna salasana:")
		kursori = mydb.cursor()
		sql = "SELECT username FROM users WHERE username=%s AND pass=%s"
		values = (user, password)
		kursori.execute(sql, values)
		res = kursori.fetchall()
		if len(res) < 1:
			print("login failed")
			input("")
			break
		else:
			print("login success as")
			for r in res:
				print(r[0])
			input("")
		break



def main():
	mydb = connectMysql()
	loginLoop(mydb)


if __name__ == '__main__':
	main()
