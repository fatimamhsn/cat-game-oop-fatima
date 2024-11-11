from cat import Cat

print("""Welcome to my cat game!
      
   |\---/|
   | ,_, |
    \_`_/-..----.
 ___/ `   ' ,""+ \ 
(__...'   __\    |`.___.';
  (_,...'(_,.`__)/'.....+
      
       """)

name = input("Enter cat name: ")
colour =  input ('Enter colour: ')
my_cat = Cat(name,colour)

while True:
    action = input("""
What would you like to do?
1. Train                   
2. Feed
3. Play
4. Sleep 
5. Show stats                           
""")

    if action=='1':
        my_cat.train()
        value = my_cat.check()
        if value == False:
            print("Your cat is too tired")
            break
    elif action == '2':
        my_cat.feed()
        value = my_cat.check()
        if value == False:
            print("Your cat is overweight")
            break        
    elif action=='3':
        my_cat.play()
        value = my_cat.check()
        if value == False:
            print("Your cat too tired")
            break
    elif action == '4':
        my_cat.sleep()
        value = my_cat.check()
        if value == False:
            print('Your cat died')
            break
    elif action=='5':
        my_cat.showstats()

    

        


