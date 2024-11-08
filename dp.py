import sqlite3

# Подключение к базе данных
connection = sqlite3.connect('database.dp')
cursor = connection.cursor()

# Создание таблицы, если она не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products
(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER
)
''')


def get_all_products(id_prod, title_prod, description_prod, price_prod):
    # Проверяем, существует ли уже продукт с данным id
    cursor.execute("SELECT * FROM Products WHERE id=?", (id_prod,))
    check_prod = cursor.fetchone()
    # Если продукта нет, добавляем( чисто чтобы затестить)
    if check_prod is None:
        cursor.execute(
            "INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
            (id_prod, title_prod, description_prod, price_prod))
        connection.commit()  # фиксируем
    # Возвращаем ВСЕ продукты из базы данных
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    print(products)
    return products


# вызов функции
all_products_1 = get_all_products(1, 'Product A', 'Description A', 200)
# all_products_2 = get_all_products(2, 'Product B', 'Description B', 100)
# print(all_products_2)

# Закрываем бд
connection.close()