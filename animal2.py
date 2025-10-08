class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

if __name__ == "__main__":
    generic_animal = Animal()
    dog = Dog()
    cat = Cat()

    generic_animal.speak()  
    dog.speak()             
    cat.speak()             
