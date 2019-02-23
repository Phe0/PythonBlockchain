my_name = 'Pedro'
my_age = 19

def print_my_data():
    print(my_name + "'s age is " + str(my_age))

def print_any_data(name, age):
    print(name + "'s age is " + str(age))

def calculate_decades_lived(age):
    decades = (age//10)
    return decades


print_my_data()
print_any_data(my_name, my_age)
print(calculate_decades_lived(my_age))