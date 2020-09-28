# BetBot

BetBot es un script que juega automáticamente a la ruleta con el método Martingala.
 
Hecho en python (3.7.0) con el webdriver selenium(3.141.0) para controlar Chrome(o cualquier navegador) y el módulo smtplib para mandar mails(cuando te quedas sin plata).

Probablemente ya no funcione pq la pagina cambia con regularidad, pero fue un proyecto divertido.

## Instalación

Paquetes necesarios con [pip](https://pypi.org/project/pip/) 

```bash
pip install selenium
pip install smtplib
```

## Uso

```bash
python main.py

>>mailSeLaCuenta@mail.com
>>contraseñaDeLaCuenta
```
