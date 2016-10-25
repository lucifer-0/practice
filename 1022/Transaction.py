import pickle


class Transaction():
    def __init__(self, amount, date, currency="USD", usd_conversion_rate=1, description=None):
        """
        >>> t = Transaction(100, "2008-12-09")
        >>> t.amount, t.currency, t.usd, t.usd_conversion_rate
        (100, 'USD', 100, 1)
        """
        self.__amount = amount
        self.__date = date
        self.__currency = currency
        self.__usd_conversion_rate = usd_conversion_rate
        self.__description = description


    @property
    def amount(self):
        return self.__amount


    @property
    def date(self):
        return self.__date


    @property
    def currency(self):
        return self.__currency


    @property
    def usd_conversion_rate(self):
        return self.__usd_conversion_rate


    @property
    def description(self):
        return self.__description


    @property
    def usd(self):
        return self.__amount * self.__usd_conversion_rate


class Account():
    """
    >>> import os
    >>> import tempfile
    >>> name = os.path.join(tempfile.gettempdir(), "account01")
    >>> account = Account(name, "Qtrac Ltd.")
    >>> os.path.basename(account.number), account.name,
    ('account01', 'Qtrac Ltd.')
    >>> account.balance, account.all_usd, len(account)
    (0.0, True, 0)
    >>> account.apply(Transaction(100, "2008-11-14"))
    >>> account.apply(Transaction(150, "2008-12-09"))
    >>> account.apply(Transaction(-95, "2009-01-22"))
    >>> account.balance, account.all_usd, len(account)
    (155.0, True, 3)
    >>> account.apply(Transaction(50, "2008-12-09", "EUR", 1.53))
    >>> account.balance, account.all_usd, len(account)
    (231.5, False, 4)
    >>> account.save()
    >>> newaccount = Account(name, "Qtrac Ltd.")
    >>> newaccount.balance, newaccount.all_usd, len(newaccount)
    (0.0, True, 0)
    >>> newaccount.load()
    >>> newaccount.balance, newaccount.all_usd, len(newaccount)
    (231.5, False, 4)
    >>> try:
    ...     os.remove(name + ".acc")
    ... except EnvironmentError:
    ...     pass
    """
    def __init__(self, number, name):
        """
        Create a new Account with the given number and name

        the number is used as the filename
        """
        self.__number = number
        self.__name = name
        self.__transactions = []


    @property
    def number(self):
        "The read only account number"
        return self.__number


    @property
    def name(self):
        """
        The account's name

        This can be changed since it is only human convenience;
        the account number is the true identifier
        """
        return self.__name


    @name.setter
    def name(self, name):
        assert len(name) > 3, "account name must be at least 4 characters"
        self.__name = name


    def __len__(self):
        "Return the number of transactions"
        return len(self.__transactions)
    
    
    @property
    def balance(self):
        """
        Return the balance in USD
        """
        total = 0.0
        for transaction in self.__transactions:
            total += transaction.usd
        return total


    @property
    def all_usd(self):
        """
        Return True if all transaction are USD
        """
        for transaction in self.__transactions:
            if transaction.currency != "USD":
                return False
        return True
 

    def apply(self, transaction):
        """
        Apply (adds) the given transaction to the account
        """
        self.__transactions.append(transaction)
    

    def save(self):
        """
        Save the account's data in number.acc
        """
        fh = None
        try:
            data = [self.number, self.name, self.__transactions]
            fh = open(self.number + ".acc", "wb")
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()


    def load(self):
        """
        Load the account's data from number.acc

        All previous data is lost
        """
        fh = None
        try:
            fh = open(self.number + ".acc", "rb")
            data = pickle.load(fh)
            assert self.number == data[0], "account number doesn't match"
            self.name, self.__transactions = data[1:]
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
