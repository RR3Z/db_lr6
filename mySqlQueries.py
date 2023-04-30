# ПОЛУЧЕНИЕ ДАННЫХ
# Получить информацию о заказах с информацией о покупателях
def getOrdersData(dbConnection):
    myCursor = dbConnection.cursor()

    # Обратиться к БД с запросом
    readOrdersDataQuery = """
                          SELECT users.login, orders.product_units, orders.order_date
                          FROM orders
                          INNER JOIN users
                          ON orders.id_users = users.id_users;
    """
    myCursor.execute(readOrdersDataQuery)
    for dbData in myCursor:
        print(dbData)

    myCursor.close()

# Получить название игры, ее стоимость, ее разработчика(developer)
def getPcGamesData(dbConnection):
    myCursor = dbConnection.cursor()

    # Обратиться к БД с запросом
    readPcGamesDataQuery = """
                    SELECT pc_games.name, pc_games.price, developers.company_name
                    FROM pc_games
                    JOIN developers ON pc_games.id_developers = developers.id_developers
    """
    myCursor.execute(readPcGamesDataQuery)
    for dbData in myCursor:
        print(dbData)

    myCursor.close()


# ДОБАВЛЕНИЕ ДАННЫХ
# Добавить жанр в таблицу genres
def addGenre(dbConnection):
    myCursor = dbConnection.cursor()

    # Получить данные от пользователя
    genreName = input("Имя жанра: ")
    genreDesc = input("Описание жанра: ")
    genre = (genreName, genreDesc)

    # Обратиться к БД с запросом
    addGenreQuery = "INSERT INTO genres (name, description) VALUES ('%s','%s');"

    myCursor.execute(addGenreQuery % genre)
    dbConnection.commit()

    myCursor.close()

# Добавить новый заказ пользователя по ID
def addOrder(dbConnection):
    myCursor = dbConnection.cursor()

    # Получить данные от пользователя
    orderDate = input("Введите дату заказа (YYYY-MM-DD HH:MM:SS): ")
    productUnits = int(input("Введите кол-во доступных единиц товара: "))
    userId = int(input("Введите id пользователя, который осуществляет заказ: "))
    order = (orderDate, productUnits, userId)

    # Обратиться к БД с запросом
    addOrderQuery = "INSERT INTO orders (order_date, product_units, id_users) VALUES ('%s', %d, %d);"
    myCursor.execute(addOrderQuery % order)
    dbConnection.commit()

    myCursor.close()


# ИЗМЕНЕНИЕ ДАННЫХ
# Изменить имя компании разработчика по id
def updateDeveloperName(dbConnection):
    myCursor = dbConnection.cursor()

    # Получить от пользователя id компании, чье имя хотим изменить
    idDeveloper = int(input("Введите id компании, чье имя хотите изменить: "))

    # Проверить имеется ли хотя бы одна запись с заданным именем в таблице
    checkDeveloperIdQuery = "SELECT id_developers FROM developers WHERE id_developers = %d;"
    myCursor.execute(checkDeveloperIdQuery % idDeveloper)
    result = myCursor.fetchone()

    if result:
        # Получить новое имя компании
        newCompanyName = input("Введите новое название компании: ")

        # Изменить название компании разработчика по ID
        updateDeveloperNameQuery = "UPDATE db.developers SET db.developers.company_name = '%s' WHERE db.developers.id_developers = %d;"
        newDeveloperName = (newCompanyName, idDeveloper)
        myCursor.execute(updateDeveloperNameQuery % newDeveloperName)
        dbConnection.commit()
    else:
        # Вывести ошибку, что нет полей с заданным пользователем id
        print(f"В таблице developers нет разработчика с id {idDeveloper}")

    myCursor.close()

# Изменить информацию об игре по имени
def updatePcGameInfo(dbConnection):
    myCursor = dbConnection.cursor()

    # Получить название игры, чью информацию мы хотим изменить
    gameName = input("Название игры: ")

    # Проверить имеется ли хотя бы одна запись с заданным именем в таблице
    checkPcGameNameQuery = "SELECT * FROM pc_games WHERE name = '%s';"
    myCursor.execute(checkPcGameNameQuery % gameName)
    result = myCursor.fetchone()

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
        myCursor.execute(updatePcGameInfoQuery % pcGameInfo)
        dbConnection.commit()
    else:
        # Вывести ошибку, что в таблице с играми нет игры с заданным пользователем именем
        print(f"В таблице pc_games нет игры с именем {gameName}")

    myCursor.close()


# УДАЛЕНИЕ ДАННЫХ
# Удалить жанр по названию
def deleteGenre(dbConnection):
    myCursor = dbConnection.cursor()

    genreName = input("Введите название жанра: ")

    # Проверить имеется ли хотя бы одна запись с данным именем жанра в таблице
    checkGenreNameQuery = "SELECT * FROM genres WHERE name = '%s';"
    myCursor.execute(checkGenreNameQuery % genreName)
    result = myCursor.fetchone()

    if result:
        # Обратиться к БД с запросом
        deleteGenreQuery = "DELETE FROM genres WHERE name = '%s';"
        myCursor.execute(deleteGenreQuery % genreName)
        dbConnection.commit()
    else:
        print(f"В таблице genres нет жанра с именем {genreName}")

    myCursor.close()

# Удалить разработчика по названию
def deleteDeveloper(dbConnection):
    myCursor = dbConnection.cursor()

    developerName = input("Введите имя компании разработчика: ")

    # Проверить имеется ли хотя бы одна запись с данным именем компании в таблице
    checkDeveloperNameQuery = "SELECT * FROM developers WHERE company_name = '%s';"
    myCursor.execute(checkDeveloperNameQuery % developerName)
    result = myCursor.fetchone()

    if result:
        # Обратиться к БД с запросом
        deleteDeveloperQuery = "DELETE FROM developers WHERE company_name = '%s';"
        myCursor.execute(deleteDeveloperQuery % developerName)
        dbConnection.commit()
    else:
        print(f"В таблице developers нет поля с именем {developerName}")

    myCursor.close()


# Аналитические запросы
# Аналитический запрос №1: Получить список всех пользователей и количество их заказов с разбивкой по месяцам за последний год
def getUsersOrders(dbConnection):
    myCursor = dbConnection.cursor()

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

    myCursor.execute(getUsersOrdersQuery)
    result = myCursor.fetchall()

    # Вывести результат запроса
    if result:
        for year, month, user_id, nickname, orders_count in result:
            print(f"{year}-{month:02d}: User {user_id} ({nickname}) made {orders_count} orders")
    else:
        print("За последний год не было совершено заказов")

    myCursor.close()

# Аналитический запрос №2: Получить список всех игр, у которых есть скидки в данный момент и указание на текущую скидку (по процентам и по цене в рублях)
def getDiscountedGames(dbConnection):
    myCursor = dbConnection.cursor()

    # Обратиться к БД с запросом
    getDiscountedGamesQuery = """
                            SELECT pc_games.name, pc_games.price, discounts.discount_percentage, discounts.discount_price
                            FROM pc_games
                            INNER JOIN discounts ON pc_games.id_games = discounts.id_games 
                            WHERE NOW() BETWEEN discounts.start_date AND discounts.end_date  
    """
    myCursor.execute(getDiscountedGamesQuery)
    result = myCursor.fetchall()

    # Вывести результат запроса
    if result:
        for game in result:
            print(game)
    else:
        print("Игр со скидками не имеется")

    myCursor.close()



# Запросы для семестровой работы
# Получить информацию обо всех зарегистрированных пользователях
def getUsersData(dbConnection):
    myCursor = dbConnection.cursor()

    # Обратиться к БД с запросом
    getUsersDataQuery = "SELECT * FROM users"
    myCursor.execute(getUsersDataQuery)
    for result in myCursor:
        print(result)

    myCursor.close()

# Добавить нового пользователя в таблицу users
def addNewUser(dbConnection):
    myCursor = dbConnection.cursor()

    # Получить данные от пользователя
    userLogin = input("Логин пользователя: ")
    userPassword = input("Пароль пользователя: ")
    userNickname = input("Псевдоним пользователя: ")
    userMail = input("Почта пользователя: ")
    userInfo = (userLogin, userPassword, userNickname, userMail)

    # Обратиться к БД с запросом
    addNewUserQuery = "INSERT INTO users (login, password, nickname, mail, registration_date) VALUES ('%s','%s','%s','%s',NOW());"

    myCursor.execute(addNewUserQuery % userInfo)
    dbConnection.commit()

    myCursor.close()

# Изменить информацию о пользователе по полю login
def updateUserData(dbConnection):
    myCursor = dbConnection.cursor()

    # Получить от пользователя login
    userLogin = int(input("Введите login пользователя: "))

    # Проверить имеется ли хотя бы одна запись с заданным login в таблице users
    checkUserLoginQuery = "SELECT login FROM users WHERE login = %s;"
    myCursor.execute(checkUserLoginQuery % userLogin)
    result = myCursor.fetchone()

    if result:
        # Получить новые данные от пользователя
        newUserLogin = input("Введите новый логин пользователя: ")
        newUserPassword = input("Введите новый пароль пользователя: ")
        newUserNickname = input("Введите новый псевдоним пользователя: ")
        newUserMail = input("Введите новую почту пользователя: ")
        userData = (newUserLogin, newUserPassword, newUserNickname, newUserMail, userLogin)

        # Изменить информацию о пользователе
        updateUserDataQuery = """
                            UPDATE users 
                            SET login = '%s', 
                                password = '%s', 
                                nickname = '%s', 
                                mail = '%s' 
                            WHERE login = '%s';
        """
        myCursor.execute(updateUserDataQuery % userData)
        dbConnection.commit()
    else:
        # Вывести ошибку, что нет полей с заданным login в таблице users
        print(f"В таблице users нет пользователя с login '{userLogin}'")

    myCursor.close()

# Удалить пользователя из таблицы users
def deleteUser(dbConnection):
    myCursor = dbConnection.cursor()

    # Получить login пользователя
    userLogin = input("Введите login пользователя: ")

    # Проверить имеется ли хотя бы одна запись с заданным login в таблице users
    checkUserLoginQuery = "SELECT * FROM users WHERE login = '%s';"
    myCursor.execute(checkUserLoginQuery % userLogin)
    checkUserLoginResult = myCursor.fetchone()

    if checkUserLoginResult:
        # Обратиться к БД с запросом
        deleteUserQuery = "DELETE FROM users WHERE login = '%s';"
        myCursor.execute(deleteUserQuery % userLogin)
        dbConnection.commit()
    else:
        print(f"В таблице users нет пользователя с логином '{userLogin}'")

    myCursor.close()


# Работа со связью многие-ко-многим
# Добавить игру в заказ
def addGameToOrder(dbConnection):
    myCursor = dbConnection.cursor()

    # Получить данные от пользователя
    idOrder = int(input("Номер заказа: "))
    gameName = input("Название игры: ")

    # Проверить имеется ли запись с заданным id в таблице
    checkIdOrderQuery = "SELECT * FROM orders WHERE id_orders = %d;"
    myCursor.execute(checkIdOrderQuery % idOrder)
    checkIdOrderResult = myCursor.fetchone()

    if checkIdOrderResult:
        # Проверить имеется ли запись с заданной игрой в таблице pc_games
        checkGameNameQuery = "SELECT * FROM pc_games WHERE name = '%s';"
        myCursor.execute(checkGameNameQuery % gameName)
        checkGameNameResult = myCursor.fetchone()

        if checkGameNameResult:
            # Обратиться к БД с запросом
            addGameToOrderQuery = "INSERT INTO pc_games_to_orders (id_games, id_orders) VALUES ((SELECT id_games FROM pc_games WHERE name = '%s'), %d);"

            gameInOrder = (gameName, idOrder)
            myCursor.execute(addGameToOrderQuery % gameInOrder)
            dbConnection.commit()
        else:
            print(f"Игры с названием '{gameName}' не существует")
    else:
        print(f"Заказа с номер '{idOrder}' не существует")

    myCursor.close()

# Заменить игру в заказе
def updateGameInOrder(dbConnection):
    myCursor = dbConnection.cursor()

    # Получить номер заказа у пользователя
    idOrder = int(input("Номер заказа: "))

    # Проверить имеется ли запись с заданным номером заказа в таблице orders
    checkIdOrderQuery = "SELECT * FROM orders WHERE id_orders = %d;"
    myCursor.execute(checkIdOrderQuery % idOrder)
    checkIdOrderResult = myCursor.fetchone()

    if checkIdOrderResult:
        gameName = input("Название игры, которую хотите заменить: ")

        # Проверить имеется ли запись с заданной игрой в таблице pc_games_to_orders
        checkGameNameInOrderQuery = "SELECT * FROM pc_games_to_orders WHERE id_orders = %d AND id_games = (SELECT id_games FROM pc_games WHERE name = '%s');"
        myCursor.execute(checkGameNameInOrderQuery % (idOrder, gameName))
        checkGameNameInOrderResult = myCursor.fetchone()

        if checkGameNameInOrderResult:
            newGameName = input("Название игры, которую хотите добавить: ")

            # Проверить имеется ли запись с новой заданной игрой в таблице pc_games
            checkNewGameNameQuery = "SELECT * FROM pc_games WHERE id_games = (SELECT id_games FROM pc_games WHERE name = '%s');"
            myCursor.execute(checkNewGameNameQuery % newGameName)
            checkNewGameNameResult = myCursor.fetchone()

            if checkNewGameNameResult:
                gameInOrder = (newGameName, idOrder, gameName)

                # Обратиться к БД с запросом
                updateGameToOrderQuery = "UPDATE pc_games_to_orders SET id_games = (SELECT id_games FROM pc_games WHERE name = '%s') WHERE id_orders = %d AND id_games = (SELECT id_games FROM pc_games WHERE name = '%s');"
                myCursor.execute(updateGameToOrderQuery % gameInOrder)
                dbConnection.commit()
            else:
                print(f"Игры с названием '{newGameName}' не существует")
        else:
            print(f"Игры с названием '{gameName}' в заказе с номер '{idOrder}' не имеется")
    else:
        print(f"Заказа с номер '{idOrder}' не существует")

    myCursor.close()

# Удалить игру из заказа
def deleteGameFromOrder(dbConnection):
    myCursor = dbConnection.cursor()

    # Получить номер заказа у пользователя
    idOrder = int(input("Номер заказа: "))

    # Проверить имеется ли запись с заданным номером заказа в таблице orders
    checkIdOrderQuery = "SELECT * FROM orders WHERE id_orders = %d;"
    myCursor.execute(checkIdOrderQuery % idOrder)
    checkIdOrderResult = myCursor.fetchone()

    if checkIdOrderResult:
        gameName = input("Название игры, которую хотите удалить: ")

        checkGameNameQuery = "SELECT id_games FROM pc_games WHERE name = '%s';"
        myCursor.execute(checkGameNameQuery % gameName)
        checkGameNameResult = myCursor.fetchone()

        if checkGameNameResult:
            # Проверить имеется ли запись с заданной игрой в таблице pc_games_to_orders
            checkGameNameInOrderQuery = "SELECT * FROM pc_games_to_orders WHERE id_orders = %d AND id_games = (SELECT id_games FROM pc_games WHERE name = '%s');"
            myCursor.execute(checkGameNameInOrderQuery % (idOrder, gameName))
            checkGameNameInOrderResult = myCursor.fetchone()

            if checkGameNameInOrderResult:
                    gameInOrder = (idOrder, gameName)

                    # Обратиться к БД с запросом
                    updateGameToOrderQuery = "DELETE FROM pc_games_to_orders WHERE id_orders = %d AND id_games = (SELECT id_games FROM pc_games WHERE name = '%s');"
                    myCursor.execute(updateGameToOrderQuery % gameInOrder)
                    dbConnection.commit()
            else:
                print(f"Игры с названием '{gameName}' в заказе с номер '{idOrder}' не имеется")
        else:
            print(f"Игры с названием '{gameName}' не существует")
    else:
        print(f"Заказа с номер '{idOrder}' не существует")

    myCursor.close()

# Аналитический запрос: Получить список всех заказов, в которых содержится игра с заданным названием
def getOrdersByGameName(dbConnection):
    myCursor = dbConnection.cursor()

    # Получить название игры у пользователя
    gameName = input("Введите название игры: ")

    # Проверить, имеется ли игра с заданным именем в таблице pc_games
    checkGameNameQuery = "SELECT id_games FROM pc_games WHERE name = '%s';"
    myCursor.execute(checkGameNameQuery % gameName)
    checkGameNameResult = myCursor.fetchone()

    if checkGameNameResult:
        # Обратиться к БД с запросом
        getOrdersDataByGameNameQuery = """
                        SELECT users.nickname, orders.id_orders, orders.order_date FROM pc_games
                        JOIN pc_games_to_orders ON pc_games.id_games = pc_games_to_orders.id_games
                        JOIN orders ON pc_games_to_orders.id_orders = orders.id_orders
                        JOIN users ON orders.id_users = users.id_users
                        WHERE pc_games.name = '%s';
        """

        myCursor.execute(getOrdersDataByGameNameQuery % gameName)
        ordersDataByGameNameResult = myCursor.fetchall()

        # Вывести результат выполнения запроса
        if ordersDataByGameNameResult:
            for result in ordersDataByGameNameResult:
                print(f"User: {result[0]}, Order ID: {result[1]}, Order date: {result[2]}")
        else:
            print(f"Ни один человек игру '{gameName}' не приобрел")
    else:
        print(f"Игры с названием '{gameName}' не существует")
    myCursor.close()