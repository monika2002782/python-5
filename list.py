#list 
ages=[13,23,34]
print(ages)

#store duplicate elements
list1=[1,"hello",3]
list1=[1,"hello",3,"hello",1]
list3=[list1]
print(list3)

#access list elements
languages=["python","swift","java"]
print(languages[0])

#negative indexing in python
languages=["python","swift","c++"]
print(languages[-2])

#insert
fruits=["apple","banana","cherry"]
fruits.insert(2,"orange")
print(fruits)

#index
num=[4,55,66,77,67]
x=num.index(66)
print(x)

#reverse
animals=["cat","dog","elephant","thangam"]
animals.reverse()
print(animals)

#list slicing in python
name=["p","y","t","h","o","n","b","n"]
print(name[2:5])
print(name[5:])
print(name[:])

#add elements
numbers=[12,34,56,78,89]
numbers.append(90)
print(numbers)

#extend add
numbers=[12,34,56]
even_numbers=[2,4,6]
numbers.extend(even_numbers)
print(numbers)

#join lists
list1=["apple","mango","cherry"]
list2=["banana","grapes"]
for x in list2:
    list1.append(x)
print(list1)

#using insert
foods=["pizza","burger","sweets"]
foods.insert(0,20)
print(foods)

#change list items
languages=["python","java","jscript"]
languages[2]="c"
del languages[1]
del languages[-1]
print(languages)

#remove
animals=["cat","dog","elephant"]
animals.remove("cat")
print(animals)

#list pop
prime_numbers=[2,3,4,5]
removed_elements=prime_numbers.pop(2)
print(removed_elements)

#employee list
employee=["shiva","anbu","sai","vishwa"]
employee.insert(1,"mathan")
print(employee)

#pop item at the given index from thelist
languages=["python","java","french","c++"]
return_value=languages.pop(3)
print(return_value)
print("updated list",languages)

#remove and return the last item
print("when index is not paused:")
print("return value:",languages.pop())
print("updated list:",languages)

#use of count
vowels=["apple","banana","cherry"]
count=vowels.count("apple")
print("the count is:",count)

#random tuple and list elements
random=["a",("a","b"),("a","b"),[3,4]]
count=random.count(("a","b"))
print("the count of [(a,b)] is:",count)
count=random.count([3,4])
print("the count of [3,4] is:",count)
numbers=[87,89,64,12,11,2]
numbers.sort()
print(numbers)
fruits=["apple","mango","cherry"]
fruits.sort(reverse=True)
print("sorted list:",fruits)



'''LIST''' 
ages=[13,23,34]
print(ages)

#store duplicate elements
list1=[1,"hello",3]
list1=[1,"hello",3,"hello",1]
list3=[list1]
print(list3)

#access list elements
languages=["python","swift","java"]
print(languages[0])
print(languages[2])

#negative indexing in python
languages=["python","swift","c++"]
print(languages[-1])
print(languages[-3])

#insert
fruits=["apple","banana","cherry"]
fruits.insert(3,"orange")
print(fruits)

#index
num=[4,55,66,77,67]
x=num.index(66)
print(x)

#reverse
animals=["cat","dog","elephant","thangam"]
animals.reverse()
print(animals)

#list slicing in python
name=["p","y","t","h","o","n","b","n"]
print(name[2:5])
print(name[5:])
print(name[:])

#add elements to a list
#append()--adds an element end of the list.
numbers=[12,34,56,78,89]
numbers.append(98)
print("final:",numbers)

#extend --add all the items of an iterable(list,tuple,string,dictionary,etc)
numbers=[12,34,56]
even_numbers=[2,4,6]
numbers.extend(even_numbers)
print("list after append:",numbers)

#join lists
list1=["apple","mango","cherry"]
list2=["banana","grapes"]
for x in list2:
    list1.append(x)
print(list1)

#using insert
foods=["pizza","burger","sweets"]
foods.insert(0,20)      ("0-index value,20-insert value","just identification")
print(foods)

#change list items
languages=["python","java","jscript"]
languages[2]="c"
print(languages)


# remove an item from a list
# delete
languages=["python","swift","c++","c","java","rust"]
# deleting the second item
del languages[1]
print(languages)
del languages[-1]
print(languages)
del languages[2]
print(languages)


#remove 
animals=["cat","dog","elephant"]
animals.remove("cat")
print(animals)

#list pop
prime_numbers=[2,3,4,5]
removed_elements=prime_numbers.pop(2)
print("removed element:",removed_elements)
print("updated list:",prime_numbers)


#employee list
employee=["shiva","anbu","sai","vishwa"]
employee.insert(1,"mathan")
print(employee)

#pop item at the given index from the list
languages=["python","java","french","c++"]
return_value=languages.pop(3)
print("return value:",return_value)
print("updated list:",languages)

#remove and return the last item
print("when index is not passed:")
print("return value:",languages.pop())
print("updated list:",languages)


print('\n when-1 is passed:')
print("Return value:",languages.pop(-1))
print("updated list:",languages)


# Remove and return the third item
print('\n when-3 is passed')
print("Return value:",languages.pop(-3))
print("updated list:",languages)

#use of count
vowels=['a','e','i','o','i','u']
count=vowels.count("i")
print("the count of i is:",count)

count=vowels.count('p')
print("The count of p is:",count)

#count tuple and list elements
random=["a",("a","b"),("a","b"),[3,4]]
count=random.count(("a","b"))
print("the count of [(a,b)] is:",count)
count=random.count([3,4])
print("the count of [3,4] is:",count)

#sort
numbers=[87,89,64,12,11,2]
numbers.sort()
print(numbers)

# sort revers example
fruits=["apple","mango","cherry"]
fruits.sort(reverse=True)
print("sorted list:",fruits)

#vowels list
a=["e","a","i","o","u"]
#sort the vowels
vowels.sort()
#print vowels
print("sorted list:",vowels)

#Sort in Descending order
#vowels list
vowels=["e","i","o","a","u"]
#sort the vowels
vowels.sort(reverse=True)
#print vowels
print("sorted list(in descending):",vowels)







lang=["kinds","ll","opition","get","did","did","did","ll","did","opition","did"]
count=lang.count("did")
print("the number of is:",count)
return_value=lang.pop(3)
print("return value:",return_value)
print("updated list:",lang)
print("when index is not passed:")
print("return value:",lang.pop(1))
print("updated list:",lang)
print("return value:",lang.pop(-1))
print("updated list:",lang)

random=['j',('j','l'),'j','j',('j','l')]
count=random.count
print("the count is ('j','l'):",count)



prime_number=[11,3,5,4]
prime_number.sort()
print(prime_number)
name=["kani","moni","hari","navin","kanikka"]
name.sort(reverse=True)
print(name)
vowels=['e','a','u','o','i']
vowels.sort(reverse=True)
print(vowels)
print("the value is:",vowels)


colours=("blue","red","green","yellow","violet")
print(len(colours))
print(type(colours))
tuple1=("jj","kk","jj","oo","pp","ff","gg")
tuple2=(4,2,3)
tuple3=("true","false","true","false")
print(tuple1,tuple3)
std_id={33,44,55,3,3333,33,3,8,7,444}
std_id.add(88)
print(std_id)
print("the numbers:",std_id)



# names={"kanika","monika","karithika","losilya"}
# money=["90","89","87","90","65","54"]
# high=names.discard("losilya")
# print("sert id remove():",names)
# lang={"py","kk","ll"}
# print("kk is the:",lang)
# names={"kanika","monika","karithika","losilya"}
# money=["90","89","87","90","65","54"]
# high=names.discard("losilya")
# print(high)





















































