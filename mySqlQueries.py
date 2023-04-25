# ПОЛУЧЕНИЕ ДАННЫХ
# Получить информацию о заказах с информацией о покупателях
def readOrdersData(myСursor):
    # Обратиться к БД с запросом
    readOrdersDataQuery = """
                          SELECT users.login, orders.product_units, orders.order_date
                          FROM orders
                          INNER JOIN users
                          ON orders.id_users = users.id_users;
    """
    myСursor.execute(readOrdersDataQuery)
    for dbData in myСursor:
        print(dbData)

# Получить название игры, ее стоимость, ее разработчика(developer)
def readPcGamesData(myСursor):
    # Обратиться к БД с запросом
    readPcGamesDataQuery = """
                    SELECT pc_games.name, pc_games.price, developers.company_name
                    FROM pc_games
                    JOIN developers ON pc_games.id_developers = developers.id_developers
    """
    myСursor.execute(readPcGamesDataQuery)
    for dbData in myСursor:
        print(dbData)


# ДОБАВЛЕНИЕ ДАННЫХ
# Добавить жанр в таблицу genres
def addGenre(myСursor, dbConnection):
    # Получить данные от пользователя
    genreName = input("Имя жанра: ")
    genreDesc = input("Описание жанра: ")
    genre = (genreName, genreDesc)

    # Обратиться к БД с запросом
    addGenreQuery = "INSERT INTO genres (name, description) VALUES (%s,%s);"

    myСursor.execute(addGenreQuery % genre)
    dbConnection.commit()

# Добавить новый заказ для пользователя по ID
def addOrder(myСursor, dbConnection):
    # Получить данные от пользователя
    orderDate = input("Введите дату заказа (YYYY-MM-DD HH:MM:SS): ")
    productUnits = int(input("Введите кол-во доступных единиц товара: "))
    userId = int(input("Введите id пользователя, который осуществляет заказ: "))
    order = (orderDate, productUnits, userId)

    # Обратиться к БД с запросом
    addOrderQuery = "INSERT INTO orders (order_date, product_units, id_users) VALUES ('%s', %d, %d);"
    myСursor.execute(addOrderQuery % order)
    dbConnection.commit()


# ИЗМЕНЕНИЕ ДАННЫХ
# Изменить имя компании разработчика по id
def updateDeveloperName(myСursor, dbConnection):
    # Получить от пользователя id компании, чье имя хотим изменить
    idDeveloper = int(input("Введите id компании, чье имя хотите изменить: "))

    # Проверить имеется ли хотя бы одна запись с заданным именем в таблице
    checkDeveloperId = "SELECT id_developers FROM developers WHERE id_developers = %d;"
    myСursor.execute(checkDeveloperId % idDeveloper)
    result = myСursor.fetchone()

    if result:
        # Получить новое имя компании
        newCompanyName = input("Введите новое название компании: ")

        # Изменить название компании разработчика по ID
        updateDeveloperNameQuery = "UPDATE db.developers SET db.developers.company_name = '%s' WHERE db.developers.id_developers = %d;"
        newDeveloperName = (newCompanyName, idDeveloper)
        myСursor.execute(updateDeveloperNameQuery % newDeveloperName)
        dbConnection.commit()
    else:
        # Вывести ошибку, что нет полей с заданным пользователем id
        print(f"В таблице developers нет разработчика с id {idDeveloper}")

# Изменить информацию об игре по имени
def updatePcGameInfo(myСursor, dbConnection):
    # Получить название игры, чью информацию мы хотим изменить
    gameName = input("Название игры: ")

    # Проверить имеется ли хотя бы одна запись с заданным именем в таблице
    checkPcGameName = "SELECT * FROM pc_games WHERE name = '%s';"
    myСursor.execute(checkPcGameName % gameName)
    result = myСursor.fetchone()

    if result:
        # Получить от пользователя новые данные
        newGameName = input("Введите новое название игры: ")
        gameDesc = input("Введите новое описание игры: ")
        gameUnits = int(input("Введите кол-во доступных единиц товара: "))
        gamePrice = float(input("Введите цену игры: "))
        gameReleaseDate = input("Введите дату релиза (YYYY-MM-DD): ")
        gameIdGenre = int(input("Введите id жанра соответствующей данной игре: "))
        gameIdPublishers = int(input("Введите id издателя: "))
        gameIdDeveloper = int(input("Введите id разработчика: "))

        # Обратиться к БД с запросом
        updatePcGameInfoQuery = """
                                UPDATE pc_games
                                    SET name = '%s', 
                                    description = '%s', 
                                    available_units = %d, 
                                    price = %f, 
                                    release_date = '%s', 
                                    id_genres = %d, 
                                    id_publishers = %d, 
                                    id_developers = %d
                                WHERE name = '%s';
        """
        pcGameInfo = (
            newGameName, gameDesc, gameUnits, gamePrice, gameReleaseDate, gameIdGenre, gameIdPublishers,
            gameIdDeveloper,
            gameName)
        myСursor.execute(updatePcGameInfoQuery % pcGameInfo)
        dbConnection.commit()
    else:
        # Вывести ошибку, что в таблице с играми нет игры с заданным пользователем именем
        print(f"В таблице pc_games нет игры с именем {gameName}")


# УДАЛЕНИЕ ДАННЫХ
# Удалить жанр по названию
def deleteGenre(myСursor, dbConnection):
    genreName = input("Введите название жанра: ")

    # Проверить имеется ли хотя бы одна запись с данным именем жанра в таблице
    checkGenreName = "SELECT * FROM genres WHERE name = '%s';"
    myСursor.execute(checkGenreName % genreName)
    result = myСursor.fetchone()

    if result:
        # Обратиться к БД с запросом
        deleteGenreQuery = "DELETE FROM genres WHERE name = '%s';"
        myСursor.execute(deleteGenreQuery % genreName)
        dbConnection.commit()
    else:
        print(f"В таблице genres нет жанра с именем {genreName}")

# Удалить разработчика по названию
def deleteDeveloper(myСursor, dbConnection):
    developerName = input("Введите имя компании разработчика: ")

    # Проверить имеется ли хотя бы одна запись с данным именем компании в таблице
    checkDeveloperName = "SELECT * FROM developers WHERE company_name = '%s';"
    myСursor.execute(checkDeveloperName % developerName)
    result = myСursor.fetchone()

    if result:
        # Обратиться к БД с запросом
        deleteDeveloperQuery = "DELETE FROM developers WHERE company_name = '%s';"
        myСursor.execute(deleteDeveloperQuery % developerName)
        dbConnection.commit()
    else:
        print(f"В таблице developers нет поля с именем {developerName}")


# Аналитические запросы
# Запрос №1 : Получить список всех пользователей и количество их заказов с разбивкой по месяцам за последний год
def getUsersOrders(myСursor):
    # Обратиться к БД с запросом
    getUsersOrdersQuery = """
            SELECT 
                YEAR(orders.order_date) AS year,
                MONTH(orders.order_date) AS month,
                users.id_users,
                users.nickname,
                COUNT(orders.id_orders) AS orders_count
            FROM 
                users 
                LEFT JOIN orders ON users.id_users = orders.id_users
            WHERE 
                orders.order_date >= DATE_SUB(NOW(), INTERVAL 1 YEAR)
            GROUP BY 
                year, month, users.id_users
            ORDER BY 
                year, month, users.id_users
        """

    myСursor.execute(getUsersOrdersQuery)
    result = myСursor.fetchall()

    # Вывести результат запроса
    if result:
        for year, month, user_id, nickname, orders_count in result:
            print(f"{year}-{month:02d}: User {user_id} ({nickname}) made {orders_count} orders")
    else:
        print("За последний год не было совершено заказов")

# Запрос №2: Получить список всех игр, у которых есть скидки в данный момент и указание на текущую скидку (по процентам и по цене в рублях)
def getDiscountedGames(myСursor):
    # Обратиться к БД с запросом
    getDiscountedGamesQuery = """
                            SELECT pc_games.name, pc_games.price, discounts.discount_percentage, discounts.discount_price
                            FROM pc_games
                            INNER JOIN discounts ON pc_games.id_games = discounts.id_games 
                            WHERE NOW() BETWEEN discounts.start_date AND discounts.end_date  
    """
    myСursor.execute(getDiscountedGamesQuery)
    result = myСursor.fetchall()

    # Вывести результат запроса
    if result:
        for game in result:
            print(game)
    else:
        print("Игр со скидками не имеется")