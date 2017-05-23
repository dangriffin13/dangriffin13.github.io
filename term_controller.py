from term_models import System
from term_views import View


class Controller:
	def __init__(self):
		self.system = System()
		self.view = View() 

	def start(self):
		new_or_login = self.view.welcome()

		if new_or_login == 1:		
			launch = self.login()
		elif new_or_login == 2:
			launch = self.create_account()

		if launch == True:
			self.view.welcome_message()
			choice = 0
			while choice != 4:
				choice = self.view.main_menu(self.system.user)
				print("choice:", choice)
				if choice == 1:
					portfolio = self.system.get_holdings(self.system.user)
					self.view.show_holdings(portfolio)

				if choice == 2:
					self.view.price_check_title()
					ticker = None
					while ticker != "0":
						ticker = self.view.price_check()
						print("controller ticker:", ticker)
						if ticker == "0":
							break
						else:
							data = self.system.get_quote(ticker)
							# data = {'Name':'Apple', 'Symbol':'AAPL','LastPrice': 451.32}
							self.view.show_stock_quote(data)


				if choice == 3:
					self.view.trade_menu_title()
					trd_choice = None

					while trd_choice != "0":
						trd_choice = self.view.trade_menu()

						if trd_choice == "1":
							trd_order = self.view.buy()
							print("controller buy:", trd_order)
							execution = self.system.buy(self.system.user, trd_order)
							self.view.execution_msg(execution, "buy")
							
						if trd_choice == "2":
							trd_order = self.view.sell()
							print("sell", trd_order)
							execution = self.system.sell(self.system.user, trd_order)
							self.view.execution_msg(execution, "sell")

						if trd_choice == "3":
							portfolio = self.system.get_holdings(self.system.user)
							self.view.show_holdings(portfolio)

				if choice == 4:
					quit()

		else:
			print("We were unsuccessful in accessing your account.  Please try again.")


	def login(self):
		credentials = self.view.login()
		print("controller:", credentials)
		self.system.login(credentials)


	def create_account(self):
		failed = False
		valid_name = False

		while valid_name is False:
			username = self.view.new_username(failed)
			print("controller:", username)
			exists = self.system.check_username_exists(username)

			if exists:
				failed = True
			else:
				valid_name = True

		credentials = self.view.account_setup(username)

		launch = self.system.add_user(credentials)
		print("controller credentials:", credentials)

		if launch == True:
			return True


def main():
	controller = Controller()

	controller.start()


if __name__ == '__main__':
	main()