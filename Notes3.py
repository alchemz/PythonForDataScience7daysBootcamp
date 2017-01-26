#map and filter functions
def times2(var):
return var*2

times2(5)

#map()
seq=[1,2,3,4,5]
list(map(times2,seq))

def times2(var):return var*2
#lambda expressuib
lambda var:var*2
t=lambda var:var*2

list(map(lambda num:num*3, seq))#write the function to a single line clean code

#built in filter
#difference: filter out elements
filter(lamda num:num%2 ==0, seq)
#return the filter 
list(filter(lambda num:num%2==0,seq))
#return values happen to be true

#methods
#returm results in some manner
s="Hello My name is LIng"
s.lower() #lower case every element
s.upper()
s.split() # split strings with all white space
tweet="Go sports #go #fo"
s.split('#')[1]
#output 'go'

d={'k1':2,'k2':1}
d.items()
d.values()
lst=[1,2,3]
lst.pop() #return the last item
item=lst.pop() # pop out the last item by default
lst.append('new') #add

'x' in [1,2,3] #false

x=[(1,2),(3,4),(4,5)]
for item in x:
    print(item)
    
for a,b in x:
print(b) #unpack the tuple
