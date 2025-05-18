import random
# creating data structure, Queue
class Queue:
    def __init__(self):
        self.lst = []
        
    def Enqueue(self,item):
        self.lst.append(item)
    
    def Dequeue(self):
        return self.lst.pop(0)
    
    def is_empty(self):
        return not bool(self.lst)
    
    def size(self):
        return len(self.lst)
    
# starting the game
print("Welcome Traveler")

print("Ahead is a dangerous game \
    Where luck and fate will never be the same \
    The barrels spin and the choices fade, \
    Will you escape or be betrayed ?")

#defining game logic
def russian_roulette(names,num):
    game_queue = Queue()
    print("The stage has been set!")
    for i in names :
        game_queue.Enqueue(i)
    while game_queue.size()>1:
        for i in range(num):
            game_queue.Enqueue(game_queue.Dequeue())
        x=game_queue.Dequeue()
        print(f" oh you greedy soul {x}, you should have turned away, alas you are no more !")
    return game_queue.Dequeue()

number = int(input("How many of you dare to enter this game ? "))
print(f"I see , there are {number} of you, so lets start the death trials")
names_list = []
for i in range(number):
    temp = input(f"gambler of life no. {i+1}, I ask you , speak your name! ")
    names_list.append(temp)
bullets = random.randint(6,12)
print(f"Hmm , lets see how many bullets do i use ? \
    haahha, my special beauty, the infamous double barrel, {bullets} bullet gun ! \
    Your days are over you gamblers, you should have turned away, but your lust said otherwise!")

result = russian_roulette(names_list,number)

print(f"Rejoice {result}, for you have survived, but remember, Fate never lets anyone walk away twice.")
