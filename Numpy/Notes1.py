my_list=[1,2,3]
import numpy as np
arr= np.array(my_lsit)
arr

my_mat=[[1,2],[2,3],[3,4]]
np.array(my_mat) #numpy array

np.arange(0,10)#from o to not including 10
#just like range function

np.arange(0,11,2) #only even numbers

np.zeros(3) #one dimension array

np.zeros((2,3))
np.ones((3,4))

#linspace
np.linspace(0,5,10)  #10 evenly space points
np.linspace(0,5,100)

np.eye(4) 
np.random.rand(5)
np.random.rand(5,5) #5 by 5 matrix
np.random.randn(2,2) #from standard normal distribution
np.random.randint(1,100) #random integer between 1 and 100 not including 100
np.random.randint(1,100,10) #10 of it

arr=np.arange(25)
ranarr=np.random.randint(0,50,10)
ranarr
arr.reshape(5,5) # need enough elements

#random array
ranarr.max()
ranarr.min()
#find location
ranarr.argmax() #the index location
ranarr.argmin() 

#shape
arr.shape # (25,) one dim
arr.reshape(5,5)

#datatype
arr.dtype #how many bit integers


