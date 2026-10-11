
# for loop in range 3 printing meow 3 times
for i in range(3): 
    print("meow") 


# et cetera way to meow 
MEOWS = 3

for i in range(MEOWS): 
    print("meow")

# class way to meow 3 times: 
class Cat: 
    MEOWS = 3

    def meow(self): 
        for i in range(Cat.MEOWS): 
            print("meow")

cat = Cat()
cat.meow()