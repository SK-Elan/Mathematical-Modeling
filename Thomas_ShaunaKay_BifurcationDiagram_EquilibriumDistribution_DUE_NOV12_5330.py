# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

#########################Want to construct Bifurcation diagram


#Function to calculate the nth iterate value of f, in the non-linear difference equation
def fn(x, a, n):
    xtPlus1 = a * x *(1-x) # Initialize xtPlus1 to substitute later in formula
    
    fVal = xtPlus1
    
    for i in range(1, n):
        fVal = a * fVal * (1 - fVal) # iterating n times
        
    return fVal

#initialization
a_min = 3.582
a_max = 3.585
n_a = 2000
min_iter = 100
n_iter = 200

#Initialize xVec and yVec
xVec = np.zeros(n_iter - min_iter)
yVec = np.zeros(n_iter - min_iter)

#Initialize aVec an n_a equally spaced values between a_min and a_max
aVec = np.linspace(a_min, a_max, n_a)

plt.figure(figsize = (10,7))

##Loop over values of a_vec
y = 0.5
for ii in range(n_a):
    y = fn(y, aVec[ii], min_iter) 
    ##Aim is to iterate until convergence(to a fixed point) is obtained. (convergence is expected by min_iter no. of iterations.) 
    #Function fn does that for us
    for jj in range (n_iter - min_iter):
        y = fn(y, aVec[ii], 1)
        #For each ii, after min_iter no. of iterations (ie fn(y, aVec[ii], min_iter) ), record the corresponding 'a' and y values. This is done
        #to see how the function behaves after 'convergence' is obtained for corresponding values of 'a' and 'y' thereafter. 
        xVec[jj] = aVec[ii] #xVec updated with each 'a[ii]' after min_iter iterations is performed
        yVec[jj] = y  #yVec is continuously being obtained after min_iter iterations is performed

    
    plt.scatter(xVec, yVec, color = 'b', s = 0.01)
    plt.title('Bifurcation Plot (a_min = {a}, a_max = {b})'.format(a=a_min, b = a_max))
    plt.xlabel('a')
    plt.ylabel('$F^{n}(x)$')


plt.show()
    



#######################################3

# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

#########################EQUILIBRIUM DISTRIBUTION FOR LOGISTIC MAP

#Function to calculate the nth iterate value of f, in the non-linear difference equation
def fn(x, a, n):
    xtPlus1 = a * x *(1-x) # Initialize xtPlus1 to substitute later in formula
    
    fVal = xtPlus1
    
    for i in range(1, n):
        fVal = a * fVal * (1 - fVal) # iterating n times
        
    return fVal

#initialization
min_iter = 100
n_iter = 100000
n_bins = 100

#Initialize xVec and yVec
xVec = np.zeros(n_iter - min_iter) #To later store varying values of 'a' after the point of convergence
yVec = np.zeros(n_iter - min_iter)#To later store varying values of 'y = F' after the point of convergence

#Initialize aVec as a vector of 'a' values
aVec = np.array([3.64, 3.68, 3.72])

#create vector to store histogram values
hists = np.zeros((len(aVec), len(yVec)))

###Bins
bins = np.linspace(0, 1, n_bins+1)




##Loop over values of a_vec
y = 0.5
for ii in range(len(aVec)):
    y = fn(y, aVec[ii], min_iter)
    for jj in range (n_iter - min_iter):
        y = fn(y, aVec[ii], 1)
        xVec[jj] = aVec[ii]
        yVec[jj] = y
        hists[ii,jj] = y

    plt.figure(num = ii +1) #, figsize = (7,6)
    
    
    plt.hist(hists[ii,:], bins)
    plt.title('Histogram Plot (a = {x})'.format(x = aVec[ii]), fontsize=15)
    plt.xlim(min(bins), max(bins))
    plt.grid(axis='y')
    plt.xlabel('Function Values',fontsize=9)
    plt.ylabel('Frequency',fontsize=9)
    plt.xticks(fontsize=9)
    plt.yticks(fontsize=9)

    plt.show()
    
##print(hists.shape)
    




