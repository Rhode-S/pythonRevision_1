class Account():

	def __init__(self,owner,amount=0):
		self.owner = owner
		self.amount = amount

	def withdraw(self,withdraw_amount):
		if self.amount < withdraw_amount:
			print ('Funds unavailable')
			print()
		else:
			print (f'Successfully withdrawed {withdraw_amount}')
			self.amount -= withdraw_amount
			print (f'Balance : {self.amount}')
			print()

	def deposit(self,deposit_amount):
		self.amount += deposit_amount
		print ('Amount successfully deposited!')
		print (f'Updated available amount : {self.amount}')
		print()

	def __str__(self):
		return f'Owner : {self.owner} \nBalance : {self.amount} \n'

account1 = Account('Jeffrey',100)

print (account1)
account1.deposit(100)
account1.withdraw(150)
account1.withdraw(100)
