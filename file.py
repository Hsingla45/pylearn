"""
name = input("enter customer name")
phone = input("enter customer phone")

customer_details = "{},{} \n".format(name, phone)

file = open("customer.csv","a")
file.write(customer_details)
print("data saved")
file.close
"""
"""
file = open("customer.csv", "r") #mention path here to write a file at particular location

data=file.read()

print(data)
"""
"""
large_data = [
                 [
                  [10,20,30],
                  [50,60,30],
                  [56,89,65],
                 ],
                [  
                 [456,564,45],
                 [85,54,56],
                ]  

]


print(large_data[1][0][1])
"""
"""name = {"a":10,"b":20,"c":30}


print(name["a":"b"])
"""
"""
def numbers (*aa):
    print(aa)

numbers(10,20,20)

print("~~~~~~~~~~~~~")

def fun(*args, **kwargs):
    print(args)
    print(kwargs)

fun(10,20,30, "hsifd","ajfd", a=10)
"""

# bubble sort
"""
def bubble_sort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                
        

numbers = [46,98,65,78,20]

result = bubble_sort(numbers)

print(numbers)

"""
"""
data = [10,20,30,40,50]

data1 = list(reversed(data))

print(data1)

"""
"""
data = ["anna","bell","cat"]

print(max(data))

data = [10,20,30,40,50]

data.sorted(data, reversed(data))
"""
"""
data = (10, 20, 50)

print(max(data))
#data.pop() 
#data.insert(3, 60) 
data.remove(20)
print(data)
"""
"""
A = {1,2,3,4,5}
B = {4,5,6,7,8}

c = A-B # remove common elements from A
print(c)
#d= A + B
#print(d) 
"""           
"""
e = A ^ B # remove common elements from a and b
print(e)

f = A | B # concatenate for set 
print(f)

dict = {} # empty dictonary 
set = set() # empty set 
list = [] #empty list

"""

my_dict ={"a": 10,
       "b": 20,
       "c": 30}

"""
keys_list= list(my_dict.keys())
print(keys_list)
values_list = list(my_dict.values()).index(30)
print(values_list)
"""


#v= list(my_dict.keys())[2]

#print(v)

#print("One line Code Key value: ", list(my_dict.keys())
#      [list(my_dict.values()).index(30)])


    
covid_data_world = {
    "usa": {"active":786167, "serious":40333, "recovered":985},
    "india": {"active":226167, "serious":2344, "recovered":1985},
    "brazil": {"active":96167, "serious":1221, "recovered":850},
    "italy": {"active":18167, "serious":4433, "recovered":3185},
    "uk": {"active":61670, "serious":6722, "recovered":9098},
}


# Write the Logic to copmute below data
# 1: Total Active
# 2: Total Serious
# 3: Total Recovered

# 4: Min/Max Active/Serious/recovered on Country

# 5: To compute Average of all Active/Serious/Recovered in world
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 1: Min/Max Active/Serious/recovered on Country

# getting max value
us_max = covid_data_world["usa"].values()
india_max = covid_data_world["india"].values()
brazil_max = covid_data_world["brazil"].values()
italy_max = covid_data_world["italy"].values()
uk_max = covid_data_world["uk"].values()


print(max(us_max))
print(max(india_max))
print(max(brazil_max))
print(max(italy_max))
print(max(uk_max))

# getting key from the max value retrieved above 
print("Maximum category of cases in US:",list(covid_data_world["usa"].keys())[list(covid_data_world["usa"].values()).index(max(us_max))])
print("Maximum category of cases in India:",list(covid_data_world["india"].keys())[list(covid_data_world["india"].values()).index(max(india_max))])
print("Maximum category of cases in Brazil:",list(covid_data_world["brazil"].keys())[list(covid_data_world["brazil"].values()).index(max(brazil_max))])
print("Maximum category of cases in Italy:",list(covid_data_world["italy"].keys())[list(covid_data_world["italy"].values()).index(max(italy_max))])
print("Maximum category of cases in UK:",list(covid_data_world["uk"].keys())[list(covid_data_world["uk"].values()).index(max(uk_max))])

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# getting min value and its key
uk_min = covid_data_world["uk"].values()
#print(min(uk_min))
print("Minimum category cases in uk:",list(covid_data_world["uk"].keys())[list(covid_data_world["uk"].values()).index(min(uk_min))])
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#2.Logic for computing the below data
#  1: Total Active
#  2: Total Serious
#  3: Total Recovered


us_list = list(covid_data_world["usa"].values())
india_list = list(covid_data_world["india"].values())
brazil_list = list(covid_data_world["brazil"].values())
italy_list = list(covid_data_world["italy"].values())
uk_list = list(covid_data_world["uk"].values())

# Total active/serious/recovered cases
print("Total Active cases in world:",us_list[0]+india_list[0]+brazil_list[0]+italy_list[0]+uk_list[0])
print("Total Serious cases in world:",us_list[1]+india_list[1]+brazil_list[1]+italy_list[1]+uk_list[1])
print("Total Recovered cases in world:",us_list[2]+india_list[2]+brazil_list[2]+italy_list[2]+uk_list[2])
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Computing Average of all Active/Serious/Recovered in world
print("Average of all Active cases:",(us_list[0]+india_list[0]+brazil_list[0]+italy_list[0]+uk_list[0])/len(covid_data_world))
print("Average of all Serious cases:",(us_list[1]+india_list[1]+brazil_list[1]+italy_list[1]+uk_list[1])/len(covid_data_world))
print("Average of all Recovered cases:",(us_list[2]+india_list[2]+brazil_list[2]+italy_list[2]+uk_list[2])/len(covid_data_world))



      