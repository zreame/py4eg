# We are extracting emails from a .txt and adding emails and count to a db 
import sqlite3

# connecting to db, always these 2 lines, cursor acts like a fhandle
# if dont exist, sqlite3 creates it
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

# this first part is from earlier ex, till the sql lines
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fhand = open(fname)

for line in fhand :
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    # ? is to indicate placeholder to prevent sql injection
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone()
    # print('row', row, email)
    if row is None :
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        # Use the direct value of count here with Update
        # Single atomic operation, dont have to worry about other pieces of code modifying it
        # we dont want to take the earlier count value and use py to add one and update 
        # because that is 2 operations, not atomic
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    # above loop runs fast, commit saves data to disk, slower, so we might want to commit every 10 loops for example
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr) :
    print(str(row[0]), row[1])

cur.close()