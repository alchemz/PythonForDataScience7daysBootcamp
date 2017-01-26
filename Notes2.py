seq=[1,2,3,4,5]
for item in seq:
  print (item);
  print ("Hello")

i=1 
while i<5:
  print('i is :{}',format(i)) #i is always smaller than 5
  i=i+1 #otherwise inifite loop
  
for x in seq:
  print(x)
  
for x in range(0,5):
  print(x) #short way to do the loop

list(range(10))

x=[1,2,3,4]
out=[]

for num in x:
  out.append(num**2) #quickly create a list

#the other way
out=[num**2 for num in x]
    #[things need to append]

  
print(out)

#functions
def my_func(param1):
  print(param1)
  
#call the function
my_func('Hello')

def my_name(name):
  print("Hello"+name)
  
#call function
my_name(name='Ling')
my_name('Ling') #for executing the function

def square(num):
    return num**2
output=square(2) #return needs to store it to some variables

def square(num):
  """
  This is a sentence
  """
  return num**2

#shift tap to get function
