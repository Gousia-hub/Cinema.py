films = {
    "Harry Potter":[10,5],
    "Gravity":[12,2],
    "Incredibles 2":[5,8],
    "The Lion King":[9,2],
    }

while True:

    
    choice = (input("Wat film would u fancy to watch?: ")).strip().title()

    if choice in films:
        age = int(input("How old r u?: ").strip())

        if age >= films[choice][0]:
            

            num_seats = films[choice][1]

            if num_seats > 0:
                
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1

            else:
                print("Sorry we are sold out!")
            
        else:
            
            
            print("U probably r way too young for the film kiddo!   U can't fool me!!")
    else:
        print("We don't have that film...")
