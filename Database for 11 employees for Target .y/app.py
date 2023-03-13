from Employee_database import Employee_database

employee_1 = Employee_database("Sarah Ponds","1067890", 
                               "Senior dev ops manager", "sponds@targetops.com", 
                               "ZBEQWio90910!!", 150120.160, "Times Square", "not active")
print(employee_1.salary)

employee_2 = Employee_database("Kenneth Bridgeman","12983030", 
                               "Senior Electrical engineer manager", "kbridgeman@targetops.com", 
                               "Qwrz90910!!", 150120.160, "Times Square", "active")
print(employee_2.position)

employee_3 = Employee_database("James Buchanan","1067890", 
                               "Senior dev ops manager", "jbuchanan@targetops.com", 
                               "BOBILop9018!!", 150120.160, "Times Square", "active")
print(employee_3.email)

employee_4 = Employee_database("Christina williams","1067890", 
                               "Senior dev ops manager", "jbuchanan@targetops.com", 
                               "Qwrz90910!!", 150120.160, "Times Square", "active")
print(employee_4.position)

employee_5 = Employee_database("James Buchanan","1067890", 
                               "Senior dev ops manager", "jbuchanan@targetops.com", 
                               "Qwrz90910!!", 150120.160, "Times Square,", "not active")
print(employee_5.generic_password)

employee_6 = Employee_database("James Buchanan","1067890", 
                               "Senior dev ops manager", "jbuchanan@targetops.com", 
                               "Qwrz90910!!", 150120.160, "Times Square", "not active")
print(employee_6.office_name)

employee_7 = Employee_database("James Buchanan","1067890", 
                               "Senior dev ops manager", "jbuchanan@targetops.com", 
                               "Qwrz90910!!", 150120.160, "Times Square","not active")
print(employee_7.salary)

employee_9 = Employee_database("James Buchanan","1067890", 
                               "Senior dev ops manager", "jbuchanan@targetops.com", 
                               "Qwrz90910!!", 150120.160, "Times Square", "active")
print(employee_9.active_user)

employee_10 = Employee_database("James Buchanan","1067890", 
                               "Senior dev ops manager", "jbuchanan@targetops.com", 
                               "Qwrz90910!!", 150120.160, "Times Square","not active")
print(employee_10.position)

employee_11 = Employee_database("James Buchanan","1067890", 
                               "Senior dev ops manager", "jbuchanan@targetops.com", 
                               "Qwrz90910!!", 150120.160, "Times Square", "active")
print(employee_11.salary)
