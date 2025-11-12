# Instrucciones para usar [Shimmy](https://github.com/Michael-A-Kuykendall/shimmy)

## Descargar modelo en formato .gguf.
Puede ser: [Gemma 3 1B](https://huggingface.co/ggml-org/gemma-3-1b-it-GGUF/resolve/main/gemma-3-1b-it-Q8_0.gguf?download=true)

Colocar el modelo en la carpeta models

# Situarse en la carpeta donde descomprimieron el repositorio y escribir en el cmd:
<code>shimmy.exe serve --bind 0.0.0.0:11434</code>

Logearse en Django con el endpoint [Login](http://localhost:8000/api/login/) -> Peticion POST
Y enviar este JSON:
{
  "username":"admin",
  "password":"1234",
}

Luego hacer una peticion POST al endpoint [Chatbot](http://localhost:8000/api/chatbot/)

con el siguiente JSON:
{
  "pregunta":"dame informacion de los envios",
  "modelo":"gemma-3-1b-it-Q8_0"
}
