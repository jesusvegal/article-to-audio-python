# Article to Audio 🎧📜

This project takes a URL of a web article, extracts the content of the text, and converts it into an audio file using Google Text-to-Speech (gTTS) technology. The goal is to allow users to **listen to articles** in a convenient and accessible way, especially for those who prefer audio content.

## 🚀 Functionality

1. **URL Validation**: The program prompts the user for a URL and checks if it is properly formatted.
2. **HTML Content Retrieval**: It sends an HTTP request to fetch the web page content from the provided URL.
3. **Text Extraction**: Uses BeautifulSoup to extract the text from the article's paragraphs.
4. **Text Validation**: Ensures the extracted text is long enough (at least 50 characters) to be converted into audio.
5. **Audio Conversion**: Uses **Google Text-to-Speech (gTTS)** to generate an audio file and plays it automatically.

## 🛠️ Requirements

This project requires Python 3.x and the following libraries. You can install them using pip:

`bash`
pip install requests beautifulsoup4 gtts

### Dependencies: 🛠️
- **requests**: To make HTTP requests and fetch web content. 📡
- **beautifulsoup4**: To parse and extract data from HTML. 📝
- **gtts**: To convert text to audio. 🎙️
- **os**: To execute operating system commands. 🖥️
- **re**: To validate and work with URLs. 🔗

## 📝 How to Use

- Clone or download this repository to your local machine.
- Install the necessary dependencies.
- Run the program in your preferred terminal or IDE:
- Enter the article URL when prompted by the program:
- The program will download the article content, extract the text, and if it’s suitable, convert it into an audio file named output.mp3. The audio will be automatically played on your system.

## Contributions 🤝

Contributions are welcome! If you have ideas to improve this project or want to add new features, please create a pull request or open an issue. Your contribution is highly valuable.

## License 📜

This project is licensed under the MIT License. See the LICENSE file for more details.

🤍 Enjoy using the Article to Audio project in Python and enhance your text-to-speech experience! 📢🎉🔊

---
# Artículo a Audio 🎧📜

Este proyecto toma una URL de un artículo web, extrae el contenido del texto y lo convierte en un archivo de audio usando la tecnología de Google Text-to-Speech (gTTS). El objetivo es permitir a los usuarios **escuchar artículos** de manera conveniente y accesible, especialmente para aquellos que prefieren contenido en formato de audio.

## 🚀 Funcionalidad

1. **Validación de URL**: El programa solicita al usuario una URL y verifica si está correctamente formateada.
2. **Obtención del contenido HTML**: Realiza una solicitud HTTP para obtener el contenido de la página web desde la URL proporcionada.
3. **Extracción de texto**: Utiliza BeautifulSoup para extraer el texto de los párrafos del artículo.
4. **Validación del texto**: Asegura que el texto extraído tenga suficiente longitud (al menos 50 caracteres) para ser convertido en audio.
5. **Conversión a audio**: Usa **Google Text-to-Speech (gTTS)** para generar un archivo de audio y lo reproduce automáticamente.

## 🛠️ Requisitos

Este proyecto requiere Python 3.x y las siguientes bibliotecas. Puedes instalarlas usando pip:

`bash`
pip install requests beautifulsoup4 gtts

### Dependencias: 🛠️
- **requests**: Para realizar solicitudes HTTP y obtener contenido web. 📡
- **beautifulsoup4**: Para analizar y extraer datos del HTML. 📝
- **gtts**: Para convertir texto en audio. 🎙️
- **os**: Para ejecutar comandos del sistema operativo. 🖥️
- **re**: Para validar y trabajar con URLs. 🔗



## 📝 Cómo Usar 

- Clona o descarga este repositorio en tu máquina local.
- Instala las dependencias necesarias.
- Ejecuta el programa en tu terminal o IDE preferido:
- Ingresa la URL del artículo cuando el programa lo pida:
- El programa descargará el contenido del artículo, extraerá el texto y, si es adecuado, lo convertirá en un archivo de audio output.mp3. El audio será reproducido automáticamente en tu sistema.

## Contribuciones 🤝

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este proyecto o deseas agregar nuevas características, crea una solicitud de extracción o abre un problema. Tu aportación es muy valiosa.

## Licencia 📜

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.

🤍¡Disfruta utilizando el proyecto de artículo a audio en Python y que mejore tus experiencias de texto a voz! 📢🎉🔊
