import os.path
from random import choice
from string import ascii_uppercase
import sqlite3
DATABASE = 'BD.db'


def get_db(BDD=None):
    global DATABASE
    if BDD is None:
        BDD = DATABASE
    db = sqlite3.connect(BDD)
    db.row_factory = sqlite3.Row
    # db.close()
    return db


def get_question(question, BDD=None):
    try:
        if BDD is None:
            db = get_db()
        else:
            db = get_db('BDs/' + BDD)
        data = db.execute(question).fetchall()
        data = [dict(ix) for ix in data]
    except Exception as e:
        return str(e)
    return data


def get_insert(question, BDD=None):
    try:
        if BDD is None:
            db = get_db()
        else:
            db = get_db('BDs/' + BDD)
        con = db.cursor()
        con.execute(question)
        db.commit()
    except Exception as e:
        return str(e)
    return True


def gen_str(leng):
    return ''.join(choice(ascii_uppercase) for i in range(leng))


def new_bd(bd='def.db'):
    if not os.path.exists('BDs/' + bd):
        try:
            with open('BDs/' + bd, 'a+') as f:
                f.write('')
            f.close()
            return True
        except:
            return False
    else:
        return False


def del_bd(bd='def.db'):
    if os.path.exists('BDs/' + bd):
        try:
            os.remove('BDs/' + bd)
            return True
        except:
            return False
    else:
        return False
