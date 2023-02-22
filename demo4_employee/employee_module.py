class Employee:
    company_name = None  # static or class variable
    company_location = None

    def __init__(self):
        self.emp_id = None  # non-static or instance variable
        self.emp_name = None
        self.emp_salary = None
        self.emp_performance = None
        self.__company_code = 0 #private variable

    @staticmethod
    def print_author_name():
        print('author name is :', 'Gaurav Inamdar')

    def display_employee_record(self):
        print(35 * "-")
        print("Employee ID: ", self.emp_id)
        print("Employee name: ", self.emp_name)
        print("Employee Salary: ", self.emp_salary)
        print("Employee performance: ", self.emp_performance)
        print("Company Name: ", Employee.company_name)
        print("Company Location: ", self.company_location)
        print(15 * "-")

    #getter method
    def get_company_code(self):
        print(self.__company_code)

    #setter method
    def set_company_code(self, company_code):
        self.__company_code = company_code

    def calculate_bonus(self):
        if self.emp_performance == "A":
            bonus = (self.emp_salary * 10) / 100
        elif self.emp_performance == "B":
            bonus = (self.emp_salary * 5) / 100
        elif self.emp_performance == "C":
            bonus = (self.emp_salary * 2) / 100
        else:
            bonus = 0
        self.emp_salary = self.emp_salary + bonus

