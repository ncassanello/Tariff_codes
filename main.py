from fastapi import FastAPI, Query
from typing import List, Dict
import unidecode

# Simulación de base de datos de clasificación arancelaria
nomenclador_sistema_armonizado = [
    {"codigo": "0101.21", "descripcion": "Caballos de raza pura para reproducción"},
    {"codigo": "0201.30", "descripcion": "Carne de bovino, fresca o refrigerada"},
    {"codigo": "0302.12", "descripcion": "Salmón del Atlantico, fresco o refrigerado"},
]

app = FastAPI()

@app.get("/clasificar/", response_model=List[Dict])
def clasificar_producto(descripcion: str = Query(..., min_length=3)):
    """Busca códigos arancelarios que coincidan con la descripción ingresada."""
    descripcion = unidecode.unidecode(descripcion.lower().strip())  # Elimina tildes y normaliza la entrada
    resultados = [
        item for item in nomenclador_sistema_armonizado
        if unidecode.unidecode(item["descripcion"].lower()) == descripcion
    ]
    
    return resultados  # Devolvemos solo la lista
