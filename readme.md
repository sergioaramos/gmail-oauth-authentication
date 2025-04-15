# Generador de Tokens OAuth 2.0 para Google APIs

Este proyecto proporciona una herramienta simple para generar tokens OAuth 2.0 necesarios para autenticarse con las APIs de Google, específicamente con Gmail API.

## 📋 Descripción

La herramienta automatiza el proceso de autenticación OAuth 2.0 con Google, generando y refrescando tokens de acceso. El script `generate_token.py` maneja todo el flujo de autenticación y almacena los tokens generados en un archivo `.env` para su fácil acceso en otras aplicaciones.

## ✨ Características

- Generación automatizada de tokens OAuth 2.0
- Almacenamiento seguro de credenciales en archivo `.env`
- Soporte para múltiples scopes de Google API
- Flujo de autenticación con servidor local
- Actualización automática de tokens existentes

## 🔧 Requisitos

- Python 3.6 o superior
- Acceso a Internet
- Cuenta de Google y proyecto en Google Cloud Platform

## 📦 Dependencias

```
dotenv
google_auth_oauthlib
```

## 🚀 Instalación

1. Clona este repositorio o descarga los archivos

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Crea un archivo `.env` con tus credenciales de Google Cloud:
   ```
   GOOGLE_CLIENT_ID=tu-client-id
   GOOGLE_CLIENT_SECRET=tu-client-secret
   GOOGLE_SCOPES=[
       'https://www.googleapis.com/auth/gmail.readonly',
       'https://www.googleapis.com/auth/gmail.modify',
       'https://www.googleapis.com/auth/gmail.send'
   ]
   ```

## 💻 Uso

Ejecuta el script principal:

```bash
python generate_token.py
```

El script:
1. Abrirá una ventana de navegador para autenticarte con Google
2. Solicitará permisos según los scopes configurados
3. Generará los tokens y los almacenará en el archivo `.env`

## ⚙️ Configuración

Puedes modificar los scopes en el archivo `.env` según las APIs de Google que necesites utilizar. Los scopes actuales están configurados para Gmail API.

## 🔐 Seguridad

- Los tokens generados se almacenan localmente en el archivo `.env`
- El archivo `.env` está incluido en `.gitignore` para evitar su publicación accidental
- Nunca compartas tus tokens o credenciales de cliente

## 📝 Notas

- Los tokens de acceso tienen un tiempo de expiración (generalmente 1 hora)
- El script utiliza el refresh token para obtener nuevos tokens de acceso cuando sea necesario

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes mejoras, no dudes en abrir un issue o enviar un pull request.