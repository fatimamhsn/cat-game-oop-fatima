from cat import Cat

print("Welcome to my cat game!")
name = input("Enter cat name: ")
colour =  input ('Enter colour: ')
my_cat = Cat(name,colour)

while True:
    action = input("""
What would yopu like to do?
1. Train                   
2. Feed
3. Play
4. Sleep                            
""")

    if action=='1':
        my_cat.train()
    elif action == '2':
        my_cat.feed()
    elif action=='3':
        my_cat.play()
    elif action == '4':
        my_cat.sleep()
        


