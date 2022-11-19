def greeting(): # Create function name greeting
    print("Welcome to piano cineplex!") 
    print("---------------------")
    print("Today's movie list.")
    print("1.Frozen")
    print("2.The Lion King")
    print("3.Toy story")
    print("4.Captain Marvel")
    print("5.Maleficent")
    return 

def movie_list(): # Create function name movie_list
    hallywood= ["1.Frozen",      # Create variable name hallywood and member of list index 0
                "2.The Lion King", # member of list index 1 
                "3.Toy story", # member of list index 2
                "4.Captain Marvel", # member of list index 
                "5.Maleficent"] # member of list index 3
    return hallywood
 
greeting() # call function 
movie = movie_list()  # call function stored in a variable name movie 
name_mov=input("Please enter your movie: ") # recive input stored in a variable name_mov
if name_mov=="1": 
    print(movie[0]) # display movie name Forzen
elif name_mov=="2": 
    print(movie[1]) # display movie name The Lion King
elif name_mov=="3":
    print(movie[2]) # display movie name Toy story 
elif name_mov=="4":
    print(movie[3]) # display movie name Captain Marvel
elif name_mov=="5":
    print(movie[4]) # display movie name Meleficent
else:
    print("No movie") # display "No Movie"
    try:
        value=int(name_mov)
    except ValueError:
        print('Error, this is not number!:')

