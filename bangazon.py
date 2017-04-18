import random

class Department(object):
    """Parent class for all departments"""

    def __init__(self, name, supervisor, employee_count, location):
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count
        self.location = location

        self.budget = 55,000
        self.employees = set()
    
    def get_budget(self):
        self.budget = 500000
        return self.budget
        print(self.budget)

    def get_department_name(self):
        return self.name

    def get_supervisor(self):
        return self.supervisor

    def get_location(self):
        return self.location

    def get_employee_count(self):
        return self.employee_count

    def get_employees(self):
        return self.employees


class Employee():
    ''' Employee Class '''
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



class HumanResources(Department):
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

   hr_department = HumanResources('Human Resources', 'Kat Von D', 'California', 5)
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
   print(miriam.eat())
   miriam.eat(food="buritto")
   miriam.eat(companions =["Ruthie", "Dara", "Casey"])
   miriam.eat(food="taco", companions= ["Casey", "Ruthie", "Dara"])




