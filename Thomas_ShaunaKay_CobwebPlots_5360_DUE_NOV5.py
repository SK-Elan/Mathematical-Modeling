#############PLOT 1

import numpy as np
import matplotlib.pyplot as plt


#Function to calculate the nth iterate value of f, in the non-linear difference equation
def fn(x, a, n):
    xtPlus1 = a * x *(1-x) # Initialize xtPlus1 to substitute later in formula
    
    fVal = xtPlus1
    
    for i in range(1, n):
        fVal = a * fVal * (1 - fVal) # iterating n times
#         xtPlus1 = fVal #update xtPlus1
        
    return fVal

# fn(0.5, 1, 3)


#Use your function to plot the function Plot...

a = 3.84 #np.array([3.84, 3.84]) #Array with varying values of 'a'

n = 1 #Number of iterations for $F^{n}(x)$

xVals = np.arange(0, 1, 0.01) #Range for x Values

yx = xVals #Create yVals2 to plot the line y = x, where the slope is 1, ie rise = run

yVals = np.zeros(len(xVals)) # 2d array(matrix) to store the values for y for varying values of 'a'

for i in range(len(xVals)): #Loop through each x in order to calculate its corresponding y value.
    yVals[i] = fn(xVals[i], a, n)
        
        
        
###########################CREATE COBWEB DIAGRAM

#Initialize starting point, x0
x0 = 0.5

#Number of iterations for CobWeb Diagram
nIteration = 50


#Initialize vector to store x and y values
xCob = np.zeros(nIteration)*1
yCob = np.zeros(nIteration)*1

#Set first two elements of xCob to x0. Starting point is (x0, 0). Since value on y on x-axis is 0.
xCob[0:2] = x0, x0


#Perform nIter number of iterations to plot values of xCob and yCob
for i in range(1, nIteration, 2):
    yCob[i:i+2] = fn(xCob[i], a, n)
    xCob[i+1:i+3] = yCob[i]

print('xCob:', xCob)
print('yCob:', yCob)


#######################  PLOT #1

plt.figure(figsize = (12,10))

plt.figure(1)

plt.plot(xVals, yVals, 'b-', label = '$X_{t+1}$', linewidth = 1)
plt.plot(xVals, yx, 'r-', label = '$X_{t+1} = X_{t}$')

########PLOT COBWEB
plt.plot(xCob, yCob, 'g', label = 'cobweb')



plt.xticks(np.arange(0, 1.1, step=0.5))
plt.yticks(np.arange(0, 1.1, step=0.5))
plt.xlabel('$X_{t}$', fontsize = 14)
plt.ylabel('$X_{t+1}$', fontsize = 14)
plt.title('$F(x),\ where \ a = 3.84$')



plt.legend()
plt.show()


        


######## PLOT 2
import numpy as np
import matplotlib.pyplot as plt


#Function to calculate the nth iterate value of f, in the non-linear difference equation
def fn(x, a, n):
    xtPlus1 = a * x *(1-x) # Initialize xtPlus1 to substitute later in formula
    
    fVal = xtPlus1
    
    for i in range(1, n):
        fVal = a * fVal * (1 - fVal) # iterating n times
#         xtPlus1 = fVal #update xtPlus1
        
    return fVal

# fn(0.5, 1, 3)


#Use your function to plot the function Plot...

a = 3.84 #np.array([3.84, 3.84]) #Array with varying values of 'a'

n = 3 #Number of iterations for $F^{n}(x)$

xVals = np.arange(0, 1, 0.01) #Range for x Values

yx = xVals #Create yVals2 to plot the line y = x, where the slope is 1, ie rise = run

yVals = np.zeros(len(xVals)) # 2d array(matrix) to store the values for y for varying values of 'a'

for i in range(len(xVals)): #Loop through each x in order to calculate its corresponding y value.
    yVals[i] = fn(xVals[i], a, n)
        
        
        
###########################CREATE COBWEB DIAGRAM

#Initialize starting point, x0
x0 = 0.5

#Number of iterations for CobWeb Diagram
nIteration = 50


#Initialize vector to store x and y values
xCob = np.zeros(nIteration)*1
yCob = np.zeros(nIteration)*1

#Set first two elements of xCob to x0. Starting point is (x0, 0). Since value on y on x-axis is 0.
xCob[0:2] = x0, x0


#Perform nIter number of iterations to plot values of xCob and yCob
for i in range(1, nIteration, 2):
    yCob[i:i+2] = fn(xCob[i], a, n)
    xCob[i+1:i+3] = yCob[i]

print('xCob:', xCob)
print('yCob:', yCob)


#######################  PLOT #1

plt.figure(figsize = (12,10))

plt.figure(2)

plt.plot(xVals, yVals, 'b-', label = '$X_{t+3}$', linewidth = 1)
plt.plot(xVals, yx, 'r-', label = '$X_{t+3} = X_{t}$')

########PLOT COBWEB
plt.plot(xCob, yCob, 'g', label = 'cobweb')



plt.xticks(np.arange(0, 1.1, step=0.5))
plt.yticks(np.arange(0, 1.1, step=0.5))
plt.xlabel('$X_{t}$', fontsize = 14)
plt.ylabel('$X_{t+3}$', fontsize = 14)
plt.title('$F^{3}(x),\ where \ a = 3.84$')




plt.legend()
plt.show()


        






