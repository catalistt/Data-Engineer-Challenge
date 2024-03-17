from typing import List, Tuple
from collections import Counter
import create_json_array 
import re

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Inicializar listas vacias para almacenar tweets y contador de tags
    tweets_content = []
    user_counter = []
    flat_user_counter = []

    # Obtener los tweets del archivo y guardar contenido
    tweet_list = create_json_array.create_json_array(file_path)
    for tweet in tweet_list:
        tweets_content.append(tweet['content'])

    # RE para encontrar tags de usuarios
    re_tags = r'@[^ ]+'

    # Encontrar tags de usuarios en el contenido de los tweets y almacenarlos en user_counter
    for tweet in tweets_content:
        mentions = re.findall(re_tags, tweet)
        if mentions:
            user_counter.append([mention[1:] for mention in mentions])

    # Aplanar la lista de listas de tags de usuarios en una sola lista
    for sublist in user_counter:
        flat_user_counter.extend(sublist)

    # Contar la frecuencia de cada tag de usuario
    user_counter = Counter(flat_user_counter)

    # Obtener los top 10 usuarios mencionados
    top_10_users = user_counter.most_common(10)

    return top_10_users