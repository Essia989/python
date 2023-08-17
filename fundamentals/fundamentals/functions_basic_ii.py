
#------------------------------------------------------------------------------
# CountDown Function 
def Countdown (number):
    list =[]
    for i in range(number,-1,-1):
        list.append(i)
    return list

print("Countdown :",Countdown(int(input ("Enter number :"))));

#------------------------------------------------------------------------------
#Print and Return
def Print_return (a,b):
    print(f"First : {a}")
    return b

print("Second :",Print_return(7,9))

#------------------------------------------------------------------------------
#First Plus Length
def FirstPlusLength(list):
    first = list[0]
    return first+len(list)

print("First Plus Length : ",FirstPlusLength([13,2,3,4,5,14,7,8,9,10,11]))

#------------------------------------------------------------------------------
#Values Greater than Second 
def values_greater_than_second(list):
    num = 0
    list2 =[]
    for i in range(len(list)):
        if list[i] > list[1]:
            num += 1
            list2.append(list[i])
    print(num)
    return list2

print (values_greater_than_second ([5,2,3,2,1,4]))

#------------------------------------------------------------------------------
#This Length, That Value
def length_and_value(size,value):
    list = []
    for i in range(size):
        list.append(value)
    return list

print (length_and_value(5,-1))