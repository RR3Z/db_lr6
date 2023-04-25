import sys

import mysql.connector
from mysql.connector import Error
import mySqlQueries as query

# Соединить приложение и БД
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("\nConnection to MySQL DB successful\n")
    except Error as e:
        print(f"\nThe error '{e}' occurred\n")

    return connection


if __name__ == '__main__':
    # Открыть доступ к БД
    dbConnection = create_connection("localhost", "root", "951753swdQ", "db")
    myСursor = dbConnection.cursor()

    # Вводное сообщение
    print("1 - Получить информацию о заказах с информацией о покупателях\n"
          "2 - Получить информацию об играх\n"
          "3 - Добавить жанр в таблицу genres\n"
          "4 - Добавить новый заказ для пользователя по ID\n"
          "5 - Изменить название разработчика по ID\n"
          "6 - Изменить информацию об игре по ID\n"
          "7 - Удалить жанр по названию\n"
          "8 - Удалить разработчика по названию\n"
          "9 - Аналитический запрос №1 - Получить список всех пользователей и количество их заказов с разбивкой по месяцам за последний год\n"
          "10 - Аналитический запрос №2 - Получить список всех игр, у которых есть скидки в данный момент и указание на текущую скидку (по процентам и по цене в рублях)\n")

    # Узнать, какой запрос хочет выполнить пользователь
    userChoice = int(input("Ваш выбор: "))

    # Проверка на значение, которое вводить пользователь
    if userChoice < 1 or userChoice > 10:
        print(f"\nЗначения '{userChoice}' нет в списке выбора")
    else:
        # Вызвать запрос, который попросил пользователь
        if userChoice == 1:
            query.readOrdersData(myСursor)
        elif userChoice == 2:
            query.readPcGamesData(myСursor)
        elif userChoice == 3:
            query.addGenre(myСursor, dbConnection)
        elif userChoice == 4:
            query.addOrder(myСursor, dbConnection)
        elif userChoice == 5:
            query.updateDeveloperName(myСursor, dbConnection)
        elif userChoice == 6:
            query.updatePcGameInfo(myСursor, dbConnection)
        elif userChoice == 7:
            query.deleteGenre(myСursor, dbConnection)
        elif userChoice == 8:
            query.deleteDeveloper(myСursor, dbConnection)
        elif userChoice == 9:
            query.getUsersOrders(myСursor)
        elif userChoice == 10:
            query.getDiscountedGames(myСursor)

    # Закрыть доступ к БД
    myСursor.close()
    dbConnection.close()











