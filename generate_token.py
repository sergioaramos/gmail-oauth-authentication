import os
from google_auth_oauthlib.flow import InstalledAppFlow
from dotenv import load_dotenv
import re

def generate_oauth_tokens():
    """
    Genera nuevos tokens OAuth 2.0 para Google APIs sin comillas en .env
    """
    print("=== Generando nuevos tokens OAuth 2.0 ===")
    
    # Definir scopes necesarios
    SCOPES = os.getenv("GOOGLE_SCOPES")
    
    # Cargar variables de entorno existentes
    load_dotenv()
    client_id = os.getenv("GOOGLE_CLIENT_ID")
    client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
    
    
    if not client_id or not client_secret:
        print("❌ Error: No se encontraron GOOGLE_CLIENT_ID y GOOGLE_CLIENT_SECRET en el archivo .env")
        return
    
    # Crear configuración del cliente
    client_config = {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"]
        }
    }
    
    try:
        # Crear el flujo OAuth
        flow = InstalledAppFlow.from_client_config(
            client_config, 
            SCOPES,
            redirect_uri="http://localhost:8090"
        )
        
        # Abrir navegador para autenticación
        flow.run_local_server(port=8090, prompt='consent')
        
        # Obtener credenciales
        credentials = flow.credentials
        
        # Actualizar el archivo .env manualmente sin comillas
        env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
        
        # Leer el contenido actual
        with open(env_path, 'r') as env_file:
            env_content = env_file.read()
        
        # Reemplazar o añadir variables sin comillas
        def update_env_var(content, var_name, new_value):
            # Busca si la variable ya existe
            pattern = re.compile(f'^{var_name}=.*$', re.MULTILINE)
            if pattern.search(content):
                # Actualiza la variable existente
                return pattern.sub(f'{var_name}={new_value}', content)
            else:
                # Añade la variable al final
                return content + f'\n{var_name}={new_value}'
        
        # Actualizar cada variable
        env_content = update_env_var(env_content, "GOOGLE_TOKEN", credentials.token)
        env_content = update_env_var(env_content, "GOOGLE_REFRESH_TOKEN", credentials.refresh_token)
        env_content = update_env_var(env_content, "GOOGLE_TOKEN_URI", credentials.token_uri)
        
        # Escribir el contenido actualizado
        with open(env_path, 'w') as env_file:
            env_file.write(env_content)
        
        print("\n✅ Tokens generados exitosamente y guardados en .env sin comillas")
        print(f"TOKEN: {credentials.token[:20]}...")
        print(f"REFRESH_TOKEN: {credentials.refresh_token[:20]}...")
        
    except Exception as e:
        print(f"❌ Error generando tokens: {str(e)}")

if __name__ == "__main__":
    # Verificar dependencias
    try:
        import google_auth_oauthlib
    except ImportError:
        print("Instalando dependencias necesarias...")
        os.system("pip install --upgrade google-auth-oauthlib python-dotenv")
    
    generate_oauth_tokens()