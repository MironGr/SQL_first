import sys
import sqlite3 as lite


def query_string_1():
    """
    1. Вывести 10 клиентов (id, имя, номер телефона, компания),
которых обслуживают сотрудники старше 50 лет, оплативших
музыку в любом жанре кроме Rock.
Выходные данные должны быть отсортированы по городу пользователя
в алфавитном порядке и емейлу в обратном.
    :return:  data = cur.fetchall()
    """
    con = None
    data = ''

    query_string = '''
        SELECT c.CustomerId, c.FirstName, c.LastName, c.Phone, c.Company
        FROM Customer as c
        INNER JOIN Employee as e,
            Invoice as i,
            InvoiceLine as il,
            Track as t,
            Genre as g
        ON c.CustomerId = e.EmployeeId 
        AND c.CustomerId = i.CustomerId
        AND i.CustomerId = il.InvoiceId
        AND il.TrackId = t.TrackId
        AND t.TrackId = g.GenreId
        WHERE e.BirthDate < '1969-01-01' AND g.Name != 'Rock'
        ORDER BY c.City AND c.Email DESC
    '''

    try:
        con = lite.connect('vers_1.sqlite')
        cur = con.cursor()
        cur.execute(query_string)
        data = cur.fetchall()
        for line in data:
            print(line)
        return data
    except Exception as e:
        print(e)
        sys.exit(1)
    finally:
        if con:
            con.close()
