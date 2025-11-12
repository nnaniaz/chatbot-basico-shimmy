import httpx
from django.conf import settings
import re


def generar_respuesta(prompt: str, model: str, temperatura: float = 0.8):
    url = f"{settings.OLLAMA_API}generate"
    payload = {"model": model,
               "prompt": prompt,
               "temperature": temperatura,
               "stream": False,
               "num_predict": 512,
               "stop": ["Usuario:", "Pregunta:"]
               }

    with httpx.Client(timeout=600) as client:
        resp = client.post(url, json=payload)
        resp.raise_for_status()
        data = resp.json()
        return limpiar_respuesta(data.get("response", ""))


def generar_respuesta_llamacpp(prompt: str, n_predict: int = 512, temperatura: float = 0.8):
    url = f"{settings.LLAMACPP_API}completion"
    payload = {"prompt": prompt,
               "n_predict": 512,
               "temperature": temperatura,
               "stream": False,
               "stop": ["Usuario:", "Pregunta:"],
               }

    with httpx.Client(timeout=600) as client:
        print("antes de la peticion", f"{settings.LLAMACPP_API}completion")
        resp = client.post(url, json=payload)
        resp.raise_for_status()
        data = resp.json()
        return limpiar_respuesta(data.get("content", ""))


def limpiar_respuesta(respuesta: str):
    texto = re.sub(r"```+", "", respuesta)
    # Quita espacios al inicio y fin de línea
    texto = texto.strip()

    if texto.startswith("=== RESPUESTA ===\n"):
        texto = texto.replace("=== RESPUESTA ===\n", "")
    if texto.startswith("===\nRespuesta ===\n"):
        texto = texto.replace("===\nRespuesta ===\n", "")
    if texto.startswith("=== RESPUESTA\n"):
        texto = texto.replace("=== RESPUESTA\n", "")
    if texto.startswith("===\nRespuesta\nHistorial relevante:\n"):
        texto = texto.replace("===\nRespuesta\nHistorial relevante:\n", "")
    if texto.startswith("Asistente: "):
        texto = texto.replace("Asistente: ", "").strip()
    if texto.startswith("Asistente:\n"):
        texto = texto.replace("Asistente:\n", "").strip()

    return texto.replace("===\nRespuesta\nHistorial relevante:\n", "")
