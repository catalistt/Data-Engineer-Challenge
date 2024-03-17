from typing import List, Tuple
from collections import Counter
import create_json_array 
import re


def q3_time(file_path: str) -> List[Tuple[str, int]]:

    # Inicializar contador para contar tags
    user_counter = Counter()

    # RE para encontrar tags de usuarios
    re_tags = re.compile(r'@([^ ]+)')

    # Obtener los tweets del archivo y contar tags de usuarios
    tweet_list = create_json_array.create_json_array(file_path)
    for tweet in tweet_list:
        if 'content' in tweet:
            # Encontrar todos los tags en el contenido del tweet
            mentions = re_tags.findall(tweet['content'])
            # Aumentar el recuento de cada usuario
            user_counter.update(mentions)

    # Obtener los top 10 usuarios mencionados
    top_10_users = user_counter.most_common(10)
    
    return top_10_users