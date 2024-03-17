from typing import List, Tuple
from datetime import datetime
from collections import defaultdict
import create_json_array

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
 # Obtener la lista de tweets del archivo
    tweet_list = create_json_array.create_json_array(file_path)

    # Inicializar un diccionario para almacenar los recuentos de tweets por fecha y usuario
    tweet_counts = defaultdict(lambda: defaultdict(int))

    # Inicializar un diccionario para almacenar el recuento de tweets por fecha
    date_counts = defaultdict(int)

    # Iterar los tweets y contar los tweets por fecha y usuario
    for tweet in tweet_list:
        # Obtener la fecha del tweet y el nombre de usuario
        date_element = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S+00:00').date()
        username_element = tweet['user']['username']

        # Actualizar los recuentos de tweets para esta fecha y usuario
        tweet_counts[date_element][username_element] += 1
        date_counts[date_element] += 1

    # Obtener las top 10 fechas con más tweets
    sorted_dates = sorted(date_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    # Obtener el usuario con más publicaciones para cada una de las top 10 fechas
    top_10_result_list = []
    for date, _ in sorted_dates:
        top_user = max(tweet_counts[date], key=tweet_counts[date].get)
        top_10_result_list.append((date, top_user))

    return top_10_result_list