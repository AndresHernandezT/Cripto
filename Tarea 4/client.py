import socket
import threading
import os
import pickle
from ECC import *
from time import sleep
from time import time
from hashlib import *
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1',50018))
BUFF = 1024

def hashing_txt(arc, new):
    f = open(arc, "r")
    out = open(new, "w")
    for i in f:
        x = sha3_512(i.encode()).hexdigest()
        out.write(x + "\n")
    f.close()
    out.close()

def sendFile(filename, enc):
        f = open(filename,"w")
        f.write(enc[0].hex() + "\n")
        f.write(enc[1].hex() + "\n")
        f.write(enc[2].hex() + "\n")
        f.write(pickle.dumps(enc[3]).hex())
        f.close()
        f = open(filename,"r")
        sock.send(f.read().encode())
        sock.send(b"")
        print("Subiendo...")
        print(sock.recv(BUFF).decode())
        f.close()
        print(filename, "enviado")
        sleep(1)

def sending():
        pubKey = pickle.loads(sock.recv(1024))
        
        f = open("hash1.txt","r")
        enc = encrypt_ECC(f.read().encode(), pubKey)
        f.close()
        sendFile("enc1.txt", enc)
        
        f = open("hash2.txt","r")
        enc = encrypt_ECC(f.read().encode(), pubKey)
        f.close()
        sendFile("enc2.txt", enc)        
        
        f = open("hash3.txt","r")
        enc = encrypt_ECC(f.read().encode(), pubKey)
        f.close()
        sendFile("enc3.txt", enc)
        
        f = open("hash4.txt","r")
        enc = encrypt_ECC(f.read().encode(), pubKey)
        f.close()
        sendFile("enc4.txt", enc)

        f = open("hash5.txt","r")
        enc = encrypt_ECC(f.read().encode(), pubKey)
        f.close()
        sendFile("enc5.txt", enc)

        print("ENDED")
        sock.close()

hashes = [
        "0 archivo_1", "10 archivo_2", "10 archivo_3", "1000 archivo_4", "1800 archivo_5"
        ]

files = [
    "archivo1.txt", "archivo2.txt", "archivo3.txt", "archivo4.txt", "archivo5.txt"
    ]
new_files = [
    "hash1.txt", "hash2.txt", "hash3.txt", "hash4.txt", "hash5.txt"
    ]
          
for i in range(0,5):
        start_time = time()
        cmd = "hashcat -O -m "+ hashes[i] +" diccionario_2.dict --potfile-disable"
        os.system(cmd)
        end_time = time() - start_time
        print("Tiempo de demora %0.10f segundos." % end_time)

for i in range(0, 5):
    cmd = "hashcat -O -m "+ hashes[i] +" diccionario_2.dict --show --outfile-format=2 >> " + files[i]
    os.system(cmd)

for i in range(0, 5):
    hashing_txt(files[i], new_files[i])

t1 = threading.Thread(target = sending)
t1.start()
