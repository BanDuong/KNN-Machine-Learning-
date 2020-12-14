import math
import matplotlib.pyplot as plt
import numpy as np

instance=[] #mảng chưa khoảng cách
k=3 # số hàng xóm

#-----------------------data------------------------#
# data được lưu vào mảng một chiều 
height=np.array(np.random.randint(140,200,size=30)) # chiều cao
weight=np.array(np.random.randint(40,120,size=30))  # cân nặng
test=[np.random.randint(140,200),np.random.randint(40,120)] #dữ liệu test

#-----------------------set label---------------------#
#quy ước: cân đối=1, không cân đối=0
label=np.array(np.random.randint(0,2,size=30))

#------------------------show------------------------#
for i in range(0,len(label),1):
    if(label[i]==1):
        plt.scatter(height[i],weight[i],100,"red","o")
    else:
        plt.scatter(height[i],weight[i],100,"blue","o")
plt.scatter(test[0],test[1],100,"yellow","<")
plt.xlabel("Chiều Cao")
plt.ylabel("Cân Nặng")
plt.title("Dự đoán người trường thành cân đối hay không")


# hàm tính khoảng cách lưu vào mảng một chiều
def function():
    for i in range(0,len(height)):
        instance.append(float(math.sqrt(math.pow(test[0]-height[i],2)+math.pow(test[1]-weight[i],2))))      

# hàm sắp xếp mảng khoảng cách và nhãn giảm dần   
def sort_funct(instance):
    for i in range(0,len(height)):
        min_index=i
        for j in range(i+1,len(height)):
            if(instance[j]>instance[min_index]):
                min_index=j
        instance[i],instance[min_index]=instance[min_index],instance[i]
        label[i],label[min_index]=label[min_index],label[i]
        
function()

sort_funct(instance)

dem=0
for i in range(0,k,1):
    if(label[i]==1):
        print(label[i])
        dem+=1
    else:
        print(label[i])
        
if(dem>k-dem):
    print("cân đối")
else:
    print("không cân đối")

plt.show()















            


