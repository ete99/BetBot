# BetBot

BetBot es un script que juega automáticamente a la ruleta en un casino online con el método Martingala.
 
Hecho en python (3.7.0) con el webdriver selenium(3.141.0) para controlar Chrome(o cualquier navegador) y el módulo smtplib para mandar mails(cuando te quedas sin plata).

Ningún dólar fue herido durante el uso de este programa, en su momento la página regalaba 1 dólar por crear una cuenta, después de varias cuentas llevadas a la bancarrota, con una llegue al mínimo para el checkout y resultó que necesitaba meter plata a la página para que me dejen quitar.

Probablemente ya no funcione el script pq la pagina cambia con regularidad, pero fue un proyecto divertido.

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
