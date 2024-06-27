# variable:- it is a sort name of any value
#                  or
# variable is a container where we store the data

# types of variable:- two types of variable
# 1. single variable
# 2 multiple variable

# limitation of variable:-

# 1. variable should be start with  alphabet.
# 2. variable can be alphanumeric.
# 3. variable in case sencentive
# 4. here you can not insert any special charactor
#5. here you can use( _ ) under score in variable

# #---------------------------------------------------
# Identation error:- it is a extra space starting of code.

# Forecasting :-data type ko change karna forecasting kahte h
#-----------------------------------------------------
# data types:- seven types of data

# 1. numerican data:-integer,float, complex 21j
# 2. text data     :-string str
# 3. sequence data :- list[],tuple(),range()
# 4. set data      :-set{}
# 5. maping data   :-dictionary{key:value}
# 6. boolen data   :- true , false
# 7. none          :- none
#----------------------------------------------------

# #-------------------------------------------------

# types of operators:- seven types of operators

# 1.arithnmatic operator : +,-,*,/,%,**,//
# 2.assignment  operator :
# 3.bitwise     operator :
# 4.comparision operator : >,<,>=,<=,==,!=(not equal to)
# 5.identity    operator : 
# 6.logical     operator : and , or , not
# 7.membership  operator :

# string fuction:-

# 1.upper:- it is use to convert the text in capital letter.
# 2.lower:-  ""  ""          ""         ""   small letter.
# 3.title:-it is use to capitalize the first alphabet of the text.
# 4.capitalize:-convert first alphabet in capital letter.
# 5.swapcase:-convert small to capital and capital to small.

# indexing:- it is use to extract the single alphabet from the text.

# types of indexing:- two types of indexing

# 1.positive indexing 
# 2.negative indexing

# slicing:-it is use to extract the range of charactor from the text.

# index:- it is use to show the position or index of alphabet.

# count:- it is use to count the particular alphabet from the text.

# replace:-it is use to replace the value from the old text.

# split:- it is use to convert string to list base of a delimeter.

# join:- it is use to convert list to string.

# strip:- it is use to delete the extra space from starting to ending of the text.

# startswith:-it is use to check the first alphabet from the text.

# #-----------------------------------------------------------------------

# loop:- it is use to run set of statement.

# types of loop:- three types of loop

# 1 while loop:- it is use to run set of statement for infinite time.
# 2.for loop:- it is use to run set of statement.
# 3.nested loop:-when one list use inside then another list is called nested loop.
# #--------------------------------------------------------------------------------

# list:- list always writtrn square bracket.
# #                  or
# list are use to store multiple value in single variable.

# uses of list:-
# 1. list are oredered
# 2. list are changable or mutable
# 3. list allow duplicate value
# 4. list are indexd
# 5. list written square bracket.
# 6. here you can store multiple value in list.

# pop:- it is use to delete value in list with the help of
#       indexing and by default delete the last value in list.

# remove:- it is use to delete valuee from the list.

# delete:- its delete all value in list.

# del:- del is a keyword that is use to delete value according
#         to index and variable.

# #--------------------------------------------------------------------------------

# insert:- it is use to add value according to index number
# append:-it is use to add the value.
# extend:- it is use to add multiple value in list.

# #-------------------------------------------------------------------------------

# sort:- it is use to arrange the data ascending or descending order.
# sorted:- same defination


#--------------------------------------------------------------
#--------------------------------------------------------------
#--------------------------------------------------------------
#--------------------------------------------------------------


# x = [45,78,89,56,253,23] # extract the value with the help of slicing

#1. 253
# print(x[-2])
#2. [45,78]
# print(x[0:2])
#3. [23,253]
# print(x[-1:-3:-1])
#4. [89,78,45]
# print(x[2::-1])
#5. [56,89]
# print(x[3:1:-1])


# sort:- it is use to arrange the data in ascending or descending order.

# x = [45,78,89,56,23,20,100]

# ascending order:-

# x.sort()
# print(x)


# descending order:-

# x.sort(reverse=True)
# print(x)

# x = [45,78,89,56,23,20,100]

# ascending order
# x.sort()
# print(x)


# descending order
# x.sort(reverse=True)
# print(x)

# x = [45,89,56,25,41,10,96,35,78]


#1.arrange the data in ascending order
# x.sort()
# print(x)

#2.extract maxium value  from the list.
# x.sort()
# print(x[-1])

#3. extract the minimum value from the list.
# x.sort()
# print(x[0])

#4. find the second highest value from the list.
# x.sort()
# print(x[-2])

#5. show the second lowest value from the list.
# x.sort()
# print(x[1])

#6 show the top 3 value from the list
# x.sort()
# print(x[-1:5:-1])

#7 show the bottom 3 number from the list
# x.sort(reverse=True)
# print(x[-1:5:-1])

#x = [45,89,56,25,41,10,96,35,78]

# max:- its extract maximum value from the list.
#print(max(x))

# min:- its extract minimum value from the list.
#print(min(x))


#-------------------------------------------------------------

# reverse
# count
# index
# copy


# x = ["sunday","monday","tuesday","wednesday","thursday","friday","saturady","sunday"]
# x.sort()
# print(x[0])



# reverse:- it is use to reverse the list.

# x = [12,85,20,100]
# x.reverse()
# print(x)

# count:- it is use to count the value from the list.

#Q. count total number of 12
# x = [12,45,78,89,56,12,45,12]
# y =  x.count(12)
# print(y)

# index:- it is show the index number of any value in list.
# b =  x.index(78)
# print(b)


# copy:- it is use to copy the list.
# x = [12,45,78,89,23]
# y = x.copy()
# x.clear()
# print(y)
# print(x)


# x = [12,45,78,89, 65,23,10]

# 1. extract all even value from the list.
# for a in x:
# 	if a%2==0:
# 		print(a)

#2. extract all odd number from the list.
# for a in x:
# 	if a%2==1:
# 		print(a)

#3. create a blank list and add all even number from x
# y = []
# for a in x:
# 	if a%2==0:
# 		y.append(a)
# print(y)

#4. create a blank list and all odd number from x
# y = []
# for a in x:
# 	if a%2==1:
# 		y.append(a)
# print(y)
#--------------------------------------------------------------


#nested list:-when one list use inside then another list
#              it is called nested list.

# x = [12,45,78,[1,2,3],100,200]
# print(x)
# print(type(x))
# print(len(x))


# x = [[1,2,3],[4,5,6],[7,8,9]]
#print(len(x))

# indeexing
#2
# print(x[0][1])
#1
# print(x[0][0])
#5
# print(x[1][1])
#9
# print(x[2][2])
#7
# print(x[2][0])
#8
# print(x[2][1])



# x = [[12,45,78,[100,200,300]]]
# print(len(x))

#1.Extract  300
# print(x[0][3][-1])
#2. 78
# print(x[0][2])
#3. 12
# print(x[0][0])
#4. 45
# print(x[0][1])
#5. 200
# print(x[0][3][-2])

#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------


# x = [12,45,78,"fri",89,8,"thu",56,62,3,32,"sun"]

# 1. delete the last value with the help of pop
# x.pop()
# print(x)

# 2. delete "Fri" with remove
# x.remove("fri")
# print(x)

# 3. delete first three elements
# x.remove(12)
# x.remove(45)
# x.remove(78)
# print(x)

# 4. delete  all values from list
# x.remove(12)
# x.remove(45)
# x.remove(78)
# x.remove(89)
# x.remove(8)
# x.remove(56)
# x.remove(62)
# x.remove(3)
# x.remove(32)
# print(x)

# 5. delete variabel of list 
# x.remove("fri")
# x.remove("thu")
# x.remove("sun")
# print(x)

#---------------------------------------------------------

# x =[12,45,78,89,23,23]
# x.insert(2,"pradeep")
# x.insert(0,250)
# print(x)



# x =[12,45,78,89,23,23]
# x.append("ram")
# x.append(4564)
# print(x)



# x = [1,2,3,4,5]
# y = [4,5,6,7,8]
# x.extend(y)
# print(x)

# x = ["virat","rohit","anikul","rakesh"]
# # create a new list and add all value of x and convert
#   in capital letter
# y = []
# for a in x:
# 	print(a.upper())
# 	y.append(a)
# print(y)

# y = []
# for a in range(1,11):
# 	y.append(a)
# print(y)

#------------------------------------------------------------


# x = [45,78,89,56,12,25,47,69,10]
# 1. delete third value
# x.remove(56)
# print(x)

# 2. add 200 in 2nd value
# x.insert(2,200)
# print(x)

# 3. add 500 in last of list
# x.append(500)
# print(x)

# 4 . delete 4th and 5 th position of value
# x.remove(12)
# x.remove(25)
# print(x)

# 5. add[1,1,1] in list
# x.append([1,1,1,])
# print(x)

# 6. add "python" last of list
# x.append("python")
# print(x)

# 7. delete 89 from list
# x.remove(89)
# print(x)



x = [45,78,89,56,253,23] # extract the value with the help of slicing

#1. 253
# print(x[-2])

#2. [45,78]
# print(x[0:2])

#3. [23,253]
# print(x[-1:3:-1])

#4. [89,78,45]
# print(x[2::-1])

#5. [56,89]
print(x[2:2:-1])




























