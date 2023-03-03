# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdasilva <jdasilva@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/03 13:17:23 by jdasilva          #+#    #+#              #
#    Updated: 2023/03/03 14:01:34 by jdasilva         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Account(object):
	
	ID_COUNT = 1
	
	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)
		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0
		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")
	def transfer(self, amount):
		self.value += amount

class Bank:
	def __init__(self):
		self.accounts = []
	def add(self, new_account):
		if not isinstance(new_account, Account):
			print("Tipo de cuenta no valida")
			return False
		if new_account.name in [account.name for account in self.accounts]:
			print(f"La cuenta {new_account.name} ya existe")
			return False
		if self.is_corrupted(new_account):
			return False
		self.accounts.append(new_account)
		print("Cuenta agregada")
		return True
	
	def transfer(self, origin_name, dest_name, amount):
		
		origin_account = self.get_account(origin_name)
		dest_account = self.get_account(dest_name)
		
		if amount < 0:
			print("Transacion no valida: no opuede ser negativo")
			return False
		
		if self.is_corrupted(origin_account) or self.is_corrupted(dest_name):
			print("Transacion no valida: cuentas corruptas")
			return False
		
		if amount >origin_account.value:
			print("Transacion no valida: fondos insuficientes")
			return False
		
		if origin_account == dest_account:
			print("Transacion valida")
			return True
		
		origin_account.value -= amount
		dest_name.value += amount
		print(f"Transacion valida: {amount}  tranferido de {origin_account} a {dest_name}")
		return True

	def get_account(self, name):
		for account in self.accounts:
			if account.name == name:
				return account
		return None
	
	def is_corrupted(self, account):
		if not account:
			return True

		attrs = dir(account)
		if len(attrs) % 2 == 0:
			return True
		
		for attr in attrs:
			if attr.startswith('b'):
				return True
			if attr.startswith('zip') or attr.startswith('addr'):
				return True
			if attr == 'name':
				if not isinstance(getattr(account, attr), str):
					return True
			elif attr == 'id':
				if not isinstance(getattr(account, attr), int):
					return True
			elif attr == 'value':
				if not isinstance(getattr(account, attr), (int, float)):
					return True

		return False
	
	def fix_account