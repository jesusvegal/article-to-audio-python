import requests  # Para realizar solicitudes HTTP y obtener contenido web.
from urllib.parse import urlparse  # Para analizar la URL.
from bs4 import BeautifulSoup  # Para analizar y extraer datos del HTML.
from gtts import gTTS  # Para convertir texto en audio.
import os  # Para ejecutar comandos del sistema operativo.
import re  # Para validar y trabajar con URLs.

# Función para validar una URL ingresada.
def is_valid_url(url):
    """
    Valida si una URL tiene un formato adecuado.
    """
    parsed = urlparse(url)
    # Comprobamos si el dominio y esquema están presentes en la URL.
    if not parsed.netloc or not parsed.scheme:
        return False

    # Expresión regular adicional para verificar la estructura completa de la URL.
    regex = re.compile(
        r'^(https?://)?'  # Soporta http y https.
        r'([a-zA-Z0-9.-]+)'  # Dominio.
        r'(\.[a-zA-Z]{2,6})'  # Extensión de dominio.
        r'(/[^\s]*)?$'  # Ruta opcional.
    )
    return bool(regex.match(url))

# Función para obtener el contenido HTML de un artículo desde una URL.
def fetch_article(url):
    """
    Envía una solicitud GET a la URL proporcionada y devuelve el contenido HTML.
    Maneja errores relacionados con solicitudes HTTP.
    """
    headers = {
        # Cabecera User-Agent para evitar bloqueos por parecer un bot.
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        # Realizamos la solicitud GET con las cabeceras definidas.
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanza un error si el código de estado no es exitoso (4xx, 5xx).
        return response.text  # Retornamos el contenido HTML.
    except requests.exceptions.HTTPError as http_err:
        print(f'Error HTTP: {http_err} para la URL: {url}')
    except requests.exceptions.RequestException as req_err:
        print(f'Error en la solicitud: {req_err} para la URL: {url}')
    return None  # Retornamos None si ocurre un error.

# Función para extraer todo el texto principal del contenido HTML.
def extract_text(html_content):
    """
    Extrae todo el texto del contenido HTML utilizando selectores flexibles.
    Limpia el texto extraído para mayor claridad.
    """
    try:
        # Creamos un objeto BeautifulSoup para analizar el HTML.
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Buscamos las estructuras comunes en las páginas web para asegurarnos de que capturamos todo el contenido.
        # Intentamos encontrar las etiquetas más relevantes para un artículo o contenido largo.
        paragraphs = soup.find_all('p')  # Extraemos todos los párrafos
        
        # Unimos el texto de cada párrafo en un solo bloque
        raw_text = ' '.join([para.get_text(separator=' ', strip=True) for para in paragraphs])
        cleaned_text = ' '.join(raw_text.split())  # Eliminamos espacios redundantes.
        return cleaned_text
    except Exception as e:
        print(f'Error al analizar el contenido HTML: {e}')
    return ''  # Retornamos una cadena vacía si no se puede extraer texto.

# Función para validar si el texto extraído es suficiente para convertirlo en audio.
def validate_text_length(text, min_length=50):
    """
    Verifica si el texto tiene al menos una longitud mínima.
    Devuelve True si es suficiente, de lo contrario False.
    """
    if len(text) < min_length:
        print(f'El texto extraído es demasiado corto ({len(text)} caracteres). No es adecuado para convertir en audio.')
        return False
    return True

# Función para convertir texto en un archivo de audio.
def text_to_speech(text, filename='output.mp3'):
    """
    Convierte el texto proporcionado en un archivo de audio utilizando gTTS.
    Guarda el archivo y lo reproduce.
    """
    try:
        tts = gTTS(text=text, lang='es')  # Configuramos el idioma a español.
        tts.save(filename)  # Guardamos el archivo de audio generado.
        print(f'Archivo de audio guardado como {filename}. Reproduciendo...')
        os.system(f'start {filename}')  # Reproducimos el archivo en Windows (ajustar para otros SO).
    except Exception as e:
        print(f'Error al convertir texto a audio: {e}')

# Función principal que coordina el flujo del programa.
def main():
    """
    Orquesta el flujo del programa:
    1. Solicita al usuario una URL.
    2. Descarga el contenido HTML del artículo.
    3. Extrae el texto principal del HTML.
    4. Valida el texto y lo convierte en audio si es adecuado.
    """
    # Solicitar al usuario ingresar la URL del artículo.
    url = input("Introduce la URL del artículo: ").strip()
    
    # Validar la URL antes de proceder.
    if not is_valid_url(url):
        print('La URL ingresada no tiene un formato válido. Por favor, intenta de nuevo.')
        return
    
    # Obtener el contenido HTML del artículo.
    html_content = fetch_article(url)

    if html_content:
        # Extraer todo el texto del contenido HTML.
        article_text = extract_text(html_content)
        
        # Validar la longitud del texto extraído antes de continuar.
        if article_text and validate_text_length(article_text):
            print('Texto extraído del artículo:')
            print(article_text[:500])  # Muestra los primeros 500 caracteres para verificar
            # Convertir el texto en audio y reproducirlo.
            text_to_speech(article_text)
        else:
            print('No se pudo procesar el texto extraído.')
    else:
        print('No se pudo obtener el contenido del artículo.')

# Verificar si el archivo se ejecuta como un script principal.
if __name__ == "__main__":
    main()
