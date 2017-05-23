
import sqlite3
import requests

conn = sqlite3.connect('traders.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS users')

c.execute('''
		CREATE TABLE IF NOT EXISTS users(
		id INTEGER,
		username VARCHAR(30) UNIQUE,
		password VARCHAR(30),
		entitlements INTEGER,
		date_created DATE,
		date_updated DATE,
		PRIMARY KEY(id)
		)''')

c.execute('DROP TABLE IF EXISTS holdings')

c.execute('''
		CREATE TABLE IF NOT EXISTS holdings(
		id INTEGER,
		user_id INTEGER,
		asset_name VARCHAR(30),
		ticker VARCHAR(30),
		quantity NUMERIC,
		date_created DATE,
		date_updated DATE,
		PRIMARY KEY(id)
		)''')

print("table created")

init_cash = 100000

class System:

	def __init__(self):
		self.user = None
		self.portfolio_id = None
		

	def login(self, credentials):
		print("models:", credentials)

	def check_username_exists(self, username):
		print("models:", username)
		name_check = '''
					SELECT username from users
					WHERE username = ?
					'''
		c.execute(name_check, (username,))

		if not c.fetchone():
			return False

	def add_user(self, credentials):
		print("models add_user: ", credentials)
		print(*credentials)

		c.execute('''
					INSERT INTO users
					(username, password, entitlements, date_created, date_updated)
					VALUES
					(?, ?, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
			''', credentials
		)

		conn.commit()


		
		c.execute('''
					SELECT id from users
					WHERE username = ?
					''', (credentials[0],)
					)

		user_id = c.fetchone()

		print("add user port id", user_id)

		self.user = User(credentials[0], user_id[0])

		print("add user user created", self.user.name, self.user.user_id)

		c.execute('''
					INSERT INTO holdings
					(user_id, asset_name, ticker, quantity, date_created, date_updated)
					VALUES
					(?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
			''', (self.user.user_id, "Cash", "LIQUIDCASH", init_cash)
		)

		conn.commit()

		c.execute('''
					SELECT * from holdings
					WHERE user_id = ?
					''', (self.user.user_id,)
					)

		holdings = c.fetchall()

		print("holdings", holdings)

		c.execute('''
					SELECT quantity from holdings
					WHERE user_id = ?
					AND ticker = "LIQUIDCASH"
					''', (self.user.user_id,)
					)

		cash = c.fetchall()

		print("cash", cash, cash[0][0])

		self.user.cash = cash[0][0]

		return True


	def company_search(self, string):
		print(string)
		self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json"
		response = requests.get(self.lookup_url + "?input=" + string)
		print(response)
		
		if not response.json():
			return 0
		else:
			return response.json()


	def get_quote(self,string):
		print("get quote ticker", string)
		self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json"
		response = requests.get(self.quote_url + "?symbol=" + string)
		
		if response.json().get("Symbol") is None:
			return 0
		else:
			return response.json()


	def get_holdings(self, user):
		c.execute('''
					SELECT * from holdings
					WHERE user_id = ?
					''', (user.user_id,)
					)

		holdings = c.fetchall()
		print("models holdings:", holdings)

		holdings_w_mkt_val = []
		
		for row in holdings:
			print("current row", row)

			if row[3] == "LIQUIDCASH":
				px = 1
			else:
				px = self.get_quote(row[3])['LastPrice']
				print("price: ", px)
				

			new_row = []
			print("row: ", row)
			for i in range(2,5):
				new_row.append(row[i])
			print("new row: ", new_row)
			new_row.append(new_row[2]*px)
			print("new row w mkt val: ", new_row)

			holdings_w_mkt_val.append(new_row)
			print("holdings w mkt val: ", holdings_w_mkt_val)


		total = 0
		for row in holdings_w_mkt_val:
			total += row[3]
		print("Total Value: ", total)

		portfolio = {'holdings_w_mkt_val': holdings_w_mkt_val, 'total': total}

		return portfolio


	def buy(self, user, trd_order):
		data = self.get_quote(trd_order[0])
		print("data (json from markit): ", data)
		if data != 0:
			print("models json price", data['LastPrice'])
		
		if data == 0:
			execution = 0

		elif float(trd_order[1]) * data['LastPrice'] > user.cash:
			execution = False
		else: 
			user.cash -= float(trd_order[1]) * data['LastPrice']

			c.execute('''
					UPDATE holdings
					SET quantity = ?
					WHERE user_id = ?
					AND ticker = "LIQUIDCASH"
					''', (user.cash, user.user_id)
					)

			c.execute('''
					INSERT INTO holdings
					(user_id, asset_name, ticker, quantity, date_created, date_updated)
					VALUES
					(?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
					''', (user.user_id, data['Name'], data['Symbol'], trd_order[1])
					)

			conn.commit()

			execution = True

		return execution

	def sell(self, user, trd_order):

		print("sell trd_order: ", trd_order)
		print("user id: ", user.user_id, "data type: ", type(user.user_id))
		print("sell ticker: ", trd_order[0], "date type:", type(trd_order[0]))

		c.execute('''
					SELECT * from holdings
				'''
				)

		table = c.fetchall()
		print("entire table:", table)

		c.execute('''
					SELECT quantity from holdings
					WHERE user_id = ?
					AND ticker = ?
					''', (user.user_id, trd_order[0])
					)

		holdings = c.fetchall()
		print("holdings for sell:", holdings)

		qty_total = 0
		for row in holdings:
			qty_total += row[0]
		print("total qty for sale:", qty_total)
		new_qty = qty_total - float(trd_order[1])

		data = self.get_quote(trd_order[0])
		print("data from sell get_quote: ", data)
		if data != 0:
			print("price", data['LastPrice'])

		if float(trd_order[1]) > qty_total:
			execution = False

			print("execution after qty check: ", execution)

		elif data == 0:
			execution = 0

			print("execution after get_quote data check: ", execution)

		else: 
			user.cash += float(trd_order[1]) * data['LastPrice']

			c.execute('''
					UPDATE holdings
					SET quantity = ?
					WHERE user_id = ?
					AND ticker = "LIQUIDCASH"
					''', (user.cash, user.user_id)
					)

			conn.commit()

			c.execute('''
				UPDATE holdings
				SET quantity = ?
				WHERE user_id = ?
				AND ticker = ?
				''', (new_qty, user.user_id, trd_order[0])
				)

			conn.commit()

			execution = True

		print("execution: ", execution)
		return execution


class User:
	def __init__(self, name, user_id, cash=None):
		self.name = name
		self.user_id = user_id
		self.cash = cash


class Transaction:
	def __init__(self, user, asset, quantity):
		self.user = user
		self.asset = asset
		self.quantity = quantity

class Portfolio:
	def __init__(self, user):
		self.owner = user.name
		self.id = user.portfolio_id