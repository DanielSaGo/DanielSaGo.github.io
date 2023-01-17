---
marp: true
author: Grupo 4
theme: default
paginate: true
---

<style>
    :root {
        color: black;
        font-family: H;
        background: linear-gradient(0deg, rgba(0,121,255,1) 0%, rgba(255,255,255,1) 16%, rgba(255,255,255,1) 100%);

    }
    
    h1 {
        text-align: left;
        color: white
    }

    h2 {
        color: #333c87;
        text-align: center;
        font-weight: bold;
    }

    h3{
        text-align: left;
        color: black
    }

    h4{
        text-align: left;
        color: white
    }

</style>

#
#
#
#
# PROYECTO 1
# Estudio y evaluación de vulnerabilidades
#### Grupo 4

![bg ](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/278197/course/overviewfiles/photo1663748241.jpg)

---
[comment]: <> (Comienzo de la Parte  1)

## ¿Qué es una inyección SQL?

Es una vulnerabilidad que permite al atacante insertar sentencias SQL de forma maliciosa para la manipulación de bases de datos, pudiendo así obtener y divulgar información.

![bg right w:500](https://nullsector.co/wp-content/uploads/2018/01/sqlinjection2.png)

--- 

## Pasos para prevenir y mitigar ataques de inyección SQL.

- Usar declaraciones prediseñadas o consultas parametrizadas.
- Validar la entrada del usuario.
- Mostrar mensajes de error genéricos.
- Limitar los privilegios del administrador de la BBDD.

![bg left w:400](https://cdn-icons-png.flaticon.com/512/564/564631.png)

---

## Medidas de monitorización.

- Herramientas de empresas especializadas.
- SQLiHelper 2.7 SQL Injection.
- Pangolin.
- SQLMap.

![bg right w:450](https://static.vecteezy.com/system/resources/previews/001/923/518/non_2x/laptop-computer-with-magnifying-glass-isolated-icon-free-vector.jpg)

---

## EJEMPLO

**Fecha de Publicación:** 07/10/2022
**Importancia:** 5 (Crítica)
**Recursos afectados:** Versiones anteriores a la versión 9.5.9 o 10.0.3.
**Descripción:** En versiones anteriores a las nombradas, se podía inyectar comandos SQL o realizar una ejecuón remota de comandos.

**Solución 1:** Actualizar a las versiones 9.5.9 o 10.0.3


![bg right w:450](https://tic.gal/wp-content/uploads/2017/11/PictoGlpi.png)

---
## Solución 2:

**Pasos Previos:**
- Hacer un backup de la base de datos
- Hacer una copia del directorio de configuración para obtener el archivo con la clave de GLPI
- Hacer un backup de los directorios de archivos (usuarios, plugins, documentos subidos)
- Hacer una copia de los directorios Marketplace y Plugins.

---

## Pasos para actualizar GLPI
- Descargar la última versión de GLPI
- Asegurarse de que el directorio donde vamos a instalar la nueva versión está vacío y extraer los archivos.
- Restaurar los archivos a los que hemos hecho copia previamente
- Abrir GLPI en la consola de php e insertar el comando db:update para que los datos del backup se integren en la base de datos.

---

## A tener en cuenta

- No se podrá usar la aplicación hasta que el proceso de actualización haya terminado

- No se puede restaurar la copia de seguridad de la base de datos en una base de datos que no esté vacía.

- Si da error al restaurar la base de datos, vaciar la misma y volver a ejecutar la copia del backup.

- El proceso de actualización desactiva los plugins, por lo que habrá que volver a activarlos.

---

[comment]: <> (Comienzo de la Parte 2)

## Los 10 tipos de ciberataques más importantes según OWASP

![bg left:50% w:400](https://evalian.co.uk/wp-content/uploads/2022/04/OWASP-Top-10-Evalian-768x755.png)

---

## Pérdida de control de acceso

### Vulnerabilidades
- Viola el principio de privilegio mínimo.
- Eludir comprobaciones de control de acceso modificando la URL.
- Acceder a APIs sin controles de acceso para los métodos POST, PUT y DELETE.

### Medidas preventivas
- Implmentar mecanismos de control de acceso.
- No permitir al usuario que pueda crear, leer, actualizar o eliminar cualquier dato.
- Tokens JWT con una corta duración.

---

## Exposición de datos sensibles

### Vulnerabilidades
- Falta de directivas de seguridad en los encabezados HTTP.
- Certificado del servidor y cadena de confianza que no se encuentren debidamente validados.

### Medidas preventivas
- Categorizar los datos procesados, almacenados o transmitidos por la aplicación.
- Cifrar todos los datos confidenciales en reposo.
- Asegurarse que los algoritmos y protocolos utilizan estandares estables y actualizados

---

## Inyecciones

### Vulnerabilidades
- Los datos proporcionados por el usuario no son validados, filtrados o sanitizados
- Acepta consultas dinámicas o no parametrizadas.
- Extracción de información de BBDD.

### Medidas preventivas
- Utilizar LIMIT y otros controles SQL para evitar la fuga de información.
- Implementar validaciones de entradas de datos en el servidor.
- Utilizar una API segura para evitar el uso de un intérprete.

---

## Diseño inseguro

### Vulnerabilidades
- No desarrollar una aplicación web desde su diseño incluyendo la seguridad de la misma.

### Medidas preventivas
- Establecer y utilizar un ciclo de desarrollo seguro apoyado en Profesionales en Seguridad de Aplicaciones para evaluar y diseñar la seguridad.
- Establecer y usar un catálogo de patrones de diseño seguros.
- Integrar verificaciones de viabilidad en cada capa de su aplicación.


---

## Configuración de seguridad incorrecta

### Vulnerabilidades
- Funciones innecesarias habilitadas.
- Cuentas y contraseñas predeterminadas.
- Software desactualizado.

### Medidas preventivas
- Implementar proceso de hardenind repetible.
- Eliminar o no instalar características no utilizadas.
- Aplicar un proceso automatizado para verificar la efectividad de las configuraciones.

---

## Componentes vulnerables y desactualizados

### Vulnerabilidades
- Utilizar un software vulnerable, sin soporte o no actualizado.
- No asegurar las configuraciones de los componentes.
- No testeando la compatibilidad de las bibliotecas actualizadas o parcheadas.

### Medidas preventivas
- Realizar un inventario continuo de las versiones de todos los componentes
- Consultar frecuentemente fuentes como CVE o NDV para detectar vulnerabilidades en los componentes. 


---

## Fallas de identificación y autenticación

### Vulnerabilidades
- Acceso de credenciales donde el atacante posea usuario-contraseña para acceder al sistema.
- Guardar contraseñas con cifrado débil o en texto plano.
- Contraseñas poco seguras, débiles o por defecto.

### Medidas preventivas
- Implementar la autenticaciñon multifactor para mayor dificultad de acceso.
- Implementar un control contra contraseñas débiles.
- Limitar o incrementar el tiempo de espera entre intentos fallidos.

---

## Fallas en software e integridad de datos

### Vulnerabilidades
- No tener una firma digital para autentificar que la integridad de los datos es la correcta.
- Cualquier ciberataque externo como fraude de identidad y los ataques de ransomware.
- Hardware comprometido, como una falla de disco y perdiendo dicha información.

### Medidas preventivas
- Utilizar firmas digitales o mecanismos similares para verificar la integridad de los datos.
- Usar herramienta de análisis de vulnerabilidades
- Tener un gestos de creación de copias de seguridad de los datos.

---

## Fallas en el registro y monitoreo

### Vulnerabilidades
- Inicios de sesión, fallas en el inicio de sesión y eventos no registrados o autorizados.
- Monitoreo de un atacanet a la red.

### Medidas preventivas
- Establecer en los datos controles de integridad para evitar la modificación o borrado.
- Establecer o adoptar un plan de respuesta y recuperación.
- Asegurarse que todos los errores de entradas de datos se registren correctamente.

---

## Falsificación de solicitudes del lado del servidor SSRF

### Vulnerabilidades
- Permite al atacante que la aplicación manda una solicitud falsa a un destino inesperado, incluso si este esta protegido por un firewall, VPN u ACL. 

### Medidas preventivas
- Desde la capa de red: Segmentar la funcionalidad de acceso a recursos remotos en redes separadas para reducir el impacto.
- Desde la capa de aplicación: Sanitizar y validar los datos de entrada. Deshabilitar redirecciones HTTP y evitar respuestas en formato "crudo" a los clientes.

---






[comment]: <> (Comienzo de la Parte  3)

## ¿Cuáles son las fases de un ciberataque?

![bg right w:350](https://www.incibe-cert.es/sites/default/files/blog/CyberKillChain/fases.png)

---

## Fase de Reconocimiento

Esta es la etapa en la que los ciberdelincuentes recopilan información sobre sus objetivos. Para ello, monitorea información sobre los detalles públicos de la organización y busca información sobre la tecnología utilizada, así como datos en redes sociales e incluso interacciones a través de correo electrónico.

![bg right w:400](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNx1i5-w37hYkznrT0gYuOnuilJ7zoMlE0sg&usqp=CAU)

---
## Herramienta de Reconocimiento

El atacante realiza una recopilación de datos sobre el comportamiento de la empresa y sus trabajadores, también usa scanners con los cuales puede hacerse una idea de los sistemas y programas que se utilizan. Los datos de la empresa y trabajadores generan, esto incluye redes sociales. está muy relacionados con todo lo que publicamos en Internet.

![bg left w:400](https://cdn.icon-icons.com/icons2/1111/PNG/512/loupe_79257.png)

---
## Fase de Preparación

En esta etapa, el ataque se prepara específicamente para el objetivo. Por ejemplo, un atacante puede crear un documento PDF o de Microsoft Office e incluirlo en un correo electrónico, haciéndose pasar por una persona legítima con la que la empresa suele hacer negocios.

![bg right w:400](https://cdn-icons-png.flaticon.com/512/2644/2644352.png)

---
## Fase de Distribución
En esta fase, por ejemplo, ocurre abriendo documentos infectados enviados por correo electrónico, accediendo a un phishing, etc. Ser conscientes de este tipo de ataques y aprender a reconocerlos será nuestra primera opción de defensa.

![bg right w:550](https://www.creativefabrica.com/wp-content/uploads/2021/05/26/Mail-phishing-icon-simple-style-Graphics-12525333-1.jpg)

---
## Herramienta de Distribución 

ZPHISHER: Es una herramienta que permite suplantar páginas web y obtener de forma ilícita correos, contraseñas y direcciones ip de los usuarios que caigan en este ataque.

![bg left w:400](https://securetechware.com/wp-content/uploads/2020/08/zphisher1.png)

---
## Fase de Explotación

Consiste en "detonar" el ataque, comprometiendo el ordenador infectado y la red a la que pertenece. Esto generalmente se debe a la explotación de vulnerabilidades conocidas que ya tienen parches de seguridad, como la vulnerabilidad de Escritorio remoto, que, si no se corrige, permitiría el acceso externo a su computadora.

![bg right w:500](https://static.vecteezy.com/system/resources/previews/006/842/158/non_2x/cybersecurity-vulnerability-black-glyph-icon-system-weakness-and-flaw-cybercriminal-gains-access-errors-exploitation-silhouette-symbol-on-white-space-isolated-illustration-free-vector.jpg)

---
## Herramienta de Explotación

RAT: Es un troyano de acceso remoto, que incluye una puerta trasera para el control administrativo del ordenador de destino. Generalmente se descargan de manera invisible con un programa solicitado por el usuario, juego o archivo adjunto de email. 

![bg left w:400](https://cdn-icons-png.flaticon.com/512/1995/1995646.png)

---
## Fase de Instalación

Es la etapa en la que el atacante instala el malware a la víctima. También puede haber situaciones en las que no se requiera la instalación, como el robo de credenciales.
 
![bg right w:400](https://cdn-icons-png.flaticon.com/512/2687/2687521.png)

---
## Herramienta de Instalación

ICEPACK realiza todo el proceso de infección y distribución sin necesidad de la intervención inicial de un hacker que manipule páginas web. Dicha herramienta apareció debido a la demanda de la venta de este tipo de software. 

![bg left w:400](https://thumbs.dreamstime.com/b/l%C3%ADnea-icono-del-vector-de-malware-114919577.jpg)

---
## Fase de Comando y control

En este punto, el atacante toma el control del sistema de la víctima, donde puede realizar o iniciar acciones maliciosas desde un servidor central llamado C&C (Command and Control), donde es capaz de robar credenciales, tomar capturas de pantalla, obtener archivos confidenciales, instalar otros programas, conocer cómo es la red del usuario y más.

![bg right w:400](https://cdn-icons-png.flaticon.com/512/6625/6625954.png)

---

## Herramienta de Comando y control

ALCHIMIST C2: Puede generar una carga útil configurada, establecer sesiones remotas, implementar la carga útil en las máquinas remotas, ejecutar la terminal, obtener tamaños de archivo, información del sistema operativo. Otas como: ejecutar comandos arbitrarios a través de cmd[.]exe., actualizar el implante Insectkt actual.

![bg left w:400](https://cdn2.iconfinder.com/data/icons/internet-security-set-2-1/64/x-06-512.png)

---
## Fase de Acciones sobre los objetos

 Esta es la etapa final en la que los atacantes pueden obtener datos e intentar extender su comportamiento malicioso a múltiples objetivos. Esta se produce cuando los atacantes han alcanzado su objetivo y se plantean cuál será su siguiente meta atacando a otro individuo y empezando otra vez el ciclo. 

![bg right w:400](https://cdn.icon-icons.com/icons2/390/PNG/512/cycle_38373.png)