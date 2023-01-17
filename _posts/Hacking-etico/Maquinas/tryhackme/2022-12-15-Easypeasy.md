---
title: THM - Easy Peasy
date: 2022-12-15 19:00:00 PM
categories: [Máquinas, TryHackMe]
tags: [nmap, gobuster, john]     # TAG names should always be lowercase
img_path: /assets/img/Maquinas/THM/Easy-Peasy
---

# Realización

Primero sacamos los puertos abiertos que tiene con:

```bash
nmap -p- -T5 -sS -Pn [IP]
```

![Untitled](p18.png)

Una vez sacado los puertos usaremos gobuster para hacer fuerza bruta y veremos los directorios.

```bash
gobuster dir -u [IP]/ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
```

Después de hacer fuerza bruta a la página encontraremos un directorio llamado hidden y si miramos en el buscador: [http://](http://10.10.128.173/)[IP]/hidden y miramos en su código fuente no encontraremos nada. 

![Untitled](p1.png)

Por tanto volveremos a hacer fuerza bruta, pero esta vez al directorio que encontramos antes

```bash
gobuster dir -u [http://](http://10.10.128.173/)[IP]/hidden/ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
```

Después de hacer fuerza bruta al directorio ‘hidden’ encontraremos whatever y dentro de ese directorio encontraremos un HIDDEN en el código de la página, por tanto intentaremos descifrarlo

![Untitled](p2.png)

![Untitled](p3.png)

Con este comando descifraremos el código con base64 y nos sacara la flag →  flag{f1rs7_fl4g}

```bash
echo "ZmxhZ3tmMXJzN19mbDRnfQ==" | base64 -d
```

Después de investigar todo lo anterior, nos iremos a la página de apache poniendo con su puerto → [http://[IP]:65524/](http://10.10.128.173:65524/) y buscaremos que hay en el código fuente.

![Untitled](p4.png)

Desde la pagina de apache buscaremos una flag aqui y si buscaomos por hidden encontraremos un hash. Una vez que lo encontremos averiguaremos qué tipo de hash es y lo descifraremos. En nuestro caso el hasht es de base 62, para ello buscaremos un descifrador de dicho hash y ya tendriamos otra flag.

![Untitled](p5.png)

![Untitled](p6.png)

Despues de sacar la flag del código fuente de apache, entraremos en el txt de robots.txt como vemos en la captura y encontraremos la flag:

![Untitled](p7.png)

Con el hash averiguaremos que tipo de hash tiene y lo descifraremos. En este caso el hash sería md5.

![Untitled](p8.png)

Después de haber sacado el hash de base 62, veremos que nos da una ruta, la cual utilizaremos. Entraremos en el buscador y entraremos en la ruta que nos dio.

![Untitled](p9.png)

![Untitled](p10.png)

Con el hash sacado anteriormente en la ruta “/n0th1ng3ls3m4tt3r”, sacaremos una contraseña. Para ello utilizaremos john para sacarla.

Primeramente meteremos el hash obtenido en un archivo llamado hash.txt, para después poder pasarle una lista descargada de TryHackMe y sacar la contraseña, la cual será otra flag.

![Untitled](p11.png)

A continuación, probaremos a ver si hay algun tipo de información en la imagen que vimos en la pagina de “/n0th1ng3ls3m4tt3r”. Para ello la descargaremos la imagen “binarycodepixabay.jpg”.

![Untitled](p12.png)

Para sacar la información usaremos el comando siguiente sobre la imagen descargada. Despues de poner el comando nos pedirá una contraseña, la contraseña que pondremos será la que hemos obtenido anteriormente “mypasswordforthatjob”. 

```bash
steghide --extract -sf binarycodepixabay.jpg
```

Al ejecutar el comando nos sacará un txt el cual abriremos y veremos información.

![Untitled](p13.png)

Lo que hemos obtenido del txt, es el usuario y una contraseña hasheada, que descodificaremos de binario a texto. Una vez descifrada ya tendriamos otra flag.

![Untitled](p14.png)

Con el usuario y contraseña sacada, podremos entrar en el SSH. Para entrar escribiremos el comando siguiente:

```bash
ssh -p 6498 boring@10.10.5.236
```

![Untitled](p15.png)

Una vez entremos en el SSH, veremos e investigaremos que hay. Como vemos en la captura encontramos la última flag cifrada.

![Untitled](p16.png)

Como podemos ver por el formato que tiene la flag, intuimos que está usando un cifrado de rotanción, en este caso ROT13. Para descifralo únicamente tendremos que buscar el descifrador de ROT13 y sacariamos la última flag.

![Untitled](p17.png)