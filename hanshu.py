# -*- coding: utf-8 -*-
"""
Created on Fri May  4 10:14:38 2018

@author: xgb
"""
import matplotlib.pyplot as plt
#daoru mokuai
fig=plt.figure()
ax=fig.add_subplot(111)
#tianjiahanzi
from matplotlib.font_manager import FontProperties  
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=18) 
plt.title(u'复线AT牵引供电系统实例参数',fontproperties=font_set)
#fanwei he mingzi
ax.axis([-5000,10000,0,10000])
#hexindian
filename = 'test1.txt'
linexs=[]
lineys=[]
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [int(s) for s in line.split()]
        ax.scatter(value[0],value[1],s=30,c='red',marker='s')
        linexs.append(value[0])
        lineys.append(value[1])
plt.text(linexs[0]-1200,lineys[0]-1800 ,'坐标原点\n({:d},{:d})'.format(linexs[0],lineys[0]),fontsize=12,fontproperties=font_set)
plt.text(linexs[1]-2500,lineys[1]+300 ,'  R1:P60\n({:d},{:d})'.format(linexs[1],lineys[1]),fontsize=12,fontproperties=font_set)
plt.text(linexs[2]-800,lineys[2]+300 ,'  R2:P60\n({:d},{:d})'.format(linexs[2],lineys[2]),fontsize=12,fontproperties=font_set)
plt.text(linexs[3]-3000,lineys[3]+300 ,'  PF:LGJ185\n({:d},{:d})'.format(linexs[3],lineys[3]),fontsize=12,fontproperties=font_set)
plt.text(linexs[4]-1500,lineys[4]-1300 ,'  PW:LGJ120/20\n({:d},{:d})'.format(linexs[4],lineys[4]),fontsize=12,fontproperties=font_set)
plt.text(linexs[5],lineys[5] ,'  MW:TJ-95\n({:d},{:d})'.format(linexs[5],lineys[5]),fontsize=12,fontproperties=font_set)
plt.text(linexs[6]-300,lineys[6]-1000 ,'  CW:CTHA-120\n({:d},{:d})'.format(linexs[6],lineys[6]),fontsize=12,fontproperties=font_set)
plt.text(linexs[7]-2200,lineys[7]+300 ,'  R1:P60\n({:d},{:d})'.format(linexs[7],lineys[7]),fontsize=12,fontproperties=font_set)
plt.text(linexs[8]-900,lineys[8]+300 ,'  R2:P60\n({:d},{:d})'.format(linexs[8],lineys[8]),fontsize=12,fontproperties=font_set)
plt.text(linexs[9]-300,lineys[9]-1000 ,'  CW:CTHA-120\n({:d},{:d})'.format(linexs[9],lineys[9]),fontsize=12,fontproperties=font_set)
plt.text(linexs[10]-2000,lineys[10]+300 ,'  MW:TJ-95\n({:d},{:d})'.format(linexs[10],lineys[10]),fontsize=12,fontproperties=font_set)
plt.text(linexs[11]-1100,lineys[11]-1300 ,'  PW:LGJ120/20\n({:d},{:d})'.format(linexs[11],lineys[11]),fontsize=12,fontproperties=font_set)
plt.text(linexs[12]-100,lineys[12]-300 ,'  PF:LGJ185\n({:d},{:d})'.format(linexs[12],lineys[12]),fontsize=12,fontproperties=font_set)
#plt.text(linexs[13]-1200,lineys[13]+300 ,'  E1\n({:d},{:d})'.format(linexs[13],lineys[13]),fontsize=12,fontproperties=font_set)
#plt.text(linexs[14]-1200,lineys[14]+300 ,'  E1\n({:d},{:d})'.format(linexs[14],lineys[14]),fontsize=12,fontproperties=font_set)

import matplotlib.pyplot as plt
#daoru mokuai
#hexin xian
plt.plot([5000,5000],[0,7500])
plt.plot([0,0],[0,7500])
plt.plot([-755,755],[1000,1000])
plt.plot([4245,5755],[1000,1000])
#fuzhu xian zuo
plt.plot([-3000,-3000],[0,9000])
plt.plot([-2500,-2500],[0,9000])
plt.plot([-3000,-2500],[9000,9000])
plt.plot([-3000,-500],[8200,8200])
plt.plot([-3000,-500],[6300,8200])
plt.plot([0,0],[0,10000])
plt.plot([-1500,-800],[0,1000])
plt.plot([800,1500],[1000,0])
#fuzhu xian you
plt.plot([8000,8000],[0,9000])
plt.plot([7500,7500],[0,9000])
plt.plot([7500,8000],[9000,9000])
plt.plot([5255,8000],[8200,8200])
plt.plot([5255,8000],[8200,6300])
plt.plot([5000,5000],[0,10000])
plt.plot([3500,4200],[0,1000])
plt.plot([5800,6500],[1000,0])