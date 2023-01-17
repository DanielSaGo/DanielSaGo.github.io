---
title: THM - CowBoyHacker
date: 2023-1-10 19:00:00 PM
categories: [Máquinas, TryHackMe]
tags: [nmap, ftp, ssh, hydra]    # TAG names should always be lowercase
img_path: /assets/img/Maquinas/THM/CowBoyHacker
---

# Realización

Primeramente escaneamos los primeros 100 puertos que tiene la maquina para ir con mayor velocidad y en segundo plano, escaneamos los demás puertos de la maquina.

![Untitled](p.png)

![Untitled](p1.png)

Después de esperar a que el primer comando termine podremos ver que nos saca los mismos puertos que el segundo comando.

Después de detectar los puerto de la maquina, lanzaremos el script de búsqueda de vulnerabilidades a los puertos. Como podemos ver en la captura, el puerto de ftp tiene vulnerabilidades:

```jsx
nmap -A -sV 10.10.46.19
```

![Untitled](p2.png)

Es posible acceder al puerto ftp anónimamente, vamos a probarlo:

![Untitled](p3.png)

Descargaremos los archivos encontrados y los abriremos y veremos su contenido.

![Untitled](p4.png)

A continuación veremos el contenido de los dos archivos:

![Untitled](p5.png)

![Untitled](p6.png)

Después de sacar la lista de contraseñas, probaremos a entrar con fuerza bruta a ssh, con el usuario “X”, que sacamos en el txt “task.txt”

![Untitled](p7.png)

Accedemos a ssh con este usuario y contraseña y hacemos un ls para ver que nos da. Ya habríamos sacado la flag.

![Untitled](p8.png)

Primero miraremos las aplicaciones que tienen permisos de administrador que tiene el usuario "x".

![Untitled](p9.png)

Vemos que podemos ejecutar tar como administrador

Nos vamos al navegador y buscamos la pagina gtfobins, para coger el comando de escalada de privilegios, buscamos tar en el buscador y copiaremos el comando que nos sale.

![Untitled](p10.png)

Una vez ejecutado el comando vemos que tenemos acceso como root, nos vamos a su carpeta principal y vemos el archivo que hay en esta:

![Untitled](p11.png)

Realizado por:

[@danielsago](https://github.com/DanielSaGo)

[@mariadgt](https://github.com/mariadgt)