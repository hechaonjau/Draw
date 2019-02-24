import matplotlib.pyplot as plt
n=1
acc_n = 0
loss_n = 0
acc_x = []
acc_y = []
loss_x = []
loss_y = []
with open("3.log") as txt:       #打开文件
    for line in txt:
        line = line.strip()      #去除多余空格
        if n%432 == 0:           #每一轮打印一次（每轮迭代次数为432）
            line1=line.split('acc:',1)      #在“acc：”处切割字符串分成2个
            a=(float(line1[1].split(',')[0]))*0.01   #再次在“，”处切割字符串，并选取第一个字符串，再将字符串转为浮点数
            acc_y.append(round(a,4))                #保留4位小数
            acc_x.append(acc_n)
            acc_n += 1
            line3=line.split('loss:',1)
            loss_y.append(float(line3[1].split(',')[0]))
            loss_x.append(loss_n)
            loss_n += 1
        n += 1
#绘图部分
print(acc_x,acc_y)
print(loss_x,loss_y)
plt.figure(figsize=(8,6))
plt.plot(acc_x,acc_y,'',label="acc")
plt.plot(loss_x,loss_y,'',label="loss")
plt.title('loss_acc')
plt.legend(loc='upper right')   #显示图例，loc表示位置
plt.xlabel('Epoch')             #x轴名称
plt.ylabel('')
plt.grid()                      #显示网格线
plt.show()