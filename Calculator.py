while True:
    num1 = float(input('Enter 1st num:'))
    num2 = float(input('Enter 2nd num:'))
    what = (input('''
             
             choices are
             Add,Sub,Multiply,Division
             What to do:
             ''')).lower()
 
    if what == 'add':
        print(num1+num2)
    elif what == 'sub':
        print(num1-num2)
    elif what == 'multiply':
        print(num1*num2)
    elif what == 'division':
        print(num1/num2)
    else:
        print('Try again')

    ans = input('Do you want to run it again(y/n)').lower()
    if ans == 'y':
        continue
    else:
        break

