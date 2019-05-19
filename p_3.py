import sys
import sqlite3 as lite


def query_string_3():
    """
      3. Вывести отсортированный список клиентов (имя, телефон) оплативших
    самые дорогие музыкальные треки.
    :return:  data = cur.fetchall()
    """
    con = None
    data = ''

    query_string = '''
        SELECT c.FirstName, c.LastName, c.Phone
        FROM Customer as c
        INNER JOIN Invoice as i,
            InvoiceLine as il,
            Track as t
        ON c.CustomerId = i.CustomerId
        AND i.CustomerId = il.InvoiceId
        AND il.TrackId = t.TrackId
        WHERE t.UnitPrice = (SELECT MAX(t.UnitPrice))
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
