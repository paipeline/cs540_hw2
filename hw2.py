import sys
import math
import re
import numpy as np

def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    #initialize dict
    X= {chr(k):0 for k in range(ord("A"),ord("Z")+1)}
    with open (filename,encoding='utf-8') as f:
        # TODO: add your code here
        for line in f:
            #loop each word
            for word in line:
                #extract only letters
                #TODO: Test on Gradescope
                word = re.sub("[^a-zA-Z]","",word)
                #loop each letter
                for l in word:
                    #to upper
                    l = l.upper()
                    X[l] += 1

    return X



# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!


#1 read in letter.txt

shred = shred("letter.txt")
#print result
# A to Z list
AtoZ= sorted(shred.keys(),reverse=False)
print("Q1")
for i in AtoZ:
    print(i,shred[i])
    #TODO: check the output

# given the probability of each letter in s and e 
each_X_given_e = get_parameter_vectors()[0]
each_X_given_s = get_parameter_vectors()[1]
# frequency of each letter in X
freq_X = list(shred.values()) # freq from A to Z
# probability of e and s
prob_e = 0.6
prob_s = 0.4

#1.2
#X_1*loge1
print("Q2")
sol_1_2_1 = np.round(freq_X[0]*np.log(each_X_given_e[0]),4)
sol_1_2_2 = np.round(freq_X[0]*np.log(each_X_given_s[0]),4)
print(sol_1_2_1)
print(sol_1_2_2)

f_e = prob_e * np.prod([each_X_given_e[i]**freq_X[i] for i in range(len(freq_X))])
f_s = prob_s * np.prod([each_X_given_s[i]**freq_X[i] for i in range(len(freq_X))])

# F(English) F(Spanish)
F_e = np.round(prob_e + np.sum(freq_X*np.log(each_X_given_e)),4)
F_s = np.round(prob_s + np.sum(freq_X*np.log(each_X_given_s)),4)
print("Q3")
print(F_e)
print(F_s)

# P(English|X)
print("Q4")
p_y_given_x = np.round(f_e/(f_e+f_s),4)
print(p_y_given_x)




# Calculate C(X)
# C_X_div = 1
# for i in range(len(freq_X)):
#     C_X_div *=np.math.factorial(freq_X[i])
# print(C_X_div)
# C_X = np.math.factorial(np.sum(freq_X))/(C_X_div)

# # Calculate P(X|Y = e) + P(X | Y = s)
# P_X_given_e = C_X * np.prod([each_X_given_e[i]**freq_X[i] for i in range(len(each_X_given_e))])

# P_X_given_s = C_X * np.prod([each_X_given_s[i]**freq_X[i] for i in range(len(each_X_given_s))])

# # Calculate Evidence
# evidence = P_X_given_e + P_X_given_s

# # Calculate P(Y=e | X)
# P_e_given_X = (P_X_given_e * prob_e)/evidence

# # Calculate P(Y=s | X)
# P_s_given_X = (P_X_given_s * prob_s)/evidence
# print(P_e_given_X,P_s_given_X)


###### Computational considerations #######
