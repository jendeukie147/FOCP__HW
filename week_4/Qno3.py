def greet():
    username = str(input("Enter your name : "))
    uppercase = username[0].upper()+username[1:].lower()
    return uppercase

print(greet())