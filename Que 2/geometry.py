class _2D_:
    def __init__(self) -> None:
        self.pi = 22/7          # Pi Value π
        self.n = 50             # Number of Spaces
        self.char = '-'         # Character for the Designing
        left = 0
        right = 0
        self.p = int()          # Variable for Perimeter
        self.a = int()          # Variable for Area
        self.list = [
            'Square',
            'Rectangle',
            'Rhombus',
            'Parallelogram',
            'Circle',
            'Exit'
        ]
        self.dict = {
            1 : self.square,
            2 : self.rectangle,
            3 : self.rhombus,
            4 : self.parallelogram,
            5 : self.circle,
            6 : exit
        }

        print("|\t   You have selected 2D shapes !\t |")
        print(self.char*self.n)

        # Menu
        print(f"  1. {self.list[0]}\n  2. {self.list[1]}\n  3. {self.list[2]}\n  4. {self.list[3]}\n  5. {self.list[4]}\n  6. {self.list[5]}")
        
        print(self.char*self.n)

        # Taking input from the User.
        choice = int(input("  Enter your choice : "))
        if choice  == 6:
            print(self.char*self.n)
            exit()
        print(self.char*self.n)

        # Heading like Square, Rectangle etc.
        try:
            temp = 48 - len(self.list[choice - 1])
        except:
            print("|\t\t     Try again !\t\t |")
            print(self.char*self.n)
            exit()
        if temp % 2 != 0:
            right  = 1
        left += temp // 2
        right += temp // 2
        print("|" + " "*left + self.list[choice - 1] + " "*right + "|")

        # Calling the particular function according to the given input by the User using the above Dictonary "self.dict".
        self.dict[choice]()

        # Rounding off all the values upto two decimal places.
        self.p = round(self.p, 2)
        self.a = round(self.a, 2)

        # priting the value of Perimeter and Area stored in two variable i.e. "self.p" and "self.a".
        print(f"| -> The Perimeter of {self.list[choice - 1]} is : {self.p}"+ " "*(15 - len(str(self.p))) +"|")
        print(f"| -> The Area of {self.list[choice - 1]} is      : {self.a}"+ " "*(15 - len(str(self.a))) +"|")
        print(self.char*self.n)

    # This function calculates the Perimeter and Area of the Square.
    def square(self):
        print(self.char*self.n)
        try:
            s = int(input("  Enter Side : "))       # Taking Side as an input from User.
        except:
            print("|\t\t     Try again !\t\t |")
            print(self.char*self.n)
            exit()
        print(self.char*self.n)
        self.p = 4 * s      # Formula of Perimeter of Sqaure = 4(Side)
        self.a = s * s      # Formula of Area of Square = Side * Side

    # This function calculates the Perimeter and Area of the Rectangle.
    def rectangle(self):
        try:
            l = int(input("  Enter length : "))     # Taking length as an input from User.
            b = int(input("  Enter Breadth : "))    # Taking breadth as an input from User.
        except:
            print("|\t\t     Try again !\t\t |")
            print(self.char*self.n)
            exit()
        self.p = 2 * (l + b)        # Formula of Perimeter of Rectangle = 2(length + breadth)
        self.a = l * b              # Formula of Area of Rectangle = length * breadth

    # This function calculates the Perimeter and Area of the Rhombus.
    def rhombus(self):
        try:
            a = int(input("Enter side : "))                 # Taking Side as an input from User.
            d1 = int(input("Enter Diagonal 1 : "))          # Taking Diagonal 1 as an input from User.
            d2 = int(input("Enter Diagonal 2: "))           # Taking Diagonal 2 as an input from User.
        except:
            print("|\t\t     Try again !\t\t |")
            print(self.char*self.n)
            exit()
        self.p = 4 * a                                      # Formula of Perimeter of Rhombus = 4*Side
        self.a = (d1 * d2)/2                                # Formula of Aera of Rhombus = (Diagonal1 * Diagonal2)/2

    # This function calculates the Perimeter and Area of the Parallelogram.
    def parallelogram(self):
        try:
            l = int(input("Enter length : "))               # Taking length as an input from User.
            b = int(input("Enter Breadth : "))              # Taking breadth as an input from User.
            h = int(input("Enter height : "))               # Taking height as an input from User.
        except:
            print("|\t\t     Try again !\t\t |")
            print(self.char*self.n)
            exit()
        self.p = 2 * (l + b)                                # Formula of Perimeter of Parallelogram = 2(length + breadth)
        self.a = b * h                                      # Formula of Area of Parallelogram = breadth * height

    # This function calculates the Perimeter and Area of the Circle.
    def circle(self):
        try:
            r = int(input("Enter radius : "))               # Taking radius as an input from User.
        except:
            print("|\t\t     Try again !\t\t |")
            print(self.char*self.n)
            exit()
        self.p = 2 * self.pi * r                            # Formula of Perimeter of Circle = 2πr
        self.a = self.pi * r * r                            # Formula of Area of Circle = π(r)^2


class _3D_:
    def __init__(self) -> None:
        self.pi = 22/7                                  # pi value π
        self.n = 50                                     # Number of spaces
        self.char = '-'                                 # Character for the Designing
        self.csa = int()                                # Variable for Curved Surface Area 
        self.tsa = int()                                # Variable for Total Surface Area
        self.vol = int()                                # Variable for Volume
        left = 0
        right = 0
        self.list = [
            'Cube', 
            'Cuboid', 
            'Right Circular Cone', 
            'Hemisphere', 
            'Sphere', 
            'Solid Cylinder', 
            'Hollow Cylinder',
            'Exit'
            ]

        self.dict = {
            1 : self.cube,
            2 : self.cuboid,
            3 : self.right_circular_cone,
            4 : self.hemisphere,
            5 : self.sphere,
            6 : self.solid_cylinder,
            7 : self.hollow_cylinder,
            8 : exit
        }

        # Menu
        print("|          You have selected 3D shapes !         |")
        print(self.char*self.n)
        print(f"  1. {self.list[0]}\n  2. {self.list[1]}\n  3. {self.list[2]}\n  4. {self.list[3]}\n  5. {self.list[4]}\n  6. {self.list[5]}\n  7. {self.list[6]}\n  8. {self.list[7]}")
        
        # Taking input from the User.
        print(self.char*self.n)
        choice = int(input("  Enter your choice : "))
        if choice == 8:
            print(self.char*self.n)
            exit()
        print(self.char*self.n)

        # Heading like Square, Rectangle etc.
        try:
            temp = 48 - len(self.list[choice - 1])
        except:
            print("|\t\t     Try again !\t\t |")
            print(self.char*self.n)
            exit()
        if temp % 2 != 0:
            right  = 1
        left += temp // 2
        right += temp // 2
        print("|" + " "*left + self.list[choice - 1] + " "*right + "|")
        print(self.char*self.n)

        # Calling the particular function according to the given input by the User using the above Dictonary "self.dict".
        self.dict[choice]()
        print(self.char*self.n)

        # Rounding off all the values upto two decimal places.
        self.csa = round(self.csa, 2)
        self.tsa = round(self.tsa, 2)
        self.vol = round(self.vol, 2)

        # Priting the value of CSA, TSA and Volume stored in three variable i.e. "self.csa", "self.tsa", and "self.vol".
        print(f"|  -> CSA of {self.list[choice - 1]} is    : {self.csa}" + " "*(12 - len(str(self.csa))) + "|")
        print(f"|  -> TSA of {self.list[choice - 1]} is    : {self.tsa}" + " "*(12 - len(str(self.tsa))) + "|")
        print(f"|  -> Volume of {self.list[choice - 1]} is : {self.vol}" + " "*(12 - len(str(self.vol))) + "|")
        print(self.char*self.n)

    # This function calculates the CSA, TSA and VOLUME of the Cube.
    def cube(self):
        try:
            s = int(input("  Enter side : "))                   # Taking Side as an input from User.
        except:
            print("|\t\t     Try again !\t\t |")
            print(self.char*self.n)
            exit()
        self.csa = 4 * s * s                                    # Formula of CSA of Cube = 4(Side)^2
        self.tsa = 6 * s * s                                    # Formula of TSA of Cube = 6(Side)^2
        self.vol = s ** 3                                       # Formula of Vol of Cube = Side^3

    # This function calculates the CSA, TSA and VOLUME of the Cuboid.
    def cuboid(self):
        try:
            l = int(input("  Enter length : "))                         # Taking length as an input from User.
            b = int(input("  Enter Breadth : "))                        # Taking breadth as an input from User.
            h = int(input("  Enter height : "))                         # Taking height as an input from User.
        except:
            print("|\t\t     Try again !\t\t |")
            print(self.char*self.n)
            exit() 
        self.csa = 2 * (l + b) * h                                      # Formula of CSA of Cuboid = 2(l+b)h
        self.tsa = 2 * (l * b + b * h + h * l)                          # Formula of TSA of Cuboid = 2(lb+bh+hl)
        self.vol = l * b * h                                            # Formula of Vol of Cuboid = lbh

    # This function calculates the CSA, TSA and VOLUME of the Right Circular Cone.
    def right_circular_cone(self):
        try:
            l = int(input("  Enter slant height : "))                   # Taking length as an input from User.
            r = int(input("  Enter radius : "))                         # Taking radius as an input from User.
            h = int(input("  Enter height : "))                         # Taking height as an input from User.
        except:
            print("|\t\t     Try again !\t\t |")
            print(self.char*self.n)
            exit()
        self.csa = self.pi * r * l                                      # Formula of CSA of Right Circular Cone = πrl
        self.tsa = self.pi * r * (r + l)                                # Formula of TSA of Right Circular Cone = πr(r+l)
        self.vol = (self.pi * (r * r) * h) / 3                          # Formula of Vol of Right Circular Cone = (1/3) π(r^2)h

    # This function calculates the CSA, TSA and VOLUME of the Hemisphere.
    def hemisphere(self):
        try:
            r = int(input("  Enter radius : "))                         # Taking radius as an input from User.
        except:
            print("|\t\t     Try again !\t\t |")
            print(self.char*self.n)
            exit()
        self.csa = 2 * self.pi * r * r                                  # Formula of CSA of Hemisphere = 2π(r^2)
        self.tsa = 3 * self.pi * r * r                                  # Formula of TSA of Hemisphere = 3π(r^2)
        self.vol = (2 * (self.pi * (r ** 3)))/3                         # Formula of Vol of Hemisphere = (2/3) π(r^3)

    # This function calculates the CSA, TSA and VOLUME of the Sphere.
    def sphere(self):
        try:
            r = int(input("  Enter radius : "))                         # Taking radius as an input from User.
        except:
            print("|\t\t     Try again !\t\t |")
            print(self.char*self.n)
            exit()
        self.csa = 4 * self.pi * r * r                                  # Formula of CSA of Sphere = 4π(r^2)
        self.tsa = 4 * self.pi * r * r                                  # Formula of TSA of Sphere = 4π(r^2)
        self.vol = (4 * (self.pi * (r ** 3)))/3                         # Formula of Vol of Sphere = (4/3) π(r^3)

    # This function calculates the CSA, TSA and VOLUME of the Solid Cylinder.
    def solid_cylinder(self):
        try:
            r = int(input("  Enter radius : "))                         # Taking radius as an input from User.
            h = int(input("  Enter height : "))                         # Taking height as an input from User.
        except:
            print("|\t\t     Try again !\t\t |")
            print(self.char*self.n)
            exit()
        self.csa = 2 * self.pi * r * h                                  # Formula of CSA of Solid Cylinder = 2πrh
        self.tsa = 2 * self.pi * r * (h + r)                            # Formula of TSA of Solid Cylinder = 2πr(r+h)
        self.vol = self.pi * (r ** 2) * h                               # Formula of Vol od Solid Cylinder = π(r^2)h

    # This function calculates the CSA, TSA and VOLUME of the Hollow Cylinder.
    def hollow_cylinder(self):
        try:
            r1 = int(input("  Enter radii r : "))                       # Taking Radius1 (r) as an input from User.
            r2 = int(input("  Enter radii R : "))                       # Taking Radius2 (R) as an input from User.
            h = int(input("  Enter height  : "))                        # Taking height as an input from User.         
        except:
            print("|\t\t     Try again !\t\t |")
            print(self.char*self.n)
            exit()    
        self.csa = 2 * self.pi * h * (r1 * r2)                          # Formula of CSA of Hollow Cylinder = 2πh(r+R)
        self.tsa = 2 * self.pi * h * (r1 + r2) + 2 * self.pi * ((r2 * r2) - (r1 * r1) )                 # Formula of TSA of Hollow Cylinder = 2πh(r+R)+2π( R^2 + r^2 )
        self.vol = self.pi * ((r2 * r2) - (r1 * r1)) * h                # Formula of VOL of Hollow Cylinder = π( R^2 - r^2 )h

def main_menu():
    n = 50                                                              # Number of Spaces
    char = '-'                                                          # Character for the Designing
    print(char*n)
    print("|\t\t\tMENU\t\t\t |")
    print(char*n)
    try:
        num = int(input("  Enter number of Students : "))               # Number of Students in the Class.
    except:
        print(char*n)
        print("|\t\t     Try again !\t\t |")
        print(char*n)
        exit()
    print(char*n)
    for i in range(num):
        Geo_dim = input("  Enter Geometry Dimension (2D/3D) : ")        # Taking Geometry Dimension (2D/3D) input from the User.
        print(char*n)
        if '2D' in Geo_dim.upper():
            _2D_()
        elif '3D' in Geo_dim.upper():
            _3D_()
        else:
            print(char*n)
            print("|\t\t     Try again !\t\t |")
            print(char*n)


if __name__ == '__main__':
    main_menu()