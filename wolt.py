from typing import Any
import random


class Wolt:
    clients_file = None
    service_providers_file = None
    clients = []
    service_providers = []
    clients_id = 0
    srvproviders_id = 0
    caccounts_ibans = set()
    srvaccounts_ibans = set()
    card_numbers = set()
    orders = {12, 34, 56}

    def __init__(self):
        self.client_parse_file()
        self.service_provider_parse_file()

    def client_parse_file(self):
        with open('Clients.txt', 'r') as self.clients_file:
            for s in self.clients_file:
                name = ''
                phone_number = ''
                password = ''
                name_filled = False
                phone_num_filled = False
                password_filled = False
                i = 0
                while i < len(s):
                    if s[i] == ':':
                        i += 2
                        while i < len(s) and s[i] != ' ':
                            if not name_filled:
                                name += s[i]
                            elif not phone_num_filled:
                                phone_number += s[i]
                            elif not password_filled:
                                password += s[i]
                            else:
                                pass
                            i += 1
                        if not name_filled:
                            name_filled = True
                        elif not phone_num_filled:
                            phone_num_filled = True
                        elif not password_filled:
                            password_filled = True
                    i += 1
                name = name.strip()
                phone_number = phone_number.strip()
                password = password.strip()
                client = Client(name, phone_number, password)
                print('Already existed client account:')
                print(f'name {name}, phone_number {phone_number}, password {password}')
                self.clients.append(client)

    def service_provider_parse_file(self):
        with open('ServiceProviders.txt', 'r') as self.service_providers_file:
            for s in self.service_providers_file:
                name = ''
                phone_number = ''
                password = ''
                name_filled = False
                phone_num_filled = False
                password_filled = False
                i = 0
                while i < len(s):
                    if s[i] == ':':
                        i += 2
                        while i < len(s) and s[i] != ' ':
                            if not name_filled:
                                name += s[i]
                            elif not phone_num_filled:
                                phone_number += s[i]
                            elif not password_filled:
                                password += s[i]
                            else:
                                pass
                            i += 1
                        if not name_filled:
                            name_filled = True
                        elif not phone_num_filled:
                            phone_num_filled = True
                        elif not password_filled:
                            password_filled = True
                    i += 1
                name = name.strip()
                phone_number = phone_number.strip()
                password = password.strip()
                service_provider = ServiceProvider(
                    name, phone_number, password)
                print('Already existed courier account:')
                print(f'name {name}, phone_number {phone_number}, password {password}')
                self.service_providers.append(service_provider)

    def add_clients(self, client):
        self.clients_file = open('Clients.txt', '+a')
        found = False
        for u in self.clients:
            if u.phone_number == client.phone_number:
                found = True
        if not found:

            card_number = random.randint(0, 100)
            while card_number in self.card_numbers:
                card_number = random.randint(0, 100)
            self.card_numbers.add(card_number)

            card = Card(card_number, '11/11/2043', 345, 'Visa')

            iban = random.randint(1, 100)
            while iban in self.caccounts_ibans:
                iban = random.randint(1.100)
            self.caccounts_ibans.add(iban)

            account = ClientAccount(iban, 0, 0, card)

            client.add_account(account)
            client.set_client_id(self.clients_id)
            self.clients.append(client)
            self.clients_file.write(str(client) + '\n')
            self.clients_id += 1
        else:
            print(f'Client with this {client.phone_number} Phone number already exist.')

        self.clients_file.close()

    def add_service_provider(self, service_provider):
        self.service_providers_file = open('ServiceProviders.txt', '+a')
        found = False
        for u in self.service_providers:
            if u.phone_number == service_provider.phone_number:
                found = True
        if not found:

            card_number = random.randint(101, 201)
            while card_number in self.card_numbers:
                card_number = random.randint(101, 201)
            self.card_numbers.add(card_number)

            card = Card(card_number, '10/10/2056', 123, 'Mastercard')

            iban = random.randint(101, 201)
            while iban in self.srvaccounts_ibans:
                iban = random.randint(101, 201)
            self.srvaccounts_ibans.add(iban)

            account = ServiceProviderAccount(iban, 0, 0, card)

            service_provider.add_account(account)
            service_provider.set_serviceprovider_id(self.srvproviders_id)
            self.service_providers.append(service_provider)
            self.service_providers_file.write(str(service_provider) + '\n')
            self.srvproviders_id += 1
        else:
            print(f'Service provider with this {service_provider.phone_number} already exist.')

        self.service_providers_file.close()

    def __repr__(self) -> str:
        return str(self.clients) + '\n' + str(self.service_providers)

    def login_client(self, phone_number, password):
        for u in self.clients:
            if u.phone_number == phone_number and u.password == password:
                return True
        return False

    def login_service_provider(self, phone_number, password):
        for u in self.service_providers:
            if u.phone_number == phone_number and u.password == password:
                return True
        return False

    def get_client(self, phone_number):
        for u in self.clients:
            if u.phone_number == phone_number:
                return u

    def get_service_provider(self, phone_number):
        for u in self.service_providers:
            if u.phone_number == phone_number:
                return u

    def add_order(self):
        order_number = random.randint(1, 1000)
        while order_number in self.orders:
            order_number = random.randint(1, 1000)
        self.orders.add(order_number)
        return order_number

    def erase_order(self, order):
        self.orders.remove(order)


class Client:
    client_id = 0
    name = ''
    phone_number = 0
    password = ''
    caccounts_id = 0
    orders = set()

    def __init__(self, name, phone_number, password) -> None:
        self.name = name
        self.phone_number = phone_number
        self.password = password
        self.accounts = []

    def add_account(self, account):
        found = False
        for acc in self.accounts:
            if acc.iban == account.iban:
                found = True
                break
        if not found:
            account.set_caccount_id(self.caccounts_id)
            self.accounts.append(account)
            self.caccounts_id += 1
        else:
            print(f'Account with this {account.iban} IBAN already exits.')

    def set_client_id(self, client_id):
        self.client_id = client_id

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f'Name is: {self.name} - Phone number is: {self.phone_number} - Password is: {self.password} - Account is: {self.accounts}'

    def get_balance(self):
        balance = 0
        for acc in self.accounts:
            balance += acc.balance
        return balance

    def add_money(self, iban, amount):
        account = None
        for acc in self.accounts:
            if acc.iban == iban:
                account = acc
                break
        if account == None:
            print(f'No such account with {iban} IBAN.')
        else:
            account.set_balance(account.get_balance() + amount)

    def get_account(self, iban):
        for acc in self.accounts:
            if acc.iban == iban:
                return acc
        return None


class ServiceProvider:
    srvprovider_id = 0
    name = ''
    phone_number = 0
    password = ''
    srvaccounts_id = 0
    orders = set()

    def __init__(self, name, phone_number, password) -> None:
        self.name = name
        self.phone_number = phone_number
        self.password = password
        self.accounts = []

    def add_account(self, account):
        found = False
        for acc in self.accounts:
            if acc.iban == account.iban:
                found = True
                break
        if not found:
            account.set_sraccount_id(self.srvaccounts_id)
            self.accounts.append(account)
            self.srvaccounts_id += 1
        else:
            print(f'Account with this {account.iban} already exists.')

    def set_serviceprovider_id(self, srvprovider_id):
        self.srvprovider_id = srvprovider_id

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self):
        return f'Name is: {self.name} - Phone number is: {self.phone_number} - Password is: {self.password} - Account is: {self.accounts}'

    def get_balance(self):
        balance = 0
        for acc in self.accounts:
            balance += acc.balance
        return balance

    def add_money(self, iban, amount=0):
        account = None
        for acc in self.accounts:
            if acc.iban == iban:
                account = acc
                break
        if account == None:
            print(f'No such account with {iban} IBAN.')
        else:
            account.set_balance(account.get_balance() + amount)

    def withdraw_money(self, iban, amount):
        account = None
        for acc in self.accounts:
            if acc.iban == iban:
                account = acc
                break
        if account == None:
            print(f'No such account with {iban} IBAN.')
        else:
            if account.get_balance() >= amount:
                account.set_balance(account.get_balance() - amount)
                print('\n')
                print(f"You have successfully withdrawn {amount} lari.")
                print('\n')
            else:
                print('\n')
                print("You don't have enough money to withdraw!")
                print('\n')

    def get_account(self, iban):
        for acc in self.accounts:
            if acc.iban == iban:
                return acc
        return None


class ClientAccount:
    caccount_id = 0
    iban = 0
    deposit = 0
    balance = 0
    card = None

    def __init__(self, iban, deposit, balance, card) -> None:
        self.iban = iban
        self.deposit = deposit
        self.balance = balance
        self.card = card

    def set_caccount_id(self, caccount_id):
        self.caccount_id = caccount_id

    def __repr__(self) -> str:
        return f'Card IBAN: {self.iban} - Balance: {self.balance} - Card: {self.card}'

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance


class ServiceProviderAccount:
    srvaccount_id = 0
    iban = 0
    deposit = 0
    balance = 0
    card = None

    def __init__(self, iban, deposit, balance, card) -> None:
        self.iban = iban
        self.deposit = deposit
        self.balance = balance
        self.card = card

    def set_sraccount_id(self, sraccount_id):
        self.srvaccount_id = sraccount_id

    def __repr__(self) -> str:
        return f'Card IBAN: {self.iban} - Balance: {self.balance} - Card: {self.card}'

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance


class Card:
    card_number = 0
    valid_through = ''
    cvv = 0
    issuer = ''

    def __init__(self, card_number, valid_through, cvv, issuer) -> None:
        self.card_number = card_number
        self.valid_through = valid_through
        self.cvv = cvv
        self.issuer = issuer

    def __repr__(self) -> str:
        return f'Card number: {self.card_number} - Valid Through: {self.valid_through} - CVV: {self.cvv} - Issuer: {self.issuer}'


wolt = Wolt()

inside_wolt = True
while inside_wolt:
    print('\n')
    print('Hi!, Welcome to Wolt.')
    print('\n')
    print('if you are Client type: 1 \
          if you are Courier type: 2 \
          if you want to exit type: 3')

    inp = int(input())

    if inp == 1:
        inside_client = True
        while inside_client:
            print('Register new client type: 1 \
                   Login as client type: 2 \
                   Exit type: 3')
            inp1 = int(input())
            if inp1 == 1:
                inp_name = input('Enter your name: ')
                inp_phone_number = input('Enter your phone number: ')
                inp_password = input('Enter your password: ')
                new_client = Client(inp_name, inp_phone_number, inp_password)
                wolt.add_clients(new_client)
                print('\n')
                print('Now, you should login as a client.')
                print('\n')
            elif inp1 == 2:
                inp_phone_number = input('Enter your phone number: ')
                inp_password = input('Enter your password: ')
                if wolt.login_client(inp_phone_number, inp_password):
                    print('\n')
                    print("You have sucessfully logged in.")
                    print(f'Your IBAN is {wolt.caccounts_ibans}')
                    print('\n')
                    logged_in = True
                    while logged_in:
                        client = wolt.get_client(inp_phone_number)
                        print('Check balance type: 1 \
                            Order something type: 2 \
                            Add money to balance type: 3 \
                            Exit type: 4')
                        inp11 = int(input())
                        if inp11 == 1:
                            print(f'Your balance is {client.get_balance()}')
                        elif inp11 == 2:
                            if client.get_balance() > 0:
                                input('Please, place your order: ')
                                order = wolt.add_order()
                                print('\n')
                                print(f'Thank you, your order {order} is being prepared and will be delivered in 40-45 minutes! :)')
                                print('\n')
                            else:
                                print('\n')
                                print(
                                    'Sorry, your balance is not enough to order. Please add money to your balance!')
                                print('\n')
                        elif inp11 == 3:
                            iban = int(
                                input('Please, provide IBAN to make deposit: '))
                            amount = int(
                                input('How much money are you adding '))
                            client.add_money(iban, amount)
                            account = client.get_account(iban)
                            if account == None:
                                print(f'No account found with this {iban} IBAN.')
                            else:
                                print(f'New balance is {account.get_balance()}')
                        elif inp11 == 4:
                            print('\n')
                            print('You have logged out from client account.')
                            print('\n')
                            logged_in = False
                        else:
                            print('\n')
                            print("Invalid input!, please re-enter input.")
                else:
                    print('\n')
                    print('Ivalid input!')
                    print('\n')
            elif inp1 == 3:
                print('\n')
                print('You have sucessfully logged out from client account!')
                print('\n')
                inside_client = False
            else:
                print('\n')
                print('Such Client does not exist!')
                print('\n')

    elif inp == 2:
        inside_service_provider = True
        while inside_service_provider:
            print('Register new courier type: 1 \
                   Login as a courier type: 2 \
                   Exit type: 3')
            inp2 = int(input())
            if inp2 == 1:
                inp_name = input('Enter your name: ')
                inp_phone_number = input('Enter your phone number: ')
                inp_password = input('Enter your password: ')
                new_service_provider = ServiceProvider(
                    inp_name, inp_phone_number, inp_password)
                wolt.add_service_provider(new_service_provider)
                print('\n')
                print('Now, you should login as a courier.')
                print('\n')
            elif inp2 == 2:
                inp_phone_number = input('Enter your phone number: ')
                inp_password = input('Enter your password: ')
                if wolt.login_service_provider(inp_phone_number, inp_password):
                    print('\n')
                    print("You have sucessfully logged in.")
                    print(f'Your IBAN is {wolt.srvaccounts_ibans}')
                    print('\n')
                    logged_in = True
                    while logged_in:
                        service_provider = wolt.get_service_provider(
                            inp_phone_number)
                        print('Check balance type: 1 \
                            Deliver orders type: 2 \
                            Withdraw money type 3 \
                            Exit type: 4')
                        inp11 = int(input())
                        if inp11 == 1:
                            print(f'Your balance is {service_provider.get_balance()}')
                        elif inp11 == 2:
                            print(
                                'With delivering each order, your balance will increase by 5 Lari.')
                            print(wolt.orders)
                            if len(wolt.orders) == 0:
                                print(
                                    'There is no orders to be delivered, please wait a bit.')
                            else:
                                order = int(
                                    input('Please enter which order you are going deliver: '))
                                wolt.erase_order(order)
                                iban = int(
                                    input('Please, provide IBAN to make deposit: '))
                                service_provider.add_money(iban, amount=5)
                                account = service_provider.get_account(iban)
                            if account == None:
                                print(f'No account found with this {iban} IBAN.')
                            else:
                                print(f'Your balance is {account.get_balance()}')
                        elif inp11 == 3:
                            iban = int(
                                input('Please, provide IBAN to withdraw money: '))
                            amount = int(
                                input('How much money are you withdrawing ? '))
                            service_provider.withdraw_money(iban, amount)
                            account = service_provider.get_account(iban)
                            if account == None:
                                print(f'No account found with this {iban} IBAN.')
                            else:
                                print(f'Your balance is {account.get_balance()}')
                        elif inp11 == 4:
                            print('\n')
                            print('You have logged out from courier account.')
                            print('\n')
                            logged_in = False
                        else:
                            print('\n')
                            print("Invalid input!, please re-enter input.")
                            print('\n')
                else:
                    print('\n')
                    print('Ivalid input!')
                    print('\n')
            elif inp2 == 3:
                print('\n')
                print('You have sucessfully logged out from courier account!')
                print('\n')
                inside_service_provider = False
            else:
                print('\n')
                print('Such courier account does not exist!')
                print('\n')
    elif inp == 3:
        print('\n')
        print('You no longer have access to wolt application!')
        break
    else:
        print('\n')
        print("Invalid input!, please re-enter input.")
        print('\n')
