#Encapsulation(Data Binding)
'''class students():
    def __init__(self,name,rank,points):
        self.name=name
        self.rank=rank
        self.points=points
    #custom function   
    def demofun(self):
        print("i am"+self.name)
        print("i got rank",+self.rank)
#create 4 objects
obj=students("streve",1,100)
obj=students("bhavya",1,200)
obj=students("vishwa",2,100)
#call the functions using the objects created above
obj.demofun()
obj.demofun()
obj.demofun()'''


#encap tast
'''class peoples():
    def __init__(self,name,acname,place,adhar):
        self.name=name
        self.acname=acname
        self.place=place
        self.adhar=adhar
    def details(self):
        print("i am"+ self.name)
        print("my acname is" +self.acname)
        print("my place is" +self.place)
        print("my adhar no",+self.adhar)
obj=peoples("bhavya","savings","myd",123456789909)
obj=peoples("abi","savings","myd",123467754433)
obj=peoples("swe","withdrawl","junction",2134567890989)
obj.details()
obj.details()
obj.details()

'''