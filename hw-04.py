# Какой номер самого дорого заказа за июль?
# Какой номер заказа с самым большим количеством товаров?
# В какой день в июле было сделано больше всего заказов?
# Какой пользователь сделал самое большое количество заказов за июль?
# У какого пользователя самая большая суммарная стоимость заказов за июль?
# Какая средняя стоимость заказа была в июле?
# Какая средняя стоимость товаров в июле?
import json


# ! Формат даты в файле гггг-дд-мм ! Made in Latvia?..
# Фильтрация по дате:
year = 2023
month = 7
print(f'Даты поиска: {year}-**-{"0" * (2 - len(str(month))) + str(month)}')

with open("orders_july_2023.json", "r") as my_file:
    data = json.load(my_file)

    # # # Инициализация переменных под задачи.
    # Какой номер самого дорого заказа за июль?
    max_price = 0
    max_price_numbers = []

    # Какой номер заказа с самым большим количеством товаров?
    max_quantity = 0
    max_quantity_numbers = []

    # В какой день в июле было сделано больше всего заказов?
    day_dict = {}  # date: orders
    max_orders = 1
    max_orders_days = []

    # Какой пользователь сделал самое большое количество заказов за июль?
    users_dict = {}  # user_id: orders
    user_max_orders = 1
    max_orders_users = []

    # У какого пользователя самая большая суммарная стоимость заказов за июль?
    users_price_dict = {}  # user_id: price_summ
    user_max_price = 1
    max_price_users = []

    # Какая средняя стоимость заказа была в июле?
    orders_counter = 0
    orders_summ = 0

    # Какая средняя стоимость товаров в июле?
    products_counter = 0

    # Всё в одном цикле (с проверкой даты):
    for number, order in data.items():
        if order["date"][0:4].isdigit():
            date_year = int(order["date"][0:4])
        else:
            date_year = -1
        if order["date"][8:10].isdigit():
            date_month = int(order["date"][8:10])
        else:
            date_month = -1
        if date_year == year and date_month == month:  # Дата соответствует заданной.

            # Какой номер самого дорого заказа за июль?
            if order["price"] > max_price:
                max_price = order["price"]
                max_price_numbers = []  # Multi-step ... replace... Отвратительно читается.
                max_price_numbers.append(number)  # Сборка нового списка
            else:
                if order["price"] == max_price:  # Более одного номера для максимального значения!
                    max_price_numbers.append(number)

            # Какой номер заказа с самым большим количеством товаров?
            if order["quantity"] > max_quantity:
                max_quantity = order["quantity"]
                max_quantity_numbers = []
                max_quantity_numbers.append(number)
            else:
                if order["quantity"] == max_quantity:  # Более одного номера для максимального значения!
                    max_quantity_numbers.append(number)

            # В какой день в июле было сделано больше всего заказов?
            day_is = order["date"]
            if day_is in day_dict:
                day_dict[day_is] += 1
            else:
                day_dict[day_is] = 1  # Добавляем день.
            if day_dict[day_is] > max_orders:
                max_orders = day_dict[day_is]
                max_orders_days = []
                max_orders_days.append(day_is)
            else:
                if day_dict[day_is] == max_orders:  # Более одной даты для максимального значения!
                    max_orders_days.append(day_is)

            # Какой пользователь сделал самое большое количество заказов за июль?
            user_is = order["user_id"]
            if user_is in users_dict:
                users_dict[user_is] += 1
            else:
                users_dict[user_is] = 1  # Добавляем пользователя
            if users_dict[user_is] > user_max_orders:
                user_max_orders = users_dict[user_is]
                max_orders_users = []
                max_orders_users.append(user_is)
            else:
                if users_dict[user_is] == user_max_orders:  # Более одного пользователя для максимального значения!
                    max_orders_users.append(user_is)

            # У какого пользователя самая большая суммарная стоимость заказов за июль?
            if user_is in users_price_dict:
                users_price_dict[user_is] += order["price"]
            else:
                users_price_dict[user_is] = order["price"]
            if users_price_dict[user_is] > user_max_price:
                user_max_price = users_price_dict[user_is]
                max_price_users = []
                max_price_users.append(user_is)
            else:
                if users_price_dict[user_is] == user_max_price:  # Более одного пользователя для максимального значения!
                    max_price_users.append(user_is)

            # Какая средняя стоимость заказа была в июле?
            orders_counter += 1  # Каждый проход цикла это отдельный заказ (можно и по числу первичных ключей в JSON).
            orders_summ += order["price"]

            # Какая средняя стоимость товаров в июле?
            products_counter += order["quantity"]

        else:  # Дата не подходит, данные по заказу пропускаются.
            continue

    # # # Отображение результатов

    # Какой номер самого дорого заказа за июль?
    if len(max_price_numbers) > 1:
        print(f'Нельзя указать конкретный заказ ({len(max_price_numbers)} штук). Максимальная стоимость заказа: {max_price}')
        print(f'Заказы: {max_price_numbers}')
    elif len(max_price_numbers) == 1:
        print(f'Номер заказа с самой большой стоимостью: {str(max_price_numbers)}. Максимальная стоимость заказа: {max_price}')
    else:
        print(f'ОШИБКА! Ничего не найдено для "max_price_number".')

    # Какой номер заказа с самым большим количеством товаров?
    if len(max_quantity_numbers) > 1:
        print(f'Нельзя указать конкретный заказ ({len(max_quantity_numbers)} штук). Максимальное число товаров в заказе: {max_quantity}')
        print(f'Заказы: {max_quantity_numbers}')
    elif len(max_quantity_numbers) == 1:
        print(f'Номер заказа максимальным количеством товаров: {str(max_quantity_numbers)}. Максимальное число товаров в заказе: {max_quantity}')
    else:
        print(f'ОШИБКА! Ничего не найдено для "max_quantity_number".')

    # В какой день в июле было сделано больше всего заказов?
    if len(max_orders_days) > 1:
        print(f'Нельзя указать конкретный день ({len(max_orders_days)} штук). Максимальное количество заказов в день: {max_orders}')
        print(f'Дни: {max_orders_days}')
    elif len(max_orders_days) == 1:
        print(f'День с максимальным числом заказов - {str(max_orders_days)}. Максимальное количество заказов в день: {max_orders}')
    else:
        print(f'ОШИБКА! Ничего не найдено для "max_orders_day".')

    # Какой пользователь сделал самое большое количество заказов за июль?
    if len(max_orders_users) > 1:
        print(f'Нельзя указать конкретного пользователя ({len(max_orders_users)} штук). Максимальное количество заказов: {user_max_orders}')
        print(f'Пользователи: {max_orders_users}')
    elif len(max_orders_users) == 1:
        print(f'Пользователь с максимальным числом заказов - {str(max_orders_users)}. Максимальное количество заказов: {user_max_orders}')
    else:
        print(f'ОШИБКА! Ничего не найдено для "max_orders_user".')

    # У какого пользователя самая большая суммарная стоимость заказов за июль?
    if len(max_price_users) > 1:
        print(f'Нельзя указать конкретного пользователя ({len(max_price_users)} штук). Максимальная сумма заказов: {user_max_price}')
        print(f'Пользователи: {max_price_users}')
    elif len(max_price_users) == 1:
        print(f'Пользователь с максимальной суммой заказов - {str(max_price_users)}. Максимальная сумма заказов: {user_max_price}')
    else:
        print(f'ОШИБКА! Ничего не найдено для "max_price_user".')

    # Какая средняя стоимость заказа была в июле?
    print(f'Средняя стоимость заказа за выбранный период: {round(orders_summ/orders_counter, 2)} условных единиц/заказ.')

    # Какая средняя стоимость товаров в июле?
    print(f'Средняя стоимость товара за выбранный период: {round(orders_summ / products_counter, 2)} условных единиц/товар.')
