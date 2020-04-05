list = [2, 45.3, (5+6j), 'text', ['12', 'text', 1], {1, 2, 3, 'text', '12'}, {'q':1, 2:'w'}, False, b'text',  None]
for i in list:
    print(f"{str(i):<25} | тип {type(i)}")