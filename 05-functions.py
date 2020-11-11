def greeter_message(user, age):
    print("Hello " + user + ", you are " + str(age))

def is_adult(age):
    if isinstance(age, int): # check if param is an int
        if age < 18:
            return False
        else:
            return True
    else:
        return False

greeter_message("Jock", 22)
greeter_message("Spike", 35)

print(is_adult(10))
print(is_adult(22))
print(is_adult("Hello"))
