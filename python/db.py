import os
import sys
import psycopg2

class MyDB:
	"""A class that handles all database operations. Uses psycopg2."""
	_db_connection = None
	_db_cur = None

	def __init__(self, db = "testdb", h = "localhost", p = "5432"):
		"""__init__ function initializes the connection and cursor variables."""
		self._db_connection = psycopg2.connect(dbname = db, host = h, port = p)
		self._db_cur = self._db_connection.cursor()

	def get_data(self, q):
		"""Execute query and get data from the database.
		Args:
			q (string): The SQL query string 
		Returns:
			r (list): A list of column names and query results
		"""
		cur = self._db_cur
		cur.execute(q)
		c = cur.description
		colnames = []
		for col in c:
			colnames.append(col[0])
		r = []
		r.append(colnames)
		r.append(cur.fetchall())
		self._db_connection.commit()
		cur.close()
		return r

	def __del__(self):
		"""__del__ function closes the connection."""
		self._db_connection.close()
