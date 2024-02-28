class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        
    def __str__(self) -> str:
        return f"Name: {self.name}, House: {self.house}"
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str) or len(name) < 1:
            raise ValueError("Invalid name.")
        self._name = name
        
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house.")
        self._house = house

    def print_student(self):
        print(f"Name: {self.name}, House: {self.house}")