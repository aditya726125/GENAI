#Loop-- helps execute block of code repeatedly
#For loop--this loop apply all sequence (list, string, tuple)

my_sub= "Python"
for i in my_sub:     #in- membership operator , i- variable
    print(i)

for i in range(len(my_sub)):
    print(my_sub[i], "->", i)

my_list= [89,76,45,34]
for i in my_list:
 print(i)

#While loop--this loop execute until condition is true

i = 0   #initialization
while i<5:  #condition
   print(i)
   i+=1 #increment

#loop control statement
#break-- this statement break the loop

i=0
while i<9:
   i+=1
   if i==6:
        break
   else:
      print(i)

#continue statement-- this statement skip your current iteration
i=0
while i<5:
   i+=1
   if i==3:
      continue
   print(i)
else:
   print(i)

   i=0
while i<5:
   i+=1
   if i==3:
      pass
   print(i)
else:
   print(i)
    