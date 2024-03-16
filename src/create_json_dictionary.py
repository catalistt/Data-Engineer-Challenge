from typing import List
import json
import os

def create_json_dictionary(input_file: str) -> List[dict]:
    # Verificar si el input existe
    if not os.path.exists(input_file):
        print(f"El archivo {input_file} no existe.")
        return None

    # Inicializar diccionario de JSON
    json_dictionary = []

    # Iterar linea por linea
    with open(input_file, 'r') as file:
        for line_number, line in enumerate(file, start=1): 
            try:
                # Cargar la línea como un objeto JSON y agregarlo al diccionario
                json_data = json.loads(line)
                json_dictionary.append(json_data)

                # Ignorar la linea del archivo si es que no esta en formato JSOM
            except json.JSONDecodeError as e:
                print(f"Error al decodificar la línea {line_number}: {e}")
                continue

    return json_dictionary