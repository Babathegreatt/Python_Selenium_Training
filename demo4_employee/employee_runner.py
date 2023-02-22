from demo4_employee.employee_module import Employee

#assign value to static values
Employee.company_name = "ACN"
Employee.company_location = "Pune"

print(Employee.company_name)
print(Employee.company_location)

#Create objects

emp1 = Employee()
emp2 = Employee()
emp3 = Employee()

#print obect details

print(emp1)
print(emp2)
print(emp3)

#load employee 1 details

emp1.emp_id = 201
emp1.emp_name= "John"
emp1.emp_salary = 12000
emp1.emp_performance = "B"

#load employee 2 details

emp2.emp_id = 1
emp2.emp_name = "Dave"
emp2.emp_salary = 15000
emp2.emp_performance = "A"

#load employee 3 details

emp3.emp_id= 405
emp3.emp_name = "Raga"
emp3.emp_salary = 13000
emp3.emp_performance = "D"

print(emp1.emp_id, emp1.emp_name, emp1.emp_salary, emp1.emp_performance)
print(emp2.emp_id,emp2.emp_name,emp2.emp_salary,emp2.emp_performance)
print(emp3.emp_id,emp3.emp_name,emp3.emp_salary,emp3.emp_performance)

print(type(emp3))
print(type(emp1.emp_id))

Employee.print_author_name()

#Display Employee details
emp1.display_employee_record()
emp2.display_employee_record()
emp3.display_employee_record()

#Calculate bonus and print total salary
emp1.calculate_bonus()
emp2.calculate_bonus()
emp3.calculate_bonus()

emp1.display_employee_record()
emp2.display_employee_record()
emp3.display_employee_record()

emp1.set_company_code(100)
emp1.get_company_code()