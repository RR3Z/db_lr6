import sys

import mysql.connector
from mysql.connector import Error
import mySqlQueries as queries

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

    # Вводное сообщение
    print("Запросы из ЛР6:\n"
          "1 - Получить информацию о заказах с информацией о покупателях\n"
          "2 - Получить информацию об играх\n"
          "3 - Добавить жанр в таблицу genres\n"
          "4 - Добавить новый заказ для пользователя по ID\n"
          "5 - Изменить название разработчика по ID\n"
          "6 - Изменить информацию об игре по ID\n"
          "7 - Удалить жанр по названию\n"
          "8 - Удалить разработчика по названию\n"
          "9 - Аналитический запрос №1 - Получить список всех пользователей и количество их заказов с разбивкой по месяцам за последний год\n"
          "10 - Аналитический запрос №2 - Получить список всех игр, у которых есть скидки в данный момент и указание на текущую скидку (по процентам и по цене в рублях)\n"
          "\nЗапросы для семестровой работы:\n"
          "11 - Получить информацию обо всех зарегистрированных пользователях\n"
          "12 - Добавить нового пользователя в таблицу users\n"
          "13 - Изменить информацию о пользователе по полю login\n"
          "14 - Удалить пользователя из таблицы users\n"
          "15 - Добавить игру к заказу (связь: многие ко многим)\n"
          "16 - Заменить игру в заказе (связь: многие ко многим)\n"
          "17 - Удалить игру из заказа (связь: многие ко многим)\n"
          "18 - Аналитический запрос - Получить список всех заказов, в которых содержится игра с заданным названием\n")

    # Узнать, какой запрос хочет выполнить пользователь
    userChoice = int(input("Ваш выбор: "))

    # Проверка на значение, которое вводить пользователь
    if userChoice < 1 or userChoice > 18:
        print(f"\nЗначения '{userChoice}' нет в списке выбора")
    else:
        # Вызвать запрос, который попросил пользователь
        if userChoice == 1:
            queries.getOrdersData(dbConnection)
        elif userChoice == 2:
            queries.getPcGamesData(dbConnection)
        elif userChoice == 3:
            queries.addGenre(dbConnection)
        elif userChoice == 4:
            queries.addOrder(dbConnection)
        elif userChoice == 5:
            queries.updateDeveloperName(dbConnection)
        elif userChoice == 6:
            queries.updatePcGameInfo(dbConnection)
        elif userChoice == 7:
            queries.deleteGenre(dbConnection)
        elif userChoice == 8:
            queries.deleteDeveloper(dbConnection)
        elif userChoice == 9:
            queries.getUsersOrders(dbConnection)
        elif userChoice == 10:
            queries.getDiscountedGames(dbConnection)
        elif userChoice == 11:
            queries.getUsersData(dbConnection)
        elif userChoice == 12:
            queries.addNewUser(dbConnection)
        elif userChoice == 13:
            queries.updateUserData(dbConnection)
        elif userChoice == 14:
            queries.deleteUser(dbConnection)
        elif userChoice == 15:
            queries.addGameToOrder(dbConnection)
        elif userChoice == 16:
            queries.updateGameInOrder(dbConnection)
        elif userChoice == 17:
            queries.deleteGameFromOrder(dbConnection)
        elif userChoice == 18:
            queries.getOrdersByGameName(dbConnection)

    # Закрыть доступ к БД
    dbConnection.close()











