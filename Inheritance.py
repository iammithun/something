class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale")


class Fish(Animal):  # Fish inherits from Animal
    
    
    
    
    def swim(self):  # Corrected method name from 'swin' to 'swim'
        print("moving in water")


nemo = Fish()
nemo.swim()  # Output: moving in water





class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale")


class Fish(Animal):  # Fish inherits from Animal
    def __init__(self):
        super().__init__()
    
    
    
    def swim(self):  # Corrected method name from 'swin' to 'swim'
        print("moving in water")


nemo = Fish()
nemo.swim()  # Output: moving in water
nemo.breathe()





class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale")


class Fish(Animal):  # Fish inherits from Animal
    def __init__(self):
        super().__init__()
    
    
    
    def swim(self):  # Corrected method name from 'swin' to 'swim'
        print("moving in water")


nemo = Fish()
nemo.swim()  # Output: moving in water
nemo.breathe()
print(nemo.num_eyes)



class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale")


class Fish(Animal):  # Fish inherits from Animal
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater")
    
    
    
    def swim(self):  # Corrected method name from 'swin' to 'swim'
        print("moving in water")


nemo = Fish()
nemo.swim()  # Output: moving in water
nemo.breathe()
print(nemo.num_eyes)