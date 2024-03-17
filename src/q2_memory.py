from typing import List, Tuple
import emoji
import heapq
import json


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Inicializar contador para contar emojis
    emoji_counts = {}

    # Abrir archivo e iterar sobre cada linea
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                # Decodificar el JSON a un objeto Python
                tweet = json.loads(line)
                # Verificar si hay un campo 'content' en el tweet
                if 'content' in tweet:
                    content = tweet['content']
                    # Iterar sobre cada caracter del contenido del tweet y verificar si es emoji
                    for char in content:
                        if emoji.is_emoji(char):
                            # Incrementar el recuento del emoji en el diccionario
                            emoji_counts[char] = emoji_counts.get(char, 0) + 1
            except json.JSONDecodeError:
                print("Error al decodificar la línea:", line)

    # Mantener solo los 10 emojis mas comunes utilizando un heap
    top_10_emojis = []
    for emoji_char, count in emoji_counts.items():
        # Si el heap aun no tiene 10 elementos, simplemente agregamos el emoji
        if len(top_10_emojis) < 10:
            heapq.heappush(top_10_emojis, (count, emoji_char))

        # Alternativamente, comparamos la cantidad del emoji actual con la del minimo en el heap
        else:
            # Usar la cuenta, descartar el emoji mientras
            min_count, _ = top_10_emojis[0]

            # Si la cantidad es mayor, eliminamos el emoji min y agregamos el emoji actual
            if count > int(min_count):
                heapq.heappop(top_10_emojis)
                heapq.heappush(top_10_emojis, (count, emoji_char))

    top_10_emojis.sort(reverse=True)

    # Revertir el orden (cantidad, emoji) a (emoji, cantidad)
    top_10_emojis = [(emoji_char, count) for count, emoji_char in top_10_emojis]


    return top_10_emojis