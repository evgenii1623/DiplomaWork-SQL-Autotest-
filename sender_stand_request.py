# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration
# Импорт библиотеки requests для выполнения HTTP-запросов
import requests
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# Определение функции post_new_order для отправки POST-запроса на создание нового заказа
def post_new_order(body):
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
	json=body,
	headers=data.headers)
# Вызов функции post_new_order с телом запроса для создания нового заказа из модуля data
response = post_new_order(data.body)
# Сохраняю номер трека в переменную order_track
order_track=response.json()['track']
# вывожу в консоль трэк заказа
print('номер трэка', order_track)

# Определение функции get_order для отправки get запроса на получение данных по заказу по его номеру
def get_order():
   return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(order_track))
# вызываем функцию get_order
response = get_order()
# проверяем, что на запрос приходит код ответа 200
assert response.status_code == 200
# получаем тело ответа в формате json
print(response.json())

# Евгений Аваргин, 21-я когорта — Финальный проект. Инженер по тестированию плюс