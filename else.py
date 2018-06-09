for item in [1,2,3,4,5]:
   print (item)


for item in range(5):
   print (item**2)


counter = 1
while counter <= 5:
	print ("Hello, world")
	counter = counter + 1

#break and continue statements
count = 0
while True:
	print(count)
	count += 1
	if count >= 5:
		break

#prints out only odd numbers - 1,3,5,7,9
for x in range(10):
	#check if x is even
	if x % 2 == 0:
		  continue
	print (x)



#if else...
count=0
while(count<5):
	print (count)
	count +=1
else:
	print ("count value reached %d" %(count))


#prints out 1,2,3,4
for i in range(1, 10):
	if (i%5==0):
		break
	print (i)
else:
    print ("the link is terminated by break hence dont print but not due to fail in condition")		




if n<0:
   print ("sorry, value is negative")
else:
	print (math.sqrt(n))



#nested if

score = 55


if score >= 90:
   print ('A')
else:
    if score >=80:
       print ('B')
    else:
        if score >=70:
           print ('C')
        else:
            if score >=60:
               print ('D')
            else:
                print ('F')



#elif...
score = 75
if score >=90:
   print ('A')
elif score >=80:
   print ('B')
elif score >=70:
	print ('C')
elif score >=60:
	print ('D')
else:
	print ('F')