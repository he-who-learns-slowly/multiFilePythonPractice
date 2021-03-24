def input_int(prompt):
    user_input = input(prompt+ " ")
    while(True):
        try:
            user_input = int(user_input)
            break
        except:
            print("Error, input must be an integer, please try again")
            user_input = input(prompt + " ")

    return user_input
