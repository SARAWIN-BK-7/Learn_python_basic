def greeting():
    print("Welcome to piano cineplex!")
    print("---------------------")
    print("Today's movie list.")
    print("1.Frozen")
    print("2.The Lion King")
    print("3.Toy story")
    print("4.Captain Marvel")
    print("5.Maleficent")
    return 

def movie_list():
    hallywood= ["1.Frozen",
                "2.The Lion King",
                "3.Toy story",
                "4.Captain Marvel",
                "5.Maleficent"]
    return hallywood
 
greeting()
movie = movie_list() 
name_mov=input("Please enter your movie: ")
if name_mov=="1":
    print(movie[0])
elif name_mov=="2":
    print(movie[1])
elif name_mov=="3":
    print(movie[2])
elif name_mov=="4":
    print(movie[3])
elif name_mov=="5":
    print(movie[4])
else:
    print("No movie")
    try:
        value=int(name_mov)
    except ValueError:
        print('Error, this is not number!:')

