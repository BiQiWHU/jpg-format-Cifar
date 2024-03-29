# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:05:17 2019

@author: 2009b_000
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:44:57 2019

@author: 2009b_000
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:43:11 2019

@author: 2009b_000
"""

from scipy.misc import imsave
import numpy as np


# 解压缩，返回解压后的字典
def unpickle(file):
    import pickle
    fo = open(file, 'rb')
    dict = pickle.load(fo,encoding='iso-8859-1')
    fo.close()
    return dict

# 生成训练集图片，如果需要png格式，只需要改图片后缀名即可。

dataName = "train"  # 读取当前目录下的data_batch12345文件，dataName其实也是data_batch文件的路径，本文和脚本文件在同一目录下。
Xtr = unpickle(dataName)
print(dataName + " is loading...")

#print(Xtr)

for i in range(0, 50000):

    img = np.reshape(Xtr['data'][i], (3, 32, 32))  # Xtr['data']为图片二进制数据
    img = img.transpose(1, 2, 0)  # 读取image  
    
    for j in range(0,100):
        if Xtr['fine_labels'][i]==j:
            picName = 'traindata/' + str(j) + '/' + str(Xtr['fine_labels'][i]) + '_' + str(i) + '.jpg'  # Xtr['labels']为图片的标签，值范围0-9，本文中，train文件夹需要存在，并与脚本文件在同一目录下。
            imsave(picName, img)
            break
        else:
            continue
  
print(dataName + " loaded.")

print("test_batch is loading...")

# 生成测试集图片
testXtr = unpickle("test")
for i in range(0, 10000):
    img = np.reshape(testXtr['data'][i], (3, 32, 32))
    img = img.transpose(1, 2, 0)
    
    for j in range(0,100):
        if testXtr['fine_labels'][i]==j:
            picName = 'testdata/' + str(j) + '/' + str(testXtr['fine_labels'][i]) + '_' + str(i) + '.jpg'  # Xtr['labels']为图片的标签，值范围0-9，本文中，train文件夹需要存在，并与脚本文件在同一目录下。
            imsave(picName, img)
            break
        else:
            continue
        
    #picName = 'test/' + str(testXtr['labels'][i]) + '_' + str(i) + '.jpg'
    #imsave(picName, img)
print("test_batch loaded.")

