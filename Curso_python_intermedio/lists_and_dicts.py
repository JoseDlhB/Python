

def run():
    my_list = [5,"Hello", True, 6.5] 
    my_dict = {'firstname': 'Jose','lastname': 'De la hoz'}

    super_list = [
        {'firstname': 'Jose','lastname': 'De la hoz'},
        {'firstname': 'Ana','lastname': 'Ballena'},
        {'firstname': 'Ketty','lastname': 'Moya'},
        {'firstname': 'Jander','lastname': 'Polo'},
        {'firstname': 'Diego','lastname': 'De la hoz'}
    ]

    super_dict = {
        'natural_num' : [1, 2, 3, 4, 5],
        'interger_num' : [-1, -2, 0, 2, 5],
        'floating_num' : [1.1, 3.3, 2.2, 4.7]
    }

    for key, value in super_dict.items():
        print(f'{key}, {value} ')
    
    print()
    
    for value in super_list:
        print(f'{value}')

if __name__ == '__main__':
    run()