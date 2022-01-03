from matplotlib import pyplot as plt
x = [2001, 2002, 2003,2004,2005,2006,2007]
y = [2400, 22500, 19700,17500, 14500,10000,5800]
plt.plot(x,y)
plt.title("value depreciation",loc='left')
plt.plot(x,y,linestyle='dashdot', marker = '*',ms='20',mfc = 'g',color='red')
plt.show()


