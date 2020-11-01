class Bike():
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.battery="300amp"
	def description(self):
		print("The make of this Bike is",self.make)
		print("The model of this Bike is",self.model)
		print("The year of this Bike is",self.year)
	def speed(self):
		print(self.make,"have different speeds")
	def verity(self):
		print(self.model,"has many verities")
	def battery(self):
		print(self.battery,"is a good battery")
	def setbatterysize(self,newsize):
		self.battery=newsize
	def getbatterysize(self):
		print("The size of the battery is",self.battery)
Bike1=Bike("Yamha","suzuki",2018)
Bike2=Bike("Kawsaki","caltas",2015)
print(Bike1.make)
print(Bike1.model)
print(Bike1.year)
Bike1.description()
Bike1.speed()
Bike1.verity()
print(Bike1.battery)
print(Bike2.battery)
Bike2.battery="500amp"
print(Bike2.battery)
print(Bike1.battery)
Bike1.getbatterysize()
Bike2.getbatterysize()
Bike1.setbatterysize("700amp")
Bike1.getbatterysize()