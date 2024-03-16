from typing import List, Tuple
import json
from collections import Counter
import emoji

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Inicializar contador para contar emojis
    emoji_counter = Counter()

    # Abrir archivo e iterar sobre cada linea
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                # Decodificar el JSON a un objeto Python
                tweet = json.loads(line)
                # Verificar si hay un campo 'content' en el tweet y almacenar
                if 'content' in tweet:
                    content = tweet['content']
                    # Iterar sobre cada caracter del contenido del tweet y verificar si es emoji
                    for char in content:
                        if emoji.is_emoji(char):
                            emoji_counter[char] += 1
            except json.JSONDecodeError:
                print("Error al decodificar la línea:", line)

    # Obtener los top 10 emojis y sus recuentos
    top_10_emojis = emoji_counter.most_common(10)
    
    return top_10_emojis