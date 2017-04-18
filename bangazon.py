class Department(object):
    """Parent class for all departments"""

    def __init__(self, name, supervisor):
        self.name = name
        self.supervisor = supervisor

        self.employees = set()

    def get_name(self):
        return self.name

    def get_supervisor(self):
        return self.supervisor


class HumanResources(Department):
    """Class for representing Human Resources department

    Methods: __init__, add_policy, get_policy, etc.
    """
    def __init__(self, name, supervisor):
        super().__init__(name, supervisor)
        self.name = name
        self.supervisor = supervisor

        self.policies = set()        

    def add_policy(self, policy_name, policy_text):
        self.policy_name = policy_name
        self.policy_text =policy_text

        self.policies.add((policy_name, policy_text))


class IT(Department):
    ''' Class representing IT department

    Methods: __init__ & add_computer 
    '''
    def __init__(self, name, supervisor):
        super().__init__(name, supervisor, employee)
        self.name = name
        self.supervisor = supervisor

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


class Marketing(Department):
    ''' Class representing Marketing department

    Methods: __init__ & add_sale 
    '''
    def __init__(self, name, supervisor):
        super().__init__(name, supervisor)
        self.name = name
        self.supervisor = supervisor


if __name__ == '__main__':
