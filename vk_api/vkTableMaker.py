# -*- coding: utf-8 -*-
"""
    created by Sergey Troshin 3 May 2017.
"""
from tqdm import tqdm
from sql_connector import SQLConnector



class VkTableMaker:
    def __init__(self, title='Table with famous writers (example)', table_name='Writers',
                 params='Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25)', russian_keys=None, local=True, data=None):
        """
        title: what this table about
        table_name: what there is actual name of a table in database
        params: what table CREATE params do you want to add
        local: is it local database
        NOTE: if you want to connect to your server, you must set 'local' at True
        """
        self.sqlConnector = SQLConnector(local=local)
        self.title = title
        self.DATABASE = 'data2you1'
        self.table_name = '{0}.{1}'.format(self.DATABASE, table_name)
        self.params = params
        self.local = local
        self.data = None
        self.russian_keys=russian_keys

    def ask_yes(self, s):
        """
        :param s: string asking permission
        :return: True if person typed positive answer
        """
        print s + '\ny/n?'
        ans = raw_input()
        return ans in ['y', 'Y', 'YES', 'yes']

    def config(self):
        """
        to fix
        this function set params on database's table's column to add utf-8 on it
        allow us to use russian enconding in database
        need to use it after each table creation where exists russian text or other non'ascii symbols.
        :return: -
        """
        if not self.local and self.russian_keys != None:
            cur = self._get_cursor()
            for key_name in self.russian_keys:
                cur.execute(
                    "ALTER TABLE {0} MODIFY COLUMN {1} VARCHAR(255)  CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL".format(
                        self.table_name, key_name))

    def rewrite_table_if_exist(self):
        """
        actually can create new table instead of existing one
        requests a permission
        :return:
        """
        cur = self._get_cursor()
        querry = "CREATE DATABASE IF NOT EXISTS {0}".format(self.DATABASE)
        cur.execute(querry)
        # unf-8 provide
        if self.ask_yes("Do you want to rewrite table " + self.table_name + " with title " + self.title):
            cur.execute("DROP TABLE IF EXISTS {0}".format(self.table_name))
            cur.execute("CREATE TABLE {0}({1})".format(self.table_name, self.params))
        self.config()

    def _get_cursor(self):
        sql_c = self.sqlConnector
        sql_c.connect()
        return sql_c.con.cursor()

    def add_rows(self, data):
        if not type(data) is list:
            raise Exception("TypeError")
        # takes structure with data about a user and add all rows in table.
        cur = self._get_cursor()
        for person in tqdm(data):
            try:
                ALL_PARAMS = ','.join([key_ for key_ in person.kvp.keys()])
                ALL_VALUES = ','.join([person.kvp[key_] for key_ in person.kvp.keys()])
                querry = "INSERT INTO " + self.table_name + " (" + ALL_PARAMS + ") VALUES("  + ALL_VALUES + ')'
                cur.execute(querry)
            except:
                print('empty string')

    def SELECT_ALL(self):
        # get all data form a table
        cur = self._get_cursor()
        querry = "SELECT * FROM {0}".format(self.table_name)
        cur.execute(querry)
        return cur.fetchall()