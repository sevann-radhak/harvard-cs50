class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):        
        return f'🍪' * self.cookies

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Amount of cookies to add must be a valid integer.")        
        
        if self.cookies + n > self.capacity:
            raise ValueError("Too many cookies.")
        
        self.cookies += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Amount of cookies to remove must be a valid integer.")        
        
        if self.cookies - n < 0:
            raise ValueError("Not enough cookies.")
        
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity
        
    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity

    @property
    def size(self):
        return self.cookies
        
