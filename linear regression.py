import numpy as np

data = [[1, 15],[2,26],[3,37],[4,45],[5,63]]
x = [i[0] for i in data]
y = [i[1] for i in data]
    
mx = np.mean(x)
my = np.mean(y)

er = sum((i - mx)**2 for i in x)

def ed (x, mx, y, my) :
    d = 0
    for i in range(len(x)) : 
        d += (x[i] - mx) * (y[i] - my)
    return d

ed = ed(x, mx, y, my)

a = ed / er
b = my - (mx * a)
error_avg = 0

for i in range(len(x)) : 
    f = a * x[i] + b
    error = abs(f - y[i])
    error_avg += error**2
    print("x :", x[i], "   y :", y[i], "   예측 y : %.1f" %f, "   Error = %.1f" %error)
    
print("평균 제곱 오차(MSE): %.1f" % (error_avg / len(x)))
print("y = %.1f" %a, "x + %.1f" %b)
