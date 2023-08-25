def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f'arg1: {arg1}')

def print_none():
    print('I got Nothing!!!!')

print_two('Timothy', 'Kamau')
print('-'*10)
print_two_again('Timothy', 'Kamau')
print('-'*10)
print_one("Timothy")
print('-'*10)
print_none()