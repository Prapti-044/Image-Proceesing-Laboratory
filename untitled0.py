# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:03:15 2019

@author: prapti
"""
#Taking inputs for Quantity and Material type

quantity = float(input("Enter the value of Quantity: "))
material = float(input("Enter the value of Material Type: "))

#Membership functions for Quantity

s_quantity = [ i * 100 for i in [ 0, 0.4 ]]
m_quantity = [ i * 100 for i in [ 0.30, 0.75 ]]
l_quantity = [ i * 100 for i in [ 0.65, 1 ]]

#Membership functions for Material type

s_material = [ i * 100 for i in [ 0, 0.45 ]]
m_material = [ i * 100 for i in [ 0.40, 0.75 ]]
h_material = [ i * 100 for i in [ 0.60, 1 ]]


q = []
m = []

#Fuzzification function for Quantity

def find_quantity(x):
    
    #for Small_quantity
    
    s_av = (s_quantity[0] + s_quantity[1])/2 #taking the average of quantity: small
    
    if x > s_quantity[1] or x < s_quantity[0]: # if x is out of range
        q.append(0)
    elif x>=s_quantity[0] and x<=s_av: # if x between average and lower range from average
        y = (x - s_quantity[0])/(s_av - s_quantity[0])
        q.append(y)
    elif x == s_av: # if x equal to average
        q.append(1)
    elif x>=s_av and x<=s_quantity[1]: # if x between average and higher range from average
        y = ( x - s_quantity[1] ) / (s_av - s_quantity[1])
        q.append(y)
        
     #for Medium_quantity
     
    m_av = (m_quantity[0] + m_quantity[1]) / 2 #taking the average of quantity: medium 
    
    if x > m_quantity[1] or x < m_quantity[0]: # if x is out of range
        q.append(0)
    elif x>=m_quantity[0] and x<=m_av:  # if x between average and lower range from average
        y = (x - m_quantity[0])/(m_av - m_quantity[0])
        q.append(y)
    elif x == m_av: # if x equal to average
        q.append(1)
    elif x>=m_av and x<=m_quantity[1]: # if x between average and higher range from average
        y = ( x - m_quantity[1] ) / (m_av - m_quantity[1])
        q.append(y)
                 
     #for Large_quantity
     
    l_av = (l_quantity[0] + l_quantity[1]) / 2 #taking the average of quantity: large
    
    if x > l_quantity[1] or x < l_quantity[0]:  # if x is out of range
        q.append(0)
    elif x>=l_quantity[0] and x<=l_av:  # if x between average and lower range from average
        y = (x - l_quantity[0])/(l_av - l_quantity[0])
        q.append(y)
    elif x == l_av: # if x equal to average
        q.append(1)
    elif x>=l_av and x<=l_quantity[1]: # if x between average and higher range from average
        y = ( x - l_quantity[1] ) / (l_av - l_quantity[1])
        q.append(y)
        
#Fuzzification function for Material type

def find_material(x):
    
    #for Soft material type
    
    s_av = (s_material[0] + s_material[1])/2 #taking the average of quantity: soft
    
    if x > s_material[1] or x < s_material[0]:
        m.append(0)
    elif x>=s_material[0] and x<=s_av:
        y = (x - s_material[0])/(s_av - s_material[0])
        m.append(y)
    elif x == s_av:
        m.append(1)
    elif x>=s_av and x<=s_material[1]:
        y = ( x - s_material[1] ) / (s_av - s_material[1])
        m.append(y)
    
    #for Medium material type
    
    m_av = (m_material[0] + m_material[1]) / 2 #taking the average of quantity: medium
    
    if x > m_material[1] or x < m_material[0]:
        m.append(0)
    elif x>=m_material[0] and x<=m_av:
        y = (x - m_material[0])/(m_av - m_material[0])
        m.append(y)
    elif x == m_av:
        m.append(1)
    elif x>=m_av and x<=m_material[1]:
        y = ( x - m_material[1] ) / (m_av - m_material[1])
        m.append(y)
    
    #for Hard material type
    
    h_av = (h_material[0] + h_material[1]) / 2 #taking the average of quantity: hard
    
    if x > h_material[1] or x < h_material[0]:
        m.append(0)
    elif x>=h_material[0] and x<=h_av:
        y = (x - h_material[0])/(h_av - h_material[0])
        m.append(y)
    elif x == h_av:
        m.append(1)
    elif x>=h_av and x<=h_material[1]:
        y = ( x - h_material[1] ) / (h_av - h_material[1])
        m.append(y)
        
#Fuzzification of quantity and material type
        
find_quantity(quantity)
find_material(material)

# Output variables

slow = []
intermediate = []
fast = []

#Rules based for proposed model

slow.append(min(q[0], m[0]))
slow.append(min(q[0], m[1]))

intermediate.append(min(q[0], m[2]))
intermediate.append(min(q[1], m[0]))
intermediate.append(min(q[1], m[1]))

fast.append(min(q[1], m[2]))

intermediate.append(min(q[2], m[0]))

fast.append(min(q[2], m[1]))
fast.append(min(q[2], m[2]))

#taking output range

max_slow = max(slow)
max_intermediate = max(intermediate)
max_fast = max(fast)

#Defuzzification
#calculating Centroid of Gravity

centroid_of_gravity = max_slow * (0.0 + 0.10 + 0.2 + 0.30)
centroid_of_gravity += max_intermediate * (0.40 + 0.50 + 0.60)
centroid_of_gravity += max_fast * (0.70 + 0.80 + 0.90 + 1.0)

centroid_of_gravity /= ((max_slow * 4) + (max_intermediate * 3) + (max_fast * 4))

#Outputs

print('Centroid of Gravity :', centroid_of_gravity)
print('Range of output: ',centroid_of_gravity * 100)