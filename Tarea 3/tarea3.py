from Crypto import Random
from Crypto.Cipher import DES
import base64

#padding
def pad(data):
    length = 16 - (len(data) % 16)
    data = data.decode() + chr(length)*length
    return data.encode()

#encriptado
def encrypt(message, passphrase, IV):
    des = DES.new(passphrase, DES.MODE_OFB, IV)
    return base64.b64encode(IV + des.encrypt(pad(message)))

#Mensaje del usuario
message = input("Ingrese un mensaje: ")
message = message.encode()
key = ""
while len(key) != 8:
    key = input("Ingrese una llave (8 caracteres): ")
key = key.encode()
IV = ""
while len(IV) != 8:
    IV = input("Ingrese un IV (8 caracteres): ")
IV = IV.encode()
encrypted = encrypt(message, key, IV)

#HTML
string = """
<p>Este sitio contiene un mensaje secreto</p>
<div class="des-ofb" id='"""+encrypted.decode()+"""'></div>
<div class="key" id='"""+key.decode()+"""'></div>
<div class="decrypted" id="decrypted"></div>
"""

with open(r"tarea3.html", 'w') as html:
    html.write(string)
