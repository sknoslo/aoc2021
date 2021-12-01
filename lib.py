def results(day, p1='--', p2='--'):
    if day < 10:
        print(f'--- day0{day} ---')
    else:
        print(f'--- day{day} ---')

    print('part01:', p1)
    print('part02:', p2)

    print('-------------')
