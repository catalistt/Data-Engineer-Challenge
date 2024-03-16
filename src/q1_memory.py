from typing import List, Tuple
from datetime import datetime
import create_json_array

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Obtener la lista de tweets del archivo
    tweet_list = create_json_array.create_json_array(file_path)

    # Inicializar diccionario para almacenar los recuentos de tweets por fecha y usuario
    tweet_counts = {}

    # Recorrer los tweets y contar los tweets por fecha y usuario
    for tweet in tweet_list:
        # Obtener la fecha del tweet y el nombre de usuario
        date_element = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S+00:00').date()
        username_element = tweet['user']['username']

        # Actualizar el recuento de tweets para esta fecha y usuario
        if date_element in tweet_counts:
            if username_element in tweet_counts[date_element]:
                tweet_counts[date_element][username_element] += 1
            else:
                tweet_counts[date_element][username_element] = 1
        else:
            tweet_counts[date_element] = {username_element: 1}

    # Ordenar las fechas por cantidad de tweets desc
    sorted_dates = sorted(tweet_counts.items(), key=lambda x: sum(x[1].values()), reverse=True)

    # Obtener las top 10 fechas con mas tweets
    top_10_dates = sorted_dates[:10]

    # Inicializar lista para almacenar los resultados finales
    top_10_result_list = []

    # Recorrer las top 10 fechas y obtener el usuario con más publicaciones para cada una
    for date, user_counts in top_10_dates:
        # Obtener el usuario con más publicaciones para esta fecha
        top_user = max(user_counts, key=user_counts.get)
        top_10_result_list.append((date, top_user))

    return top_10_result_list
