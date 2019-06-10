#!/usr/bin/python

import sqlite3
from sqlite3 import Error
import gw2db

def create_connection():
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    db_file = r"C:\Users\Brennen\Desktop\python projects\gw2tp\gw2db.db"
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def print_table():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM current_tp")
    rows = cur.fetchall()
    for item in rows :
        print(item[0])



def select_all_recipes(conn):
    """
    Query all rows in the recipes table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM recipes")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_recipe_by_output_id(conn, output_item_id):
    """
    Query recipes by output_item_id
    :param conn: the Connection object
    :param output_item_id:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM recipes WHERE output_item_id=?", (output_item_id,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

def printSellers(ids) :
    names = getName(ids)
    prices = getSellers(ids)
    for i in range(0, len(names)) :
        print(str(ids[i]) + '\t' + str(prices[i]) + '\t' + names[i])

def printBuyers(ids) :
    names = getName(ids)
    prices = getBuyers(ids)
    for i in range(0, len(names)) :
        print(str(ids[i]) + '\t' + str(prices[i]) + '\t' + names[i])

def getName(ids) :
    conn = create_connection()
    cur = conn.cursor()
    names = []
    for item in ids :
        cur.execute("SELECT name FROM items WHERE id=?", (item,))
        rows = cur.fetchall()
        for row in rows:
            #print(row[0])
            names.append(row[0])
    return names

def getID(names) :
    conn = create_connection()
    cur = conn.cursor()
    ids = []
    for item in names :
        cur.execute("SELECT id FROM items WHERE name=?", (item,))
        rows = cur.fetchall()
        for row in rows:
            ids.append(row[0])
            #print(row[0])
    return ids

def getSet(word) :
    conn = create_connection()
    cur = conn.cursor()
    set = []
    for item in word :
        cur.execute("SELECT id FROM items WHERE (name LIKE ?) AND (level = 80)", ('%'+item+'%',))
        rows = cur.fetchall()
        for row in rows:
            set.append(row[0])
            #print(row[0])
    return set

def getMats(word) :
    conn = create_connection()
    cur = conn.cursor()
    set = []
    for item in word :
        cur.execute("SELECT id FROM items WHERE name LIKE ?", ('%'+item+'%',))
        rows = cur.fetchall()
        for row in rows:
            set.append(row[0])
            #print(row[0])
    return set

def getRecipe(ids):
    conn = create_connection()
    cur = conn.cursor()
    set = []
    for id in ids :
        cur.execute("SELECT * FROM recipes WHERE output_item_id=?", (id,))
        rows = cur.fetchall()
        for row in rows:
            set.append(row)
            #print(row[0])
    if set == [] :
        return [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    else :
        #print(set)
        return set
def getBuyers(ids) :
    conn = create_connection()
    cur = conn.cursor()
    set = []
    for id in ids :
        cur.execute("SELECT buys_price FROM tp_current WHERE id=?", (id,))
        rows = cur.fetchall()
        for row in rows:
            set.append(row[0])
            #print(row[0])
        if rows == [] :
            set.append(0)
    return set

def getSellers(ids) :
    conn = create_connection()
    cur = conn.cursor()
    set = []
    for id in ids :
        cur.execute("SELECT sells_price FROM tp_current WHERE id=?", (id,))
        rows = cur.fetchall()
        for row in rows:
            set.append(row[0])
            #print(row[0])
        if rows == [] :
            set.append(0)
    return set

def cost2make(ids) :
    conn = create_connection()
    cur = conn.cursor()
    set = []
    for id in ids :
        #print(id)
        recipe = getRecipe([id])[0]
        ingredients = [recipe[5],recipe[7],recipe[9],recipe[11]]
        amounts = [recipe[6],recipe[8],recipe[10],recipe[12]]
        mats = getSellers(ingredients)
        #mats = getSellers(ingredients)
        #print(ingredients)
        #print(mats)
        #print(amounts)
        cost = mats[0]*amounts[0]+mats[1]*amounts[1]+mats[2]*amounts[2]+mats[3]*amounts[3]
        if recipe[4] != 0 :
            cost = int(cost/recipe[4])
        set.append(cost)
    return ids, set

def profit(id, make, sell) :
    names = getName(id)
    set = []
    for item in range(0,len(id)) :
        #print(sell[item])
        #print(make[item])
        profit = int(sell[item]*0.85-make[item])
        diff = int(-sell[item]+make[item])
        #set.append(profit)
        try :
            if profit> 2000 :
                print(str(id[item]) + '\t' + str(sell[item]) + '\t'  + str(make[item]) + '\t'+ str(profit) + '\t' + str(names[item]))
        except :
            continue
def makeORsell(id, make, sell) :
    names = getName(id)
    set = []
    for item in range(0,len(id)) :
        diff = int(-sell[item]+make[item])
        try :
            if diff > 0 :
                print(str(id[item]) + '\t' + str(make[item]) + '\t'  + str(sell[item]) + '\t'+ str(diff) + '\t' + str(names[item]))
        except :
            continue

if __name__ == '__main__':
    gw2db.update()
    leather =	[36752,	36783,	36818,	36842,	36867,	36891,	45804,	45778,	45791,	45830,	45765,	45817,	11879,	11795,	11837,	11963,	11753,	11921,	11876,	11792,	11834,	11960,	11750,	11918,	11877,	11793,	11835,	11961,	11751,	11919,	11881,	11797,	11839,	11965,	11755,	11923,	11878,	11794,	11836,	11962,	11752,	11920,	11880,	11796,	11838,	11964,	11754,	11922,	11882,	11798,	11840,	11966,	11756,	11924]
    armor =	[36887,	36860,	36839,	36806,	36774,	36746,	45635,	45662,	45648,	45674,	45622,	45609,	10705,	10719,	10712,	10726,	10698,	10691,	10702,	10716,	10709,	10723,	10695,	10688,	10703,	10717,	10710,	10724,	10696,	10689,	10704,	10718,	10711,	10697,	10707,	10721,	10714,	10728,	10700,	10693,	10706,	10720,	10713,	10727,	10699,	10692,	10708,	10722,	10715,	10729,	10701,	10694]
    craft =	[19746,	19736,	19709,	19747,	19735,	72194,	19684,	19880,	19881,	19882,	19883,	19884,	19885,	19886,	37176,	41555,	50366,	13219,	13221,	13222,	13223,	13224,	13225,	13226,	13227,	13228,	13229,	13230,	13220,	13150,	13151,	13147,	13149,	13148,	13158,	13152,	13153,	13154,	13155,	13156,	13157]
    gather = [19745,	19731,	19748,	19729,	19722,	19701,	19700,	19721,	24294,	24341,	24350,	24276,	24356,	24288,	24299,	24282,	76254,	70718,	24295,	24358,	24351,	24277,	24357,	24289,	24300,	24283,	82582,	83757,	83103,	83284,	86269]
    #tpPriceIDs = [36752,	36783,	36818,	36842,	36867,	36891,	45804,	45778,	45791,	45830,	45765,	45817,	11879,	11795,	11837,	11963,	11753,	11921,	11876,	11792,	11834,	11960,	11750,	11918,	11877,	11793,	11835,	11961,	11751,	11919,	11881,	11797,	11839,	11965,	11755,	11923,	11878,	11794,	11836,	11962,	11752,	11920,	11880,	11796,	11838,	11964,	11754,	11922,	11882,	11798,	11840,	11966,	11756,	11924,	36887,	36860,	36839,	36806,	36774,	36746,	45635,	45662,	45648,	45674,	45622,	45609,	10705,	10719,	10712,	10726,	10698,	10691,	10702,	10716,	10709,	10723,	10695,	10688,	10703,	10717,	10710,	10724,	10696,	10689,	10704,	10718,	10711,	10697,	10707,	10721,	10714,	10728,	10700,	10693,	10706,	10720,	10713,	10727,	10699,	10692,	10708,	10722,	10715,	10729,	10701,	10694,	19735,	72194,	19684,	19880,	19881,	19882,	19883,	19884,	19885,	19886,	37176,	41555,	50366]
    #makecost = cost2make(tpPriceIDs)[1]
    #buyprice = getBuyers(tpPriceIDs)
    #sellprice = getSellers(tpPriceIDs)
    #printBuyers(tpPriceIDs)
    #printSellers(tpPriceIDs)
    #profit(tpPriceIDs, makecost, sellprice)
    print('PROFITS \nid \tsell \tmake \tprofit \tname')
    profit(leather+armor, cost2make(leather+armor)[1], getSellers(leather+armor))
    print('__________________________')
    print('MAKE OR BUY \nid \tmake \t buy\t diff\t name')
    makeORsell(craft, cost2make(craft)[1], getBuyers(craft))
