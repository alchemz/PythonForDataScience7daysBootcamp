#dictionary
d={'key1':'value','key2':123}
d['key1'] #d[0] does not work
d['key2']
d={'k2'"[1,2,3]}
d['k2']
d['k2'][1] # second elements of the k2
d={'k1':{'innerKey':[1,2,3]}}    #nested
   d['k2']['innerKey'][0]

#difference between t=(1,2,3) t=[1,2,3]
#do not support item assignment
   
#sets
   {1,2,3,3,3,3,3}
   #output the unique elements only
   {1,2,3}
   s={1,2,3,5}
   s.add(6)

#comparsion operators
   1>2 #false
   1==1 #error for assignment
   1 !=1 #false
   1 <2 and 2<3 # true and false return a false
   1 <2 or 2<3 # true or false return true
   
#conditions
   if 1<2: # if true
   print('First')
   elif 1<3: #elif for else if
   print('middle')
   else:
   print('last')
