
#_author__ : 'Devanshu'

class Patterns:

	def __init__(self):
		self.a = 37
		self.b = "-"
		self.choice = 0 
		
	def main(self):
		print(self.b * self.a)
		print("|\t\t MENU\t\t    |")
		print(self.b * self.a)
		print(
"""|  1. Right-angled triangle         |
|  2. Isosceles triangle            |
|  3. Kite                          |
|  4. Half Kite                     |
|  5. X                             |"""
		)
		print(self.b * self.a)

		self.choice = input("\tEnter your choice : ")
		print(self.b * self.a)

		try:
			c = int(self.choice)
			size = int(input("\tEnter the Size : "))
			self.n = size
			print(self.b * self.a)

			if int(self.choice) == 1:
				self.right_angle_triangle()

			elif int(self.choice) == 2:
				if int(self.n) % 2 == 0:
					self.Isosceles_triangle()
				else:
					print("|    Size should be even number.  |")
			
			elif int(self.choice) == 3:
				if int(self.n) % 2 == 0:
					self.kite()
				else:
					print("|    Size should be even number.  |")

			elif int(self.choice) == 4:
				self.half_kite()
			
			elif int(self.choice) == 5:
				if int(self.n) % 2 == 0:
					self.x()
				else:
					print("|    Size should be even number.  |")  
			
			else:
				print("|\t  Try again !!!  |")
		except:
			print("|\t  Try again !!!  |")

	def right_angle_triangle(self):
		for i in range(1, self.n + 1):
			print("   ", end="")
			for j in range(1, i + 1):
				print(j, " ", end='')
			print("")

	def Isosceles_triangle(self):
		count = 1
		for i in range(self.n, 0, -1):
			print(" "*i, end="")
			for j in range(1, count+1):
				print(j, end="")
			count += 2
			print("")

	def kite(self):
		self.Isosceles_triangle()
		count =  self.n + 1
		for i in range(2, self.n+1):
			print(" "*i, end="")
			for j in range(1, count+1):
				print(j, end="")
			count -= 2
			print("")

	def half_kite(self):
		count = 1
		for i in range(self.n):
			for j in range(1, count+1):
				print(" ", j, " ", end="")
			count += 1
			print("")
		count = self.n
		for i in range(self.n-1):
			for j in range(1, count):
				print(" ", j, " ", end="")
			count -= 1
			print("")

	def x(self):
		count = self.n * 2
		for i in range(1, self.n+1):
			print(" "*i, end="")
			for j in range(1, count):
				print(j, end="")
			print("")
			count -= 2
		
		count = 2
		for i in range(self.n-1, 0, -1):
			print(" "*i, end="")
			count += 2
			for j in range(1, count):
				print(j, end="")
			print("")
	

if __name__ == "__main__":
	a = Patterns()
	a.main()
	#print("-"*35)
	while True:
		print("-"*37)
		choice = input("  Do you want to continue (Y/N) : ")
		if choice.lower() == "y":
			print("-"*37)
			a.main()
		else:
			print("-"*37)
			break