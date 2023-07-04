#With a single integer as the input,
#generate the following until a = x
#[series of numbers as shown in below examples]

#Output: (examples)
#1) input a = 1, then output : 1
#2) input a = 2, then output : 1, 3
#3) input a = 3, then output : 1, 3, 5
#4) input a = 4, then output : 1, 3, 5, 7
#5) input a = x, then output : 1, 3, 5, 7.

def generate_series(n):
    series=[]
    num=1
    incre=2

    while len(series)<n:
        series.append(num)
        num+=incre
        incre+=0

    return series

n=4
op=generate_series(n)
print(op)
