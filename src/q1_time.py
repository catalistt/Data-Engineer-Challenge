from typing import List, Tuple
from datetime import datetime
import create_json_array
from collections import defaultdict, Counter

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:

    # Obtener la lista de tweets del archivo
    tweet_list = create_json_array.create_json_array(file_path)

    # Inicializar diccionario para almacenar los recuentos de tweets por fecha y usuario
    tweet_counts = defaultdict(lambda: defaultdict(int))

    # Iterar los tweets y contar los tweets por fecha y usuario
    for tweet in tweet_list:
        # Obtener la fecha del tweet y el nombre de usuario
        date_element = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S+00:00').date()
        username_element = tweet['user']['username']

        # Actualizar el recuento de tweets para esta fecha y usuario
        tweet_counts[date_element][username_element] += 1

    # Obtener las top 10 fechas con más tweets
    sorted_dates = sorted(tweet_counts.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]

    # Obtener el usuario con más publicaciones para cada una de las top 10 fechas, iterando sobre las fechas
    top_10_result_list = []
    for date, user_counts in sorted_dates:
        top_user = max(user_counts, key=user_counts.get)
        top_10_result_list.append((date, top_user))

    return top_10_result_list