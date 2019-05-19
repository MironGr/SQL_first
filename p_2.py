import sys
import pickle
import sqlite3 as lite


def query_string_2():
    """
    2. Вывести список пользователей (полное имя, телефон) с указанием
руководителя (полное имя, телефон).
Сохранить в pickle в формате словаря.
    :return:  data = cur.fetchall()
    """
    con = None
    data = {}

    query_string = '''
        SELECT c.FirstName, c.LastName, c.Phone, e.FirstName, e.LastName, e.Phone 
        FROM Customer as c, Employee as e
        CROSS JOIN Employee ON c.CustomerId = e.EmployeeId 
    '''

    try:
        con = lite.connect('vers_1.sqlite')
        cur = con.cursor()
        cur.execute(query_string)
        data = cur.fetchall()
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f)
        for line in data:
            print(line)
        return data
    except Exception as e:
        print(e)
        sys.exit(1)
    finally:
        if con:
            con.close()