import random

class Department():
    """Parent class for all departments"""

    def __init__(self, name, supervisor, location, employee_count):
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count
        self.location = location
        self.budget = 550000
        self.employees = set()
    
    def get_department_name(self):
        return self.name


    def get_budget(self):
        self.budget = 500000
        return self.budget
        print(self.budget)


    def get_supervisor(self):
        return self.supervisor

    def get_location(self):
        return self.location

    def add_employee(self, employee):
        employee_status = ''
        try:
            employee_status = ' hours per pay period: ' + str(employee.hours_per_pay_period)
        except(AttributeError, NameError):
            pass

        try:
            if employee.access_card == True:
                employee_status += ' has ACCESS CARD '
        except(AttributeError, NameError):
            pass

        try:
            employee__name = employee.first_name + ' ' + employee.last_name + employee_status + self.employees.add(employee_name)
        except(AttributeError, NameError):
                print('Add an Employee')               


    def remove_employee(self, employee):
        try:
            employee_name = employee.first_name + ' ' + employee.last_name + self.employees.remove(employee_name)
        except AttributeError:
                print("Add an employee")
        except KeyError:
                print("Employee not found")

                            
    def get_employee_count(self):
        return self.employee_count


    def get_employees(self):
        print("Department: {}\n\t{}".format(self.name, ("\n\t".join(self.employees))))


    @property
    def name(self):
        try:
            return self.__name
        except AttributeError:
            return ""

    @name.setter
    def name(self, val):
        if len(val) > 1:
            self.__name = val
        else:
            raise ValueError('Please enter a department name')
                
    @property
    def supervisor(self):
        try:
            return self.__supervisor
        except AttributeError:
            return ""

    @supervisor.setter
    def supervisor(self, val):
        if len(val) > 4:
            self.__supervisor = val
        else:
            raise ValueError('Please enter a supervisor name longer than 4 characters')                        

class Employee():
    '''Class representing an employee
    Methods: eat
    '''

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return '{}, {}'.format(self.first_name, self.last_name)

    def eat(self, food = None, companions = None):
        restaurant_list = ['McDonalds', 'Chipotle', 'Subway', 'Baskin Robins', 'Burger King', 'Wendys', 'Taco Bell', 'Panda Express', 'Sbarro', 'Wich Wich', 'Sonic', 'Starbucks']
        restaurant_choice = random.choice(restaurant_list)

        if companions is None and food is not None:
            print('{} ate  {} at work today.'.format(self.first_name, food))
        elif companions is None and food is None:
            print('{} ate alone at {}.'.format(self.first_name, restaurant_choice))
            return restaurant_choice

        elif companions is not None and food is None:
            print('{} ate at {} with {}.'.format(self.first_name, restaurant_choice,(','.join(companions))))

        elif companions is not None and food is not None:
            print('{} ate {} at {} with {}.'.format(self.first_name, food, restaurant_choice, (','.join(companions))))



class Full_Time():
    ''' Class representing full-time employee'''
    def __init__(self):
        self.hour_per_week = 40



class Part_Time():
    ''' Class representing part-time employee '''
    def __init__(self):
        self.hour_per_week = 25




class Access_Card():
    def __init__(self):
        self.access_card = True




class Human_Resources_Employee(Employee, Full_Time):

    ''' Class Representing Human Resources Employee '''

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        Full_Time.__init__(self)                                                

class IT_Employee(Employee, Part_Time, Access_Card):

    ''' Class Representing Human Resources Employee '''

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        Part_Time.__init__(self)
        Access_Card.__init__(self)


class Marketing_Employee(Employee, Full_Time, Access_Card):

    ''' Class Representing Human Resources Employee '''
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        Full_Time.__init__(self)


class Human_Resources(Department):
    """Class for representing Human Resources department

    Methods: __init__, add_policy, get_policy, etc.
    """

    def __init__(self, name, supervisor, employee_count, location):
        super().__init__
        # (name, supervisor, employee_count, location)
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count
        self.location = location
        self.budget = super().get_budget() + 5000
        self.policies = set()        

    def add_policy(self, policy_name, policy_text):
        self.policy_name = policy_name
        self.policy_text =policy_text

        self.policies.add((policy_name, policy_text))

    def get_budget(self):
        '''Sets the base budget and adds for the dept'''
        self.budget = super().get_budget() + 50000
        print(self.budget)    

    # def meet(self):    


class IT(Department):
    ''' Class representing IT department

    Methods: __init__ & add_computer 

    '''
    def __init__(self, name, supervisor, employee_count, location):
        super().__init__
        # (name, supervisor, employee_count, location)
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count
        self.location = location
        self.budget = super().get_budget() - 8000
        self.computer_dict = dict()

    def add_computer(self, computer_id, employee_id):
        ''' Adds a new computer to the computer_dict as a 'key'. If no employeeId is entered it will be assigned Not Registered.

        Arguments:
        computer_id - (string)
        employee_id - (string)
        '''
        self.computer_id = computer_id
        self.employee_id = employee_id
        self.computer_dict[computer_id] = employee_id

    def get_budget(self):
        '''Sets the base budget and adds for the dept'''
        self.budget = super().get_budget() + 40000
        print(self.budget)    


class Marketing(Department):
    ''' Class representing Marketing department

    Methods: __init__ & add_sale 
    '''
    def __init__(self, name, supervisor, employee_count, location):
        super().__init__
        # (name, supervisor, employee_count, location)
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count
        self.location = location

        self.budget = super().get_budget() - 10000

    def get_budget(self):
        '''Sets the base budget and adds for the dept'''
        self.budget = super().get_budget() + 1000000
        print(self.budget)    




if __name__ == '__main__':

   hr_department = Human_Resources('Human Resources', 'Kat Von D', 'California', 5)
   marketing_department = Marketing('Marketing', 'Beyonce', 'Texas', 10)
   it_department = IT('Information Technology', 'George Cloony', 'California', 15)
   # Prints the name of each of department instances (exercise 1)
   print(hr_department.name)
   print(marketing_department.name)
   print(it_department.name)

   hr_department.add_policy('Abuse Free Zone', 'Employees can not display or engage in any verbal, physical, emotional, or any other kid of  abuse or violence.')
   print(hr_department.policy_name)
   print(hr_department.policy_text)
   # #Prints adjusted budget for each department (exercise 2)
   print('hr_department budget=', hr_department.budget)
   print('marketing_department budget =', marketing_department.budget)
   print('it_department budget =', it_department.budget)

   #Prints statements from method overloadng (exercise 3)
   miriam = Employee("Miriam", "Rozenbaum")
   print(miriam)
   print('--------this is miriam.eat():', miriam.eat())
   miriam.eat('banana', ['Ruthie', 'Dara', 'Casey'])
   miriam.eat(companions =["Ruthie", "Dara", "Casey"])
   miriam.eat(food="sandwich", companions= ["Casey", "Ruthie", "Dara"])




