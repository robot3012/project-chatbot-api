from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from model import load_model, preprocess_input, load_tokenizer, load_label_encoder, decode_prediction

app = FastAPI()

class Consulta(BaseModel):
    pregunta: str

# Cargar el modelo, el tokenizador y el codificador de etiquetas
model = load_model('models/modelo.keras')
tokenizer = load_tokenizer('models/tokenizer.pkl')
label_encoder = load_label_encoder('models/label_encoder.pkl')

@app.post("/consultar/", description="Consulta el chatbot sobre seguros")
async def consultar_seguro(consulta: Consulta):
    if model is None or tokenizer is None or label_encoder is None:
        return {"error": "No se pudo cargar el modelo, el tokenizador o el codificador de etiquetas"}

    try:
        pregunta_procesada = preprocess_input(consulta.pregunta, tokenizer)
        respuesta = model.predict(pregunta_procesada)
        respuesta_legible = decode_prediction(respuesta, label_encoder, threshold=0.5)
        return {"respuesta": respuesta_legible}
    except Exception as e:
        return {"error": f"Error al procesar la consulta: {e}"}
