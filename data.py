# заголовки для HTTP-запроса создания нового заказа, указывающие на то, что тело запроса будет в формате JSON
headers = {
"Content-Type": "application/json"
}

# данные заказа для создания новой записи о нем в системе, содержат имя, фамилию, адрес, станцию метро, телефон, срок аренды, дату доставки, комментарий, цвет
body = {
	"firstName": "Evgenii",
	"lastName": "Ivanov",
	"address": "Konoha, 142 apt.",
	"metroStation": 6,
	"phone": "+7 800 355 35 35",
	"rentTime": 5,
	"deliveryDate": "2020-06-06",
	"comment": "Saske, come back to Sosnovyi Bor",
	"color": [
	      "BLACK"
        ]
}
