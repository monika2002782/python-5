## reuseful of value

#single 


# class student():
#     def studentdetails(self):
#         print("it ois my details")
#         print("this is a student idea")
# class staff(student):
#     def studentdetails(self):
#         print("yeah its me")
# detail=staff()
# detail.studendetails()
# detail.staffdetails()
       



#multiple 


# class employeedetails():
#     def company(self,name,age):
#         print("it is my resume")
#         print("Name:",name,"Age:",age)
# class secondround():
#     def round2(self,score):
#         print("it is my score")
#         print("may score is:",score)
# class thirdround(employeedetails,secondround):
#     def round3(self,hr):
#         print("final round")
#         print("my details",hr)
# obj= thirdround()
# obj.company("monika",11)
# obj.round2("89")
# obj.round3("kkkkk")


###single inheritance


# class  vehicle():
#     def vehicle_info(self):
#         print("inside name class")

##child class


# class car(vehicle):
#     def car_info(self):
#         print("insoide car class")



#create object of car



# ob=car()   
# #access vehicles info using car object    
# ob.vehicle_info() 
# ob.car_info()


#multiple inheritance

# class person():
#     def person_info(self,name,age):
#         print("inside person class")
#         print("Name:",name,"Age:",age)

##parent class

# class company():
#     def company_info(self,company_name,location):
#         print("inside company class")
#         print("Name:",company_name,location)

##child class

# class employee(person,company):
#     def employee_info(self,salary,skill):
#         print("inside employee class")
#         print("salary:",salary,"skil:",skill)





#task


# kk=employee()
# kk.person_info("moni",56)
# kk.company_info("jj","north street")
# kk.employee_info(80000,"none")        
# class hotel():
#     def roomkey_no(self):
#         print("the first room key no is: 787")
#         print("the second room key no is: 676")
# class room1(hotel):
#     def first_room(self,book,guide,dictionary):
#         print("the first room availabel") 
#         print("Book:",book,"Guide:",guide,"Dictionary:",dictionary)
# class room2(hotel):
#     def second_room(self,notes,waterbottle,pen):
#         print("the second room availabel") 
#         print("notes:",notes,"water botttle:",waterbottle,"pen:",pen) 
# class room3(room1,room2):
#     def thrid_room(self,bags,food):
#         print("the thrid room availabel")
#         print("bags:",bags,"foods:",food)        
# hh=room1()
# hh=room2()
# hh.roomkey_no()
# hh.first_room("nnn","kkk","jjj")
# hh.second_room("jjj","ggg","bhhh")
# hh.thrid_room("jjjp","hhh")                    

