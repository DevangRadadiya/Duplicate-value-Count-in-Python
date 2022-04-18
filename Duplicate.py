country_name=[]
count_name={}
for i in range(5):
    a=input("Enter Country Name : ");
    country_name.append(a)

for i in country_name:
     if not i in count_name:
        count_name[i] = 1       
     else:          
        count_name[i] +=1
print(count_name)
