#1-  For loop Print all integers from 0 to 150.
print ("For loop Print all integers from 0 to 150.")
for i in range(151):
    print(i)

#2- For loop Print all the multiples of 5 from 5 to 1,000
print ("For loop Print all the multiples of 5 from 5 to 1,000")
for i in range(5,1001,5):
    print(i)

#3- For loop Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"
print ("For loop Print integers 1 to 100. If divisible by 5, print 'Coding' instead. If divisible by 10, print 'Coding Dojo'")
for i in range(1,100):
    if i%10 == 0: print("Coding Dojo")
    elif i%5 == 0: print("Coding")
    else: print(i)

#4- For loop Add odd integers from 0 to 500,000, and print the final sum
print ("For loop Add odd integers from 0 to 500,000, and print the final sum")
sum = 0
for i in range(0,500000):
    if i%2 == 1: 
        sum += i 
print (" sum = " + str (sum))

#5- For loop Print positive numbers starting at 2018, counting down by fours.
print ("For loop Print positive numbers starting at 2018, counting down by fours.")

for i in range(2018,0,-4):
    print (i)

#6- For loop et three variables: lowNum, highNum, mult.if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
print ("For loop set three variables: lowNum, highNum, mult.if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)")
lowNum = 6 
highNum = 3621
mult = 7 
for i in range(lowNum,highNum):
    if i%mult == 0: print (i)