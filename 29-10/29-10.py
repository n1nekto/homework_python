import numpy as np

def transponeM(list_1):
    npa = np.transpose(list_1)
    return npa.tolist()

def multiplyM(list_1, list_2):
    return np.dot(list_1, list_2).tolist()

def addM(list_1, list_2):
    return np.add(list_1, list_2).tolist()

list1 = [[1,2,3],[4,5,6],[7,8,9]]
list2 = [[0,8,9],[5,6,7],[1,1,2]]
print(transponeM(list1))
print(multiplyM(list1, list2))
print(addM(list1, list2))