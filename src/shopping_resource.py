import pymysql

import os


class ShoppingResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        conn = pymysql.connect(
            user='dbuser',
            password='dbuserdbuser',
            host='database-1.cgeyeawignkd.us-east-1.rds.amazonaws.com',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM Cart.carts WHERE Cart.carts.cart_id =%s"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def get_by_item_id(key):

        sql = "SELECT * FROM Cart.items WHERE Cart.items.item_id=%s"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result