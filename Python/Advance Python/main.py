# import matplotlib.pyplot as plt
from time import sleep
from csv import reader,DictReader
# file=open('sample.txt','w')
# file.write("Python is easy\n")
# file.writelines(['Sql is easy\n','Maths is easy\n','ML is easy\n'])

# with open('sample.txt','w') as file:
#     file.write("Python is easy\n")
#     file.writelines(['Sql is easy\n','Maths is easy\n','ML is easy\n','RCB lost\n'])

# with open('demo.txt','r') as f:
#     print(f.read())
#     print(f.readline())
#     print(f.readlines())

# with open(r"C:\Users\rajar\Downloads\sample1 (1).txt") as f:
#     # lst=[]
#     # for line in f:
#     #     if line.strip():
#     #         lst.append(line.split()[2])
#     lst = [line.split()[2] for line in f if line.strip()]
# print(f"Total number of messages is {len(lst)}")
# print(f"Total number of unique messages is {len(set(lst))}")
# print({msg:lst.count(msg) for msg in lst})

# code optimization
# def message_analysis(path):
#     with open(path) as f:
#         lst = [line.split()[2] for line in f if line.strip()]
#     print(f"Total number of messages is {len(lst)}")
#     print(f"Total number of unique messages is {len(set(lst))}")
#     print({msg:lst.count(msg) for msg in lst})

# message_analysis(r"C:\Users\rajar\Downloads\sample1 (1).txt")

# with open('demo.txt','a') as f :
#     f.write(" Hello\n")

# with open ('emp.txt','w') as f:
#     f.write("ID, NAME, AGE, GENDER, SALARY\n")
#     f.writelines(["101, steve jobs, 30, male, 50000\n","102, bill gates, 40, male, 60000\n",
#     "103, anna, 25, female, 25000\n"])

# with open ("emps.csv.xls") as f:
#     for line in f:
#         print(line)
#         sleep(1)

##with open("emps.csv.xls") as f:
##    rows=reader(f)
##    header_row=next(rows)
##    lst_emps=[]
##    for row in rows:
##        lst_emps.append(row)

# def total_pay():
#     Sum=0
#     for emp in lst_emps:
#         Sum+=int(emp[-4])
#     return Sum

# def emp_count_gender():
#     gender={}
#     for emp in lst_emps:
#         if emp[2] not in gender:
#             gender[emp[2]]=1
#         else:
#             gender[emp[2]]+=1
#     return gender


# print("Total Pay :" , total_pay())
# print(emp_count_gender())

# def department_count():
#     department={}
#     for emp in lst_emps:
#         if emp[3] not in department:
#             department[emp[3]]=1
#         else:
#             department[emp[3]]+=1
#     return department

#print(department_count())

# def gender():
#     for emp in lst_emps:
#         male,female=0,0
#         if emp[2]=="Male":
#             male+=1
#         else:
#             female+=1
#     return male,female

# print(gender())

##Salary
##lst_sorted_emp_data=sorted(lst_emps,key=lambda emp:int(emp[-4]))
##
##for emp in lst_sorted_emp_data:
##    print(emp[1],emp[-4])

##Young Employee
##lst_sorted_emp_age=sorted(lst_emps,key=lambda emp:int(emp[6]))
##print(f'The Youngest employee is {lst_sorted_emp_age[0][1]}')
##
####Oldest Employee
##print(f'The Oldest employee is {lst_sorted_emp_age[-1][1]}')


##Dictionary
##with open("emps.csv.xls") as f:
##    rows=DictReader(f)
##    for row in rows:
##        print(row)
##        sleep(1)

##def emp_data(path):
##    lst_emps=[row for row in DictReader(open(path))]
##    return lst_emps
##
##file_path="emps.csv.xls"
##lst_emp_data=emp_data(file_path)
##
##def count_city():
##    city_count={}
##    for emp in lst_emp_data:
##        if emp["City"] not in city_count:
##            city_count[emp["City"]]=1
##        else:
##            city_count[emp["City"]]+=1
##            
##    return city_count
##print(count_city())

# with open('data.csv','w+') as file:
#     file.write('Emp_ID,Name,Gender,Department,Designation,City,Age\n')
#     file.writelines(['101,Amit Sharma,Male,IT,Python Developer,Mumbai,26\n']['102,Priya Mehta,Female,HR,HR Executive,Pune,29\n'])
#     file.seek(0)
#     print(file.read())


