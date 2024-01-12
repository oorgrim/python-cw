import employee_module as emp_mod

new_employee_res = emp_mod.newEmployee("\nСабина Кункаева", "01.01.2000", "Бизнесмен", 500000)
print(new_employee_res)

new_employee_res = emp_mod.newEmployee("\nКан Эрик", "02.03.2002", "Менеджер", 600000)
print(new_employee_res)

fire_employee_res = emp_mod.fireEmployee(1)
print(fire_employee_res)

employeeId = emp_mod.getEmployeeId("\nЭрик")
print(f"\nID сотрудника: {employeeId}")

employeeRecord = emp_mod.getEmployeeRecord(employeeId)
print(employeeRecord)

fired_employees = emp_mod.getFiredEmployees()
print("\nУволенные сотрудники:")
for employee in fired_employees:
    print(employee)

total_salary = emp_mod.getTotalSalary()
emp_mod.min_salary, emp_mod.max_salary, emp_mod.avg_salary, emp_mod.median_salary = emp_mod.getMinMaxAvgSalary()

print(f"Общий размер зарплатного фонда компании: {total_salary}")
print(f"Минимальная зарплата: {emp_mod.min_salary}")
print(f"Максимальная зарплата: {emp_mod.max_salary}")
print(f"Средняя зарплата: {emp_mod.avg_salary}")
print(f"Медианная зарплата: {emp_mod.median_salary}")


olders = emp_mod.get_employee_list(lambda x: x['birthDate'][-4:] > "1980")
print(olders)