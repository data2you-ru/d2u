# -*- coding: utf-8 -*-
"""
    created by Sergei Troshin 3 May 2017.
"""
from config import SqlAWSinfo
import MySQLdb as sql
from config import SqlAWSinfo

class SQLConnector:
    """wrapper to mysql server connections
        Example:
        >>> sql_c.connect()
        >>> cur = sql_c.con.cursor()
        >>> cur.execute("INSERT INTO data2you1.Writers(Name) VALUES('Jack London')")
        >>> cur.close()
    """
    con = None
    def __init__(self, local=False, utf8=True):
        self.info = SqlAWSinfo()
        self.local = local
        self.utf8=utf8
        self.connections_count = 0
    def _on_start(self):
        if self.utf8:
            pass
    def connect(self):
        #start server form config.py
        if not self.local:
            info = SqlAWSinfo()
            self.con = sql.connect(
                host=info.HOST,
                user=info.USER,
                passwd=info.PASSWORD(),
                port=info.PORT,
            )
        else:
            # start local mysql mashine
            self.con = sql.connect(host='localhost', user='root', passwd='')
        if self.connections_count == 0:
            self._on_start()
        self.con.autocommit(on=True)
        cur = self.con.cursor()
        self.connections_count += 1
    def __del__(self):
        if not (self.con is None):
            self.con.close()