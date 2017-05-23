

class View:

	def welcome(self):
		new_or_login = None
		while new_or_login not in ["1", "2"]:
			print("Welcome to Grif Trader")
			print("Press 1 to login")
			print("Press 2 to create an acount")
			new_or_login = input()
		
		return int(new_or_login)

	def login(self):
		username = input("Enter your username: ")
		password = input("Enter your password: ")
		return (username, password)

	def new_username(self, failed):
		if failed:
			print("That name is taken.  Please select a different one.")
		else:
			print("Let's get you set up.")
			
		new_username = input("Pick your username: ")
		return new_username

	def account_setup(self, username):
		print("Congratulations.  Your username is: ", username)
		password1 = 0
		password2 = 1
		mismatch = False
		while password1 != password2:
			if mismatch == True:
				print("Your passwords didn't match.  Please try again.")
			password1 = input("Please choose your password: ")
			password2 = input("Please confirm your password: ")
			mismatch = True
		return (username, password1)

	def welcome_message(self):
		print("Welcome to Grif Trader") 

	def main_menu(self, user):
		print("menu user",user.name)
		# print("menu cash", user.cash)
		# menu_option = user.entitlement
		print("MAIN MENU")
		print("1. View Holdings")
		print("2. Check Stock Price")
		print("3. Execute Trade")
		print("4. Exit Grif Trader")

		choice = int(input("Select an option: "))

		while choice not in [1,2,3,4]:
			choice = input("Invalid choice.  Please choose 1-3: ")

		return choice

	def holdings_menu(self, user, holdings):
		print("Your Holdings")
		for row in holdings:
			print(row[2:5])
		end = input("Press any key to return to Main Menu")

	def price_check_title(self):
		print("PRICE CHECK")

	def price_check(self):
		print("Press 0 to return to the Main Menu")
		ticker = input("To view a price, enter the company's ticker: ")
		return ticker

	def show_stock_quote(self, data):
		print("Company", data['Name'])
		print("Ticker", data['Symbol'])
		print("Last Price", data['LastPrice'])

	def trade_menu_title(self):
		print("TRADE MENU")

	def trade_menu(self):
		print("Press 0 to return to the Main Menu")
		print("1. Buy")
		print("2. Sell")
		print("3. View Holdings")
		trd_choice = input("Choose an option: ")
		return trd_choice

	def buy(self):
		ticker = input("Enter the ticker to buy: ")
		qty = input("Enter the quantity you would like to buy: ")
		return ticker, qty


	def sell(self):
		ticker = input("Enter the ticker to sell: ")
		qty = input("Enter the quantity you would like to sell: ")
		return ticker, qty


	def show_holdings(self, portfolio):
		print("Your Holdings")
		for row in portfolio['holdings_w_mkt_val']:
			print(row)
		# total = 0
		# for row in holdings:
		# 	total += row[7]
		# 	print("row: ", row)
		# 	print(row[2:5]+[row[7]])
		print("Total Value: ", portfolio['total'])
		end = input("Press any key to return to Trade Menu")

	def execution_msg(self, execution, order_type):
		print("execution_msg execution value: ", execution)
		if execution == True:
			print("Congratulations.  Your trade was successful.")

		elif execution == 0:
			print("That's an invalid ticker.  Please try again.")

		elif execution == False:
			if order_type == "buy":
				print("You do not have sufficient cash for that order.")

			if order_type == "sell":
				print("You do not have enough shares for that order.")

			else:
				print("Your order did not execute.  Please try again.")

		else: 
			print("Something went wrong with your order.  Please contact us.")

		end = input("Press any key to return to Trade Menu.")

