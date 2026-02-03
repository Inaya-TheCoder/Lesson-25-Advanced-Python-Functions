a = [1,2,3,4,5]
b = [4,5,6,7,8]
result = zip(a,b)
print(list(result))


for x, y in zip(b,a[::-1]):
    print(x,y)


Company= ["Google","Microsoft","Apple"]
Founder= ["Larry Page","Bill Gates","Steve Jobs"]
result_2 = {company: founder for company, founder in zip(Company, Founder)}
print ('\n{}'.format(result_2))