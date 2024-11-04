from faker import Faker

fake = Faker()
# print(fake.name())
# print(fake.address())
# print(fake.text())

def triangle_type(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        if a==b and b==c:
            return 'Triangle is Equilateral.'
        elif a==b or b==c or a==c:
            return 'Triangle is Isosceles.'
        else:
            return 'Triangle is Scalane'
    else:
        return 'Triangle is not possible from given sides.'

Faker.seed(0)
# for _ in range(5):
#     print(fake.random_int(min=0, max=15))
print("---------------------------------------------------------------------------------------------")
for _ in range(15):
    a = fake.random_int(min=0, max=15)
    b = fake.random_int(min=0, max=15)
    c = fake.random_int(min=0, max=15)
    print("a = " + str(a) + " b = " + str(b) + " c = " + str(c) + "  " + triangle_type(a,b,c))
print("---------------------------------------------------------------------------------------------")
for _ in range(5):
    a = fake.random_int(min=-5, max=0)
    b = fake.random_int(min=0, max=15)
    c = fake.random_int(min=0, max=0)
    print("a = " + str(a) + " b = " + str(b) + " c = " + str(c) + "  " + triangle_type(a,b,c))
print("---------------------------------------------------------------------------------------------")
for _ in range(5):
    a = fake.random_digit()/10
    b = fake.random_digit()/10
    c = fake.random_digit()/10
    print("a = " + str(a) + " b = " + str(b) + " c = " + str(c) + "  " + triangle_type(a,b,c))


