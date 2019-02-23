names_list = ['Pedro', 'Henrique', 'João', 'Carlos', 'Paulinha', 'Marcos', 'Matheus', 'Montalvão', 'Ray']
#names_list = ['Pedro']

def print_names(names):
    for name in names:
        syze = len(name)
        if check_name(name, syze):
            print('The lenght of ' + name + ' is ' + str(syze))


def check_name(name, syze):
    is_valid = False
    has_n = 0
    for letter in name:
        if letter == 'n' or letter == 'N':
            has_n =+ 1
    if has_n > 0 and syze > 5:
        is_valid = True
    return is_valid

def empty_list(list):
    syze = len(list)
    for i in range(syze):
        list.pop()

print_names(names_list)
print(names_list)
empty_list(names_list)
print(names_list)