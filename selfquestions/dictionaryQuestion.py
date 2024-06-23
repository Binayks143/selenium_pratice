#wipro
# 1. create a dict with city and capital
# 2. count the number of city
# 3. print capital of xyz city is pqr
# 4. sort based on capital

# 1. create a dict with city and capital
cityCapital={'Karnataka':'Bangalor','TN':'chennai','Odisha':'BBSR','Telengana':'Hydrabad'}

# 2. count the number of city
print("Numbers of element is: ", len(cityCapital))

# 3. print capital of xyz city is pqr
for i in cityCapital:
    print(f"Capital of {i} is : {cityCapital[i]}")

# 4. sort based on city i.e key
sortedBasedOnKey=dict(sorted(cityCapital.items(),key=lambda item: item[0].lower()))
print(sortedBasedOnKey)

# 4. sort based on value i.e capital
sortedBasedOnValue=dict(sorted(cityCapital.items(), key=lambda item:item[1]))
print(sortedBasedOnValue)