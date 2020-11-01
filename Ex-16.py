class Bakra():
    def __init__(self,tail,teeth,health):
        self.tail=tail
        self.teeth=teeth
        self.health=health
    def scrificeable(self):
        print(self.teeth,"donda is sacrificeable and khara is not sacrificeable")
        print(self.health,"healthy is sacrificeable and sick is not sacrificeable")
        print(self.tail,"tail is necessary and tail_less is not sacrificeable")
bakra1=Bakra("tail_less","khera","sick")
bakra2=Bakra("tail","donda","sick")
bakra3=Bakra("tail","khera","healthy")
bakra4=Bakra("tail_less","khera","sick")
bakra5=Bakra("tail","donda","healthy")
bakra6=Bakra("tail","donda","healthy")
bakra7=Bakra("tail","donda","healthy")
bakra8=Bakra("tail","donda","healthy")
bakra9=Bakra("tail","donda","healthy")
bakra10=Bakra("tail_less","khera","sick")
bakra11=Bakra("tail","donda","sick")
bakra12=Bakra("tail","khera","healthy")
bakra13=Bakra("tail_less","khera","sick")
bakra14=Bakra("tail","donda","sick")
bakra15=Bakra("tail","khera","healthy")
bakra16=Bakra("tail_less","khera","sick")
bakra10.scrificeable()
bakra7.scrificeable()