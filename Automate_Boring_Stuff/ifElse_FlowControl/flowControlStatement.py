is_raining = input('Is it Raining? ')

if is_raining == 'Y':
    q1 = input('have umbrella? ')
    if q1 == "Y":
        print('Go outside')
    elif q1 == 'N':
        print('Wait a while')

elif is_raining == 'N':
    print('go outside')
