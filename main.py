import mysql.connector
from mysql.connector import Error
import mySqlQueries as query

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

dbConnection = create_connection("localhost", "root", "951753swdQ", "db")
mycursor = dbConnection.cursor()
print("1 - Получить информацию о заказах с информацией о покупателях\n"
      "2 - Получить информацию об играх\n"
      "3 - Добавить жанр в таблицу genres\n"
      "4 - Добавить новый заказ для пользователя по ID\n"
      "5 - Изменить название разработчика по ID\n"
      "6 - Изменить информацию об игре по ID\n"
      "7 - Удалить жанр по названию\n"
      "8 - Удалить разработчика по названию\n")


userChoice = int(input("Ваш выбор: "))

if userChoice < 1 or userChoice > 8:
    print(f"Значения '{userChoice}' нет в списке выбора")

if userChoice == 1: query.readOrdersData(mycursor)
elif userChoice == 2: query.readPcGamesData(mycursor)
elif userChoice == 3: query.addGenre(mycursor, dbConnection)
elif userChoice == 4: query.addOrder(mycursor, dbConnection)
elif userChoice == 5: query.updateDeveloperName(mycursor, dbConnection)
elif userChoice == 6: query.updatePcGameInfo(mycursor, dbConnection)
elif userChoice == 7: query.deleteGenre(mycursor, dbConnection)
elif userChoice == 8: query.deleteDeveloper(mycursor, dbConnection)











