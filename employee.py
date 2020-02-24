from pip._internal.commands.list import tabulate

emp = str(input("entr the employee name  "))
hrs = int(input("enter the number of hours employee works"))
pay_perhr = int(input("enter the pay of per hour"))
weeks = int(input("enter the number of weeks employee works"))

monthly_sal = hrs * pay_perhr * weeks
yearly_sal = monthly_sal * 12
'''print("employee data")
print(" ".join(emp))

'''
'''table=[[emp,monthly_sal,yearly_sal]]
headers=["name","monthly sal","yearly sal"]
print(tabulate(table, headers,tabble))


#print(tabulate({"Name": [emp],"monthly salary": [monthly_sal],"yearly salary":[yearly_sal]}))

#print(tabulate([["employee name", "monthly salry", "yearly salary"], [emp, monthly_sal, yearly_sal]], headers="firstrow"))
'''
print("monthly_sal=", monthly_sal)
print("yearly salaray=", yearly_sal)

if (yearly_sal <= 250000):
    print("Mr.", emp, "hurray! you have no tax to pay >>>>you have too much of black money")

elif (yearly_sal <= 500000):
    tax = (yearly_sal - 250000) * 0.05
    print("Mr.", emp, "you have to pay tax of rupee", tax)
elif (yearly_sal <= 1000000):
    tax = 12500 + 100000 + (yearly_sal - 1000000) * 0.3
    print("Mr.", emp, "you have to pay the tax of rupee", tax)

    print(tabulate([["employee name", "monthly salry", "yearly salary"], [emp,monthly_sal,yearly_sal]],headers="firstrow"))
