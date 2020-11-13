import socket
import threading
import os
from ECC import *
from tinyec import registry
import pickle
from time import sleep
import sqlite3
from sqlite3 import Error

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',50018))
s.listen(4)

privKey = secrets.randbelow(curve.field.n)
pubKey = privKey * curve.g
BUFF = 1024
conn = None

def writeFile(sock, filename):
	f = ""
	print("Descargando...")
	while True:
		data = sock.recv(BUFF)
		if len(data) < BUFF:
			f += data.decode()
			break
		f += data.decode()
		data = ""
	f = f.split()
	enc = []
	num = 0
	for i in f:
		if num == 3:
			enc.append(pickle.loads(bytes.fromhex(i)))
			break
		enc.append(bytes.fromhex(i))
		num += 1
	dec = decrypt_ECC(enc, privKey)
	file = open(filename, "w")
	file.write(dec.decode())
	file.close()
	sock.send(b"Archivo recibido")
	print(filename, "recibido")	
		
def saveFile(table, filename):
	
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	
	c.execute('''CREATE TABLE IF NOT EXISTS %s
		(numero INTEGER PRIMARY KEY AUTOINCREMENT, texto TEXT);''' %table)

	f = open(filename, 'r')

	for i in f:
		c.execute("INSERT INTO %s(texto) VALUES (?) ;" % table, (i,))

	conn.commit()
	f.close()
	conn.close()

def run(sock, addr):
	print ("Cliente conectado")
	sock.send(pickle.dumps(pubKey))
	writeFile(sock, "dec1.txt")
	sleep(1)
	writeFile(sock, "dec2.txt")
	sleep(1)
	writeFile(sock, "dec3.txt")
	sleep(1)
	writeFile(sock, "dec4.txt")
	sleep(1)
	writeFile(sock, "dec5.txt")

	print("Guardando en base de datos...")
	saveFile("tabla1", "dec1.txt")
	saveFile("tabla2", "dec2.txt")
	saveFile("tabla3", "dec3.txt")
	saveFile("tabla4", "dec4.txt")
	saveFile("tabla5", "dec5.txt")
	print("Guardado con exito")

	sock.close()

print('~Server iniciado~')
while True:
	sock, addr = s.accept()
	t = threading.Thread(target = run, args = (sock, addr))
	t.start()
		
s.close()
