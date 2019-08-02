class Animal:
    @classmethod
    def greet(cls):
        print("Hello")
        return 0

animal = Animal()  # Animalクラスのインスタンスを生成
print(animal)
print(Animal.greet())
