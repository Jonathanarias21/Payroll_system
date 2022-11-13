from tabulate import tabulate

employee_list = []

while len(employee_list) < 11:
    employee_name = input("Enter Your Name")
    pay_rate = float(input("What is your hourly wage?"))
    hours_worked = float(input("How many hours did you work this week?"))
    overtime_rate = pay_rate*1.5
    
    if hours_worked > 40:
        regular_pay = pay_rate*hours_worked
        overtime_pay = regular_pay+overtime_rate
        gross_pay = regular_pay+overtime_pay
    else:
        regular_pay = pay_rate*hours_worked
        overtime_pay = 0
        gross_pay = regular_pay+overtime_pay 

    fed_tax = round(gross_pay*.1)
    state_tax = round(gross_pay*.06)
    fica = round(gross_pay*.03)
    net_pay = gross_pay-(fed_tax+state_tax+fica)
    res = employee_name, hours_worked, pay_rate, regular_pay, overtime_pay, gross_pay, fed_tax, state_tax, fica, net_pay
    employee_list.append(res)
     

headers_table = 'Employee Name', 'Hours Worked', 'Pay Rate', 'Regular Pay', 'Overtime Pay', 'Gross Pay', 'Fed Tax', 'State Tax', 'FICA', 'Net Pay'    
print(tabulate(employee_list, headers=headers_table, tablefmt='rounded_grid'))
