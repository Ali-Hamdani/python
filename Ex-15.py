class Tank():
	def __init__(self,belt,body,weight):
		self.belt=belt
		self.body=body
		self.weight=weight
		self.power="1000hwp"
	def speed(self):
		print(self.weight,"Light weight baody has good speed")
		print(self.belt,"Friction less belt has more speed")
	def durability(self):
		print(self.body,"Strong body has very good durability")
	def setpower(self,newpower):
		self.power=newpower
	def getpower(self):
		print(self.power,"has very high power")
Alkhald=Tank("Friction_less","mettled","medium")
T_90=Tank("Friction_less","Uranium_mettled","Heavy")
print(Alkhald.body)
print(T_90.body)
Alkhald.speed()
T_90.speed()
Alkhald.durability()
T_90.durability()
print(Alkhald.power)
print(T_90.power)
T_90.power="15000hwp"
print(Alkhald.power)
print(T_90.power)
Alkhald.getpower()
T_90.getpower()
Alkhald.setpower("3000hwp")
Alkhald.getpower()
T_90.setpower("4000hwp")
T_90.getpower()
