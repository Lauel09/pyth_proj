import os
from collections import Counter as Ct
#Returns the element with highest frequency and it's count
def common(x):
    y = Ct(x).most_common()
    return y

#Convert Dict to list for Counter
def dict_val_tolist(Dictionary):
    val = []
    for key,value in Dictionary.items():
        val.append(value)
    return val

def listdir_dict():
    dic = {}
    for i in os.listdir():
        dic['{a}'.format(a=i)] = round(os.stat(i).st_size/1024,4)
    return dic

def files(file_path):
    os.chdir(file_path)

    dic = listdir_dict()
    #to_delete = list()
    print(dic)
    dupl = common(dict_val_tolist(dic))
    for i in dupl:
        freq = i[1]
        while freq > 1:
            
            for key,value in dic.items():
                
                if value == i[0] and freq > 1:
                    print('\n Delete file:{}, of size:{}?(y/n)'.format(key,value))
                    io = input()
                    if io == 'y':
                        os.remove(key)
                        freq -= 1
                    else:
                        pass
                
                elif value < 0.0001:
                    print('\nDelete file:{},of size:{}?(y/n)'.format(key,value))
                    io =  input()
                    if io == 'y':
                        os.remove(key)
                    else:
                        passs
    dic.clear()
    #deleting dictionary
    dic = listdir_dict()
    print(dic) 
    #Cross checking if everything went right
if name == "__main__":
    folder_path = input("Path of the folder:-")
    files(folder_path)
 
