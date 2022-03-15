import _sqlite3

def mysqlite(exchangedate, rate):
    base = _sqlite3.connect('nbu.db')
    cur = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS {}(exchangedate PRIMARY KEY, rate)'.format('currency'))
    base.commit()

    cur.execute('INSERT INTO currency VALUES(?, ?)', (exchangedate, rate))
    base.commit()

    base.close()

# mysqlite('29.04.1994', '26.9492')