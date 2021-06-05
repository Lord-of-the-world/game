import sqlite3 as sql



def create_table():
    con = sql.connect("/home/Sham13namo/mysite/game.db")
    cur = con.cursor()
    create = """\
        CREATE TABLE room (
            smth INTEGER PRIMARY KEY AUTOINCREMENT,
            id_room INTEGER NOT NULL,
            player1 TEXT default 'nothing',
            player2 TEXT default 'nothing',
            player3 TEXT default 'nothing',
            player4 TEXT default 'nothing',
            player5 TEXT default 'nothing',
            player6 TEXT default 'nothing',
            player7 TEXT default 'nothing',
            player8 TEXT default 'nothing',
            player9 TEXT default 'nothing',
            colvo_players INTEGER default 0
            )
    """

    create2 = """\
        CREATE TABLE player(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
            )
    """

    create3 = """\
        CREATE TABLE country(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            owner INTEGER NOT NULL,
            money INTEGER default 0,
            bombs INTEGER default 0,
            isopen INTEGER default 0,
            country TEXT)
    """

    create4 = """\
        CREATE TABLE city1(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            level INTEGER DEFAULT 1,
            shield INTEGER DEFAULT 0,
            owner INTEGER,
            name TEXT)
    """

    create5 = """\
        CREATE TABLE city2(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            level INTEGER DEFAULT 1,
            shield INTEGER DEFAULT 0,
            owner INTEGER,
            name TEXT)
    """



    create6 = """\
        CREATE TABLE city3(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            level INTEGER DEFAULT 1,
            shield INTEGER DEFAULT 0,
            owner INTEGER,
            name TEXT)
    """
    try:
        cur.executescript(create)


    except sql.DatabaseError as err:
        print(err)

    try:
        cur.executescript(create2)

    except sql.DatabaseError as err:
        print(err)

    try:
        cur.executescript(create3)

    except sql.DatabaseError as err:
        print(err)

    try:
        cur.executescript(create4)

    except sql.DatabaseError as err:
        print(err)

    try:
        cur.executescript(create5)

    except sql.DatabaseError as err:
        print(err)

    try:
        cur.executescript(create6)

    except sql.DatabaseError as err:
        print(err)

    cur.close()
    con.close()

def write_in_db(table, row, info):#3
    con = sql.connect("/home/Sham13namo/mysite/game.db")
    cur = con.cursor()
    write = f"INSERT INTO {table} ({row}) VALUES ({info})"
    try:
        cur.execute(write)
        con.commit()
    except sql.DatabaseError as err:
        print(err)

    cur.close()
    con.close()

def update(table, row, info,cor1, cor):
    con = sql.connect("/home/Sham13namo/mysite/game.db")
    cur = con.cursor()
    write = f"UPDATE {table} SET {row}={info} WHERE {cor1}={cor}"
    try:
        cur.execute(write)
        con.commit()
    except sql.DatabaseError as err:
        print(err)
    cur.close()
    con.close()

def add_player(room_id, id):
    con = sql.connect("/home/Sham13namo/mysite/game.db")
    cur = con.cursor()
    j = get_inf("room", "colvo_players")[get_cor_inf("room", "smth", room_id)[0][0]-1][0]
    print(j)
    if j <9:
        plus = f"UPDATE room SET colvo_players={j+1} WHERE id_room={room_id}"
        try:
            cur.execute(plus)
            con.commit()
        except sql.DatabaseError as err:
            print(err)
        player_n = "player" + str(get_inf("room", "colvo_players")[0][0])
    #player_n = "player3"
        add = f"UPDATE room SET {player_n}={id} WHERE id_room={room_id}"
        try:
            cur.execute(add)
            con.commit()
        except sql.DatabaseError as err:
            print(err)
    else:
        return 1
    cur.close()
    con.close()

def get_cor_inf(table, col, row):
    con = sql.connect("/home/Sham13namo/mysite/game.db")
    cur = con.cursor()
    get =  f"SELECT {col} FROM {table} WHERE id_room={row}"
    try:
        cur.execute(get)
        c = cur.fetchall()
        return c
    except sql.DatabaseError as err:
        print(err)
    cur.close()
    con.close()

def get_inf(table, col):
    con = sql.connect("/home/Sham13namo/mysite/game.db")
    cur = con.cursor()
    get = f"SELECT {col} FROM {table}"

    try:
        cur.execute(get)
        c = cur.fetchall()
        return c
    except sql.DatabaseError as err:
        print(err)
    cur.close()
    con.close()

def get_inf_f_t(table):
    con = sql.connect("/home/Sham13namo/mysite/game.db")
    cur = con.cursor()
    get = f"SELECT * FROM {table}"
    try:
        cur.execute(get)
        c = cur.fetchall()
        return c
    except sql.DatabaseError as err:
        print(err)
    cur.close()
    con.close()

def find_id(nickname):
    con = sql.connect("/home/Sham13namo/mysite/game.db")
    cur = con.cursor()
    info = get_inf_f_t("player")
    for i in info:
        if i[1] == nickname:
            return i[0]
    cur.close()
    con.close()







print(get_inf_f_t("player"))