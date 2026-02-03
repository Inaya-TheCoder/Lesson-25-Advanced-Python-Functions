a =[1,2,3,4,5]
b = [4,5,6,7,8]
result = map(lambda x,y: x*y, a,b)
print (list(result))

def square(x):
    return x*x
result_2 = map(square,a)
print (list(result_2))
print ("End of the code")