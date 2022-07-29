class Pattern:
    def __init__(self):
       
        self.l = list()
        self.calc = 0
        self.lower_bound = int()
        self.upper_bound = int()
        self.incr = int()
        self.m = 55
        self.c = '-'
        self.input()

    def input(self):
        self.n = int(input("  Enter the degree of Polynomial:"))
        print(self.c*self.m)
        for i in range(self.n+1):
            temp = int(input(f"  -> Coeff {i + 1}: "))
            self.l.append(temp)
        
        print(self.c*self.m)

        self.lower_bound = int(input("  Provide lower bound for x: "))
        self.upper_bound = int(input("  Provide upper bound for x: "))
        self.incr = int(input("  Provide number of steps, you wish to increment x: "))
        self.l.reverse()
        
        print(self.c*self.m)
        self.print()
        print(self.c*self.m)

    
    def print(self):
        for i in range(self.lower_bound, self.upper_bound, self.incr):
            calc = 0
            print("| ", end="")
            for index, coeff in enumerate(self.l):
                calc += (i ** index) * coeff
            print("*"*int(calc))

def main():
    m = 55
    c = '-'
    print(c*m)
    print("|" + " "*13 + "POLYNOMIAL FUNCTOIN PROBLEM" + " "*13 + "|")
    print(c*m)
    print("|\t  Provide Polynomial Function Details:\t      |")
    print(c*m)


if __name__ == '__main__':
    main()
    Pattern()