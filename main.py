class Shark:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

    def swim(self):
        print("the shark is swiming")

    def eat(self):
        print("the shark is eating")

def main():
    x = Shark('yossi','4','blue')
    x.swim()
    x.eat()
    print(x.name)

main()

print("hi")
print("yes")
