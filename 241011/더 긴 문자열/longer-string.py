string = input().split()
if len(string[0]) > len(string[1]):
    print(f'{string[0]} {len(string[0])}')
if len(string[0]) < len(string[1]):
    print(f'{string[1]} {len(string[1])}')
if len(string[0])==len(string[1]):
    print('same')