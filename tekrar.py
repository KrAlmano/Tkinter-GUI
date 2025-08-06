#Setler

set1 = set([1,2,4])
set2 = set([1,2,5])

set1.difference(set2)

set1.union(set2)

set1.isdisjoint(set2) #Kesisimleri bos mu?

set1.issubset(set2)


#Fonksiyonlar

def calculate(varm,moisture,charge):
    return int((varm+moisture)/charge)

calculate(1,2,3)


def standardization(a,p):
    return a*10/100*p*p

standardization(1,2)



def all_calculations(varm,moisture,charge,p):
    a = calculate(varm,moisture,charge)
    b = standardization(a,p)
    print(b*10)


all_calculations(4, 3,5,10)

#If-Else-Elif

def number_checker(number):
    if number ==10:
        print("equal to 10")
    elif number <10:
        print("less than 10")
    else:
        print("Greater than 10")


number_checker(9)



#Donguler


students = ["ahmet",'Furkan','Cayirtepe']

for x in students:
    print(x.upper())


salaries = [1000,2000,3000,4000,5000]

for salary in salaries:
    print(salary)


for salary in salaries:
    print(int(salary*20/100+salary))



def new_salary(salary,rate):
    return(int(salary*rate/100 + salary))

new_salary(1000,20)


for salary in salaries:
    print(new_salary(salary,10))


#Uygulama sorusu -> cift harfleri buyult

def alternating(string):
    new_string = ""
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i].upper()
        else:
            new_string += string[i].lower()

    print(new_string)


alternating("Almano")


#Enumerate





