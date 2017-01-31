#what is 7 to the power of 4
7**4

#split the string s="Hi there Sam!"
s="Hi there Sam!"
s.split()
#output: ['Hi','there','Sam!']

#format
planet ="Earth"
diameter=12742

print('The diameter of planet is kilometers'.format(planet,diameter))
#{} will be filled with parameters

#indexing to grab element
lsd=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
#find "Hello"
lsd[3] #find[5,[100,200,['hello']]]
lsd[3][1][2][0]

#grab "Hello"
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d['k1'] #the only key
d['k1'][3]['tricky'][3]['target'][3]

#use a function to obtain the email domain
def domainGet(email)
  return email.split('@')[1]

domainGet('user@domain.com')

