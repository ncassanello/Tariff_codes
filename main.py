from fastapi import FastAPI, Query
from typing import List

# Simulación de base de datos de clasificación arancelaria
nomenclador_sistema_armonizado = [
    {"codigo": "0101.21", "descripcion": "Caballos de raza pura para reproducción"},
    {"codigo": "0201.30", "descripcion": "Carne de bovino, fresca o refrigerada"},
    {"codigo": "0302.12", "descripcion": "Salmón del Atlántico, fresco o refrigerado"},
]

app = FastAPI()

@app.get("/clasificar/")
def clasificar_producto(descripcion: str = Query(..., min_length=3)) -> List[dict]:
    """Busca códigos arancelarios que coincidan con la descripción ingresada."""
    resultados = [item for item in nomenclador_sistema_armonizado if descripcion.lower() in item["descripcion"].lower()]
    
    return {"descripcion_ingresada": descripcion, "resultados": resultados}
