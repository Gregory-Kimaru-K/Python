class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

company = Company("Krusty Krab")
company.add_employee("Greg", "Sr. Software Developer")
company.add_employee("Adam", "Jr. Software Developer")
company.add_employee("SpongeBov", "Machine Learning Engineer")

print(company.company_name)
for employee in company.list_employees():
    print(employee)