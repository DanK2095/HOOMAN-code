# define EuclidGCD()
def EuclidGCD(a,b):

    # if b is greater than a
    if b > a:    
        #then swap b and a values
        temp = a
        a = b
        b = temp
    #implement the Euclid GCD algorithum 
    while b != 0:
        temp = b
        b = a % b
        a = temp
        
    return a

#define Main() function
def main():

    #get user input for n
    N = int(input("please enter an integer that is greater than zero: "))
    #while N is wrong ( N needs to be greater than 0)
    while N < 0:
        #print error for N
        print("INVAILD INPUT: N must be greater than zero")
        #get new N
        N = int(input("please enter an integer that is greater than zero: "))

    #get user input for M
    M = int(input("please enter an integer that is greater than zero: "))
    #while M is wrong ( M needs to be greater than 0) M > 0
    while M < 0:
        #print error for M
        print("INVAILD INPUT: N must be greater than zero")
        #get new M
        M = int(input("please enter an integer that is greater than zero: "))

    # call EuclidGCD for calculations
    GCD = EuclidGCD(N,M)
    #print n and m values and their Greatest Common Divisor
    print("The N value was {}, The M value was {} and their Greatest Common Divisor is {}".format(N,M,GCD))

    return
    
main()
