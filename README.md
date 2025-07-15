# 🛰️ ISS Overhead Email Notifier

Este proyecto en Python monitorea la ubicación de la Estación Espacial Internacional (ISS) y te envía un correo electrónico automáticamente cuando la ISS está cerca de tu ubicación **y es de noche**, para que puedas salir y verla pasar por el cielo. 🌌📬

---

## 🚀 ¿Qué hace?

- Consulta la API [Open Notify](http://api.open-notify.org/) para obtener la ubicación actual de la ISS.
- Verifica tu ubicación (latitud y longitud) y determina si la ISS está a ±5° de tu posición.
- Usa la API de [Sunrise Sunset](https://sunrise-sunset.org/api) para saber si es de noche.
- Si ambas condiciones se cumplen, **envía un correo automático** avisándote que la ISS está sobre ti.
- Repite la verificación **cada 60 segundos**.

---

## 📦 Tecnologías utilizadas

- Python 3
- `requests` – Para consumir APIs
- `datetime` – Para manejo de fechas
- `smtplib` – Para enviar correos
- `time` – Para control de espera (60 segundos entre verificaciones)

---

## 📄 Estructura del proyecto


---

## 🔧 Configuración

1. Asegúrate de tener Python 3 instalado.
2. Instala las dependencias (solo `requests`):

```bash
pip install requests
```

3. Modifica tu información en main.py:

MY_LAT = TU_LATITUD
MY_LONG = TU_LONGITUD
MY_EMAIL = "tu_correo@gmail.com"
PASSWORD = "tu_contraseña_o_app_password"

Usa una App Password si tienes la verificación en dos pasos en Gmail.
