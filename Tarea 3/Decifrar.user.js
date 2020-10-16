// ==UserScript==
// @name         Decifrar
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        file:///C:/Users/Andres-Desune/Desktop/tarea3.html
// @grant        none
// @require      https://raw.githubusercontent.com/AndresHernandezT/Cripto/master/Tarea%203/components/core.js
// @require      https://raw.githubusercontent.com/AndresHernandezT/Cripto/master/Tarea%203/rollups/tripledes.js
// @require      https://raw.githubusercontent.com/AndresHernandezT/Cripto/master/Tarea%203/components/tripledes.js
// @require      https://raw.githubusercontent.com/AndresHernandezT/Cripto/master/Tarea%203/components/mode-ofb.js
// ==/UserScript==

(function() {
    'use strict';
    // se obtiene mensaje y llave de la pagina
    var mensaje = document.getElementsByClassName("des-ofb")[0].getAttribute("id");
    document.getElementsByClassName("des-ofb")[0].innerText = mensaje;
    var key = document.getElementsByClassName("key")[0].getAttribute("id");
    document.getElementsByClassName("key")[0].innerText = key;

    // se decodifica el texto cifrado que viene en Base 64
    var ciphertext = CryptoJS.enc.Base64.parse(mensaje);
    key = CryptoJS.enc.Utf8.parse(key);

    // separar el iv y el texto cifrado
    var iv = ciphertext.clone();
    iv.sigBytes = 8;
    iv.clamp();
    ciphertext.words.splice(0, 2);
    ciphertext.sigBytes -= 8;
    console.log(iv);

    // desencriptado
    var decrypted = CryptoJS.DES.decrypt({ciphertext: ciphertext}, key, {
      iv: iv,
      mode: CryptoJS.mode.OFB
    });

    // se muestra el mensaje oculto en pantalla
    var plaintext = document.getElementsByClassName("decrypted")[0]
    plaintext.innerText = decrypted.toString(CryptoJS.enc.Utf8);
})();