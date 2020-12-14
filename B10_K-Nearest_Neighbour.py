from matplotlib import pyplot
import numpy as np
import cv2

#--------------------------Khởi tạo--------------------#
data=np.random.randint(0,100,(50,2)).astype(np.float32) # 2: mảng 2 chiều(tọa độ)
result=np.random.randint(0,2,(50,1)).astype(np.float32) # gán nhãn

#-------------------------Gán nhãn----------------------#
red=data[result.ravel()==1]
blue=data[result.ravel()==0]

#-------------------------Hiển Thị----------------------#
pyplot.scatter(red[:,0],red[:,1],100,"red","o") # 100 là tỉ lệ kích cỡ hiển thị
pyplot.scatter(blue[:,0],blue[:,1],100,"blue","s")

#-------------------------Dữ liệu test------------------#
newbie=np.random.randint(0,100,(1,2)).astype(np.float32)
pyplot.scatter(newbie[:,0],newbie[:,1],100,"yellow","<")

#---------------------------Huấn luyện------------------------#

knn=cv2.ml.KNearest_create()
knn.train(data,0,result)
k=5
findResult=knn.findNearest(newbie,k)

#print(findResult)
print("Color: ",findResult[0])
print("Lable: ",findResult[1])
print("{} nearest neighbour are: {}".format(k,findResult[2]))
print("Distance to nearest neighbours are: ",findResult[3],"(mm)")

if findResult[0]==1:
    print("Result: it's red")
elif findResult[0]==0:
    print("Result: it's blue")

pyplot.show()