import requests, json, time, sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def create_table(conn, create_table_sql):
  """ create a table from the create_table_sql statement
  :param conn: Connection object
  :param create_table_sql: a CREATE TABLE statement
  :return:
  """
  try:
      c = conn.cursor()
      c.execute(create_table_sql)
  except Error as e:
      print(e)

# BELOW IS STUFF FOR RECIPE DATABASE =============================================

def add_recipe(conn, recipe) :
    """
    Create a new recipe
    :param conn:
    :param recipe:
    :return:
    """

    data = """ INSERT INTO recipes(id, name, type, output_item_id, output_id_count, input_item_id_1, input_count_1, input_item_id_2, input_count_2, input_item_id_3, input_count_3, input_item_id_4, input_count_4, disciplines)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(data, recipe)
    return cur.lastrowid

def populate_recipes_db() :
    url1 = 'https://api.guildwars2.com/v2/recipes?page='
    url2 = '&page_size='
    for page in range(0, 60) :
        print(page)
        r = requests.get(url1 + str(page) + url2 + str(200))
        info = json.loads(r.text)
        for recipe in range(0,len(info)) :
            c = info[recipe]
            type = c['type']
            output_item_id = c['output_item_id']
            output_item_count = c['output_item_count']
            disciplines = c['disciplines']
            ingredients = c['ingredients']
            input_item_id = [0,0,0,0]
            input_count = [0,0,0,0]
            for items in range(0, len(ingredients)) :
                input_item_id[items] = ingredients[items]['item_id']
                input_count[items] = ingredients[items]['count']
            id = c['id']
            chat_link = c['chat_link']
            temp_recipe = (id, 'name', type, output_item_id, output_item_count, input_item_id[0], input_count[0],  input_item_id[1], input_count[1],  input_item_id[2], input_count[2],  input_item_id[3], input_count[3], 'disciplines')
            add_recipe(temp_recipe)

def sqlRecipe(recipe_info):
  database = r"C:\Users\Brennen\Desktop\python projects\gw2tp\gw2db.db"
  sql_create_recipes_table = ''' CREATE TABLE IF NOT EXISTS recipes (
                                      id integer PRIMARY KEY,
                                      name text,
                                      type text,
                                      output_item_id integer,
                                      output_id_count integer,
                                      input_item_id_1 integer,
                                      input_count_1 integer,
                                      input_item_id_2 integer,
                                      input_count_2 integer,
                                      input_item_id_3 integer,
                                      input_count_3 integer,
                                      input_item_id_4 integer,
                                      input_count_4 integer,
                                      disciplines text
                                  ); '''

  # create a database connection
  conn = create_connection(database)
  if conn is not None:
      # create recipes table
      create_table(conn, sql_create_recipes_table)
  else:
      print("Error! cannot create the database connection.")

  with conn:
    add_recipe(conn, recipe_info)




# BELOW HAS COMPREHENSIVE ITEMS DATABASE STUFF ===================


def add_item(conn, item) :
    """
    Create a new item
    :param conn:
    :param item:
    :return:
    """

    data = """ INSERT INTO items(id, name, type, level, rarity)
              VALUES(?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(data, item)
    return cur.lastrowid


def sqlItem(item_info):
  database = r"C:\Users\Brennen\Desktop\python projects\gw2tp\gw2db.db"
  sql_create_items_table = ''' CREATE TABLE IF NOT EXISTS items (
                                      id integer PRIMARY KEY,
                                      name text,
                                      type text,
                                      level integer,
                                      rarity text
                                  ); '''

  # create a database connection
  conn = create_connection(database)
  if conn is not None:
      # create items table
      create_table(conn, sql_create_items_table)
  else:
      print("Error! cannot create the database connection.")

  with conn:
    add_item(conn, item_info)


def create_items_db() :
    url1 = 'https://api.guildwars2.com/v2/items?page='
    url2 = '&page_size='
    for page in range(0, 277) :
        print(page)
        r = requests.get(url1 + str(page) + url2 + str(200))
        info = json.loads(r.text)
        for item in range(0,len(info)) :
            c = info[item]
            name = c['name']
            #description = c['description']
            type = c['type']
            level = c['level']
            rarity = c['rarity']
            #vendor_value = c['vendor_value']
            id = c['id']
            #chat_link = c['chat_link']
            #icon = c['icon']
            temp_item = (id, name, type, level, rarity)
            sqlItem(temp_item)

# BELOW HAS TRADING POST HISTORY =====================================


def get_TP_info(conn, ids) :
    idList = []
    for i in ids:
        idList.append(str(i))
    idList = ','.join(idList)
    url = 'https://api.guildwars2.com/v2/commerce/prices?ids='
    r = requests.get(url + idList)
    info = json.loads(r.text)

    idItem = []
    buyQuantity = []
    buyPrice = []
    sellQuantity = []
    sellPrice = []
    items = []
    date = int(time.time())
    for i in range(0, len(info)) :
        idItem.append(info[i]['id'])
        buyQuantity.append(info[i]['buys']['quantity'])
        buyPrice.append(info[i]['buys']['unit_price'])
        sellQuantity.append(info[i]['sells']['quantity'])
        sellPrice.append(info[i]['sells']['unit_price'])
        temp_info = (idItem[i], buyQuantity[i], buyPrice[i], sellQuantity[i], sellPrice[i], date)
        #print(temp_info)
        add_post(conn, temp_info)


def add_post(conn, item) :
    """
    Create a new item
    :param conn:
    :param item:
    :return:
    """

    data = """ INSERT INTO tp_history(id, buys_quantity, buys_price, sells_quantity, sells_price, date)
              VALUES(?,?,?,?,?,?) """

    data2 = """ UPDATE tp_current
                SET buys_quantity = ?, buys_price = ?, sells_quantity = ?, sells_price = ?
                WHERE id = ? """

    item2 = (item[1], item[2], item[3], item[4], item[0])


    cur = conn.cursor()
    try :
        cur.execute(data, item)
        cur.execute(data2, item2)

    except :
        return
    return cur.lastrowid


def get_TP_update(ids):
  database = r"C:\Users\Brennen\Desktop\python projects\gw2tp\gw2db.db"
  sql_create_tp_table = ''' CREATE TABLE IF NOT EXISTS tp_history (
                                      id integer,
                                      buys_quantity integer,
                                      buys_price integer,
                                      sells_quantity integer,
                                      sells_price integer,
                                      date integer
                                  ); '''

  sql_create_tp2_table = ''' CREATE TABLE IF NOT EXISTS tp_current (
                                      id integer PRIMARY KEY,
                                      buys_quantity integer,
                                      buys_price integer,
                                      sells_quantity integer,
                                      sells_price integer,
                                      date integer
                                  ); '''

  # create a database connection
  conn = create_connection(database)
  if conn is not None:
      # create items table
      #create_table(conn, sql_create_tp_table)
      create_table(conn, sql_create_tp2_table)
  else:
      print("Error! cannot create the database connection.")

  with conn:
    get_TP_info(conn, ids)


def update() :
    print('updating database')
    leather =	[36752,	36783,	36818,	36842,	36867,	36891,	45804,	45778,	45791,	45830,	45765,	45817,	11879,	11795,	11837,	11963,	11753,	11921,	11876,	11792,	11834,	11960,	11750,	11918,	11877,	11793,	11835,	11961,	11751,	11919,	11881,	11797,	11839,	11965,	11755,	11923,	11878,	11794,	11836,	11962,	11752,	11920,	11880,	11796,	11838,	11964,	11754,	11922,	11882,	11798,	11840,	11966,	11756,	11924]
    armor =	[36887,	36860,	36839,	36806,	36774,	36746,	45635,	45662,	45648,	45674,	45622,	45609,	10705,	10719,	10712,	10726,	10698,	10691,	10702,	10716,	10709,	10723,	10695,	10688,	10703,	10717,	10710,	10724,	10696,	10689,	10704,	10718,	10711,	10697,	10707,	10721,	10714,	10728,	10700,	10693,	10706,	10720,	10713,	10727,	10699,	10692,	10708,	10722,	10715,	10729,	10701,	10694]
    craft =	[19746,	19736,	19709,	19747,	19735,	72194,	19684,	19880,	19881,	19882,	19883,	19884,	19885,	19886,	37176,	41555,	50366,	13219,	13221,	13222,	13223,	13224,	13225,	13226,	13227,	13228,	13229,	13230,	13220,	13150,	13151,	13147,	13149,	13148,	13158,	13152,	13153,	13154,	13155,	13156,	13157]
    gather = [19745,	19731,	19748,	19729,	19722,	19701,	19700,	19721,	24294,	24341,	24350,	24276,	24356,	24288,	24299,	24282,	76254,	70718,	24295,	24358,	24351,	24277,	24357,	24289,	24300,	24283,	82582,	83757,	83103,	83284,	86269]
    get_TP_update(leather + armor + craft + gather)

if __name__ == '__main__':
    leather =	[36752,	36783,	36818,	36842,	36867,	36891,	45804,	45778,	45791,	45830,	45765,	45817,	11879,	11795,	11837,	11963,	11753,	11921,	11876,	11792,	11834,	11960,	11750,	11918,	11877,	11793,	11835,	11961,	11751,	11919,	11881,	11797,	11839,	11965,	11755,	11923,	11878,	11794,	11836,	11962,	11752,	11920,	11880,	11796,	11838,	11964,	11754,	11922,	11882,	11798,	11840,	11966,	11756,	11924]
    armor =	[36887,	36860,	36839,	36806,	36774,	36746,	45635,	45662,	45648,	45674,	45622,	45609,	10705,	10719,	10712,	10726,	10698,	10691,	10702,	10716,	10709,	10723,	10695,	10688,	10703,	10717,	10710,	10724,	10696,	10689,	10704,	10718,	10711,	10697,	10707,	10721,	10714,	10728,	10700,	10693,	10706,	10720,	10713,	10727,	10699,	10692,	10708,	10722,	10715,	10729,	10701,	10694]
    craft =	[19746,	19736,	19709,	19747,	19735,	72194,	19684,	19880,	19881,	19882,	19883,	19884,	19885,	19886,	37176,	41555,	50366,	13219,	13221,	13222,	13223,	13224,	13225,	13226,	13227,	13228,	13229,	13230,	13220,	13150,	13151,	13147,	13149,	13148,	13158,	13152,	13153,	13154,	13155,	13156,	13157]
    gather = [19745,	19731,	19748,	19729,	19722,	19701,	19700,	19721,	24294,	24341,	24350,	24276,	24356,	24288,	24299,	24282,	76254,	70718,	24295,	24358,	24351,	24277,	24357,	24289,	24300,	24283,	82582,	83757,	83103,	83284,	86269]
    #get_TP_update(leather + armor + craft + gather)
