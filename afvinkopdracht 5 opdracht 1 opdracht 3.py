def is_prime():
    getal = int(input('please enter a number'))
    y = 0
    z = 0
    if getal < 1:
        print(false)
    for x in range(2,getal):
        if getal%x == 0:
            y = 1
        else:
            z = 1
    if y == 1:
        print('false')
    else:
        print('true')
def main():
    is_prime()
main()
                
    
