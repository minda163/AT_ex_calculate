
# coding: utf-8

# In[94]:


"""
Created on Sun May 6 2018

@author: wyxx
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#在jupyter的运行环境中显示图像
get_ipython().magic('matplotlib inline')

fig=plt.figure()
ax=fig.add_subplot(111)

font_set = 'STsong' #赋值STsong为宋体，SimHei黑体 
plt.title(u'复线AT牵引供电系统实例参数',fontproperties=font_set)#添加标题，并显示汉字
filename = 'Traction_Network_Parameters.xlsx'# 读取的文件名（放在同一文件下）

# 使用pandas处理excel文件,excel文件里有原始数据
para = pd.read_excel(filename)
para.set_index(keys=['导线编号'])# 指定 导线编号 为索引列
# print(para.head(5))
linexs=para['横坐标'] #把横坐标值赋值给linexs
lineys=para['纵坐标'] #把纵坐标值赋值给lineys
spec=para['规格'] #把规格值赋值给spec 作图显示各线的规格名称时使用
name=para['导线名（编程）']#把导线名值赋值给name 作图显示各线的名称时使用
num=para['导线编号']#把导线编号值赋值给num 作图显示各线的编号时使用
leftx = linexs.max()+(linexs.max()-linexs.min())/6
rightx =linexs.min()-(linexs.max()-linexs.min())/6
highty =lineys.max()+(lineys.max()-lineys.min())/6
ax.axis([rightx,leftx,0,highty])# 根据位置数据，划定坐标范围

# 把需要划的线分为十二个点的连线
x1 = x2 = x8 = x12 = 0
y1 = y3 = y5 = y10 = 0
y2 = y4 =y6 =highty-(lineys.max()-lineys.min())/14
x3 = x4 = (linexs.min()/10)*6
x5 = x6 = x7 = x9 = (linexs.min()/10)*7
y7 = y8 = y2*0.9
y9 =y2*0.7
x10 = x3*0.65
x11 = x3*0.45
y11 = y12 = 810
# doty = [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12]
color = 'blue' #调整图中线条的颜色
# 画图，坐标原点左边的柱子和三角架和轨枕
plt.plot([x1,x2],
         [y1,y2],color=color) #坐标原点的柱子,点1和2连接
plt.plot([x3,x4,x6,x5],
         [y3,y4,y6,y5],color=color) #坐标原点左侧的双线柱子，点3465连接
plt.plot([x7,x8,x9],
         [y7,y8,y9],color=color) #三角架子，点789连接
plt.plot([x10,x11,x12],
         [y10,y11,y12],color=color) #轨枕，点10,11,12连接
plt.plot([-x10,-x11,x12],
         [y10,y11,y12],color=color) #轨枕，点10,与点11,12x轴取负值后连接
# 画图，坐标原点右边的柱子和三角架和轨枕
# 由于对称关系，y轴没有变化，x轴加5000
dotx = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12]
dotxx=np.zeros(12)
for i in range(12):
    if i in [0,1,7,11]:
        dotxx[i]=dotx[i]+5000
    else:
        dotxx[i]=abs(dotx[i])+5000
plt.plot([dotxx[1-1],dotxx[2-1]],
         [y1,y2],color=color) #坐标原点的柱子,点1和2连接
plt.plot([dotxx[3-1],dotxx[4-1],dotxx[6-1],dotxx[5-1]],
         [y3,y4,y6,y5],color=color) #坐标原点左侧的双线柱子，点3465连接
plt.plot([dotxx[7-1],dotxx[8-1],dotxx[9-1]],
         [y7,y8,y9],color=color) #三角架子，点789连接
plt.plot([dotxx[10-1],dotxx[11-1],dotxx[12-1]],
         [y10,y11,y12],color=color) #轨枕，点10,11,12连接
plt.plot([x10+5000,x11+5000,dotxx[12-1]],
         [y10,y11,y12],color=color) #轨枕，点10,11,12连接

fontsize = 8 #调整图中字体的大小
locx=[200,200,-1800,-1800,-500,-2800,-1500,
     -3000,-3000,-1300,-1400,100,-500,-500]#调整对应点文字说明的位置，x轴
locy=[-200,-500,300,300,300,-1000,300,
      -1000,500,200,300,300,-1000,300]#调整对应点文字说明的位置，y轴
# 画点和点的说明
for l in range(14):
    if l in [3,4,10,11]:
        ax.scatter(linexs[l],lineys[l],s=30,c='k',marker='s')
        plt.text(linexs[l]+locx[l],lineys[l]+locy[l],
                 '{},{}:{}\n({:d},{:d})'.format(num[l],name[l],spec[l],linexs[l],lineys[l]),fontsize=fontsize)
    else:
        ax.scatter(linexs[l],lineys[l],s=30,c='red',marker='o')
        plt.text(linexs[l]+locx[l],lineys[l]+locy[l],
                 '{},{}:{}\n({:d},{:d})'.format(num[l],name[l],spec[l],linexs[l],lineys[l]),fontsize=fontsize)
plt.savefig('AT.png')

