class Employee_database:
    def __init__(self, name, emplid, position, email, generic_password, salary, office_name, active_user):
        self.name = name
        self.emplid = emplid
        self.position = position
        self.email = email
        self.generic_password = generic_password
        self.salary = salary
        self.office_name = office_name
        self.active_user = active_user

    def __salary__over__100k(self):
        if self.salary > 100000:
            return True
        else:
            return False
        
    def __active__user(self):
        for employee in range (11):
            if self.active_user == str ("active"):
                break 
            print("Active user" + str(self.name))
        else:
            return False
        print("not active user")

