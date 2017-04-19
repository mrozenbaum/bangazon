Bangazon Orientation - Defining Your Departments

Setup

mkdir -p workspace/python/orientation/bangazon && cd $_
touch bangazon.py
Instructions

Create a Department class. Create some simple properties and methods on Department. You are going to create some derived classes that inherit from Department, so make sure that the properties/methods you add are general to all Departments (e.g. name, supervisor, employee_count, etc).
Example property/method definition

```python

class Department(object):
  """Parent class for all departments"""

  def __init__(self):
      self.employees = set()

  @property
  def name(self):
    try:
      return self.__name
    except AttributeError:
      return ""

  @name.setter
  def name(self, val):
    if isinstance(val, str):
      raise TypeError('Please provide a string value for the department name')

    if val is not "" and len(val) > 1:
      self.__name = val
    else:
      raise ValueError("Please provide a department name")

  @property
  def supervisor(self):

    try:
      return self.__supervisor
    except AttributeError:
      return ""

  @supervisor.setter
  def supervisor(self, val):
    if not isinstance(val, str):
      raise TypeError('Please provide a string value for the supervisor name')

    if val is not "" and len(val) > 5:
      self.__supervisor = val
    else:
      raise ValueError("Please provide a supervisor name")

```
After you are happy with your Department class, create a derived class that defines a particular Department. Create some properties that apply only to that department.
The classes should, at the very least, set the initial value for the properties that you defined in the base class inside the constructor __init__.

Examples, include HR, IT, Marketing, Sales, etc.

```python
class HumanResources(Department):
  """Class for representing Human Resources department

  Methods: __init__, add_policy, get_policy, etc.
  """

  def __init__(self, name, supervisor, employee_count):
    super().__init__(name, supervisor, employee_count)
    self.policies = set()

  def add_policy(self, policy_name, policy_text):
    """Adds a policy, as a tuple, to the set of policies

    Arguments:
      policy_name (string)
      policy_text (string)
    """

    self.policies.add((policy_name, policy_text))
```
Create three more classes for departments of your choosing.
Create some instances of each department.
Assign values to the properties of each.
Use print() to output the name of each of your department instances.
hr_department = HumanResources(...)
print(hr_department.name)

Part 2:

Bangazon Orientation - Specializing Derived Classes with Overriding

Instructions

Override

Choose one of the general methods that you created in the Department class for overriding. For example, the meet() method which handles the logic of how teammates in that department gather for a meeting.
Override that method in all of your derived classes, giving each a more specialized implementation. For example, you could output a different meeting place for each department.
Override, but use parent

Now make a method on Department named get_budget(). It will set, and return, the base budget that each department gets each year. You pick what that number is.
Override that method in each of the derived classes.
Make sure you invoke the parent class' overridden method with the super keyword (e.g. super().get_budget()). That will set the base budget.
Now add, or subtract, from that base budget inside the derived class' override method to adjust that specific department's budget.
class Department(object):
  """Parent class for all departments

  Methods: __init__, get_name, get_supervisor, meet
  """

  def meet():
    print("Everyone meet in {}'s office".format(self.supervisor))
class Development(object):
  """Software development department

  Methods: __init__, get_name, get_supervisor, meet
  """

  def meet():
    """This overrides the base meet() method completely"""
    
    print("Everyone meet in the server room")

    Part 3:

    Bangazon Orientation - Method Overloading

Method overloading in Python uses a single method, but utilizes parameter names and default values. This allows a single method to have multiple signatures.

Instructions

Create a new class to represent an Employee.

It's constructor should accept two parameters.

First name of employee
Last name of employee
Define a method named eat() that will allow it to be invoked with the following four signatures.

eat() - Will select a random restaurant name from a list of strings, print to console that the employee is at that restaurant, and also return the restaurant.
eat(food="sandwich") - Will output that the employee ate that specific food at the office.
eat(companions=[Sam, Dean, Alice]) - Will select a random restaurant name from a list of strings, print to console that the employee is at that restaurant, and also output the first name of each employee in the specified list.
eat("pizza", [Sam, Dean, Alice]) - Will select a random restaurant name from a list of strings, print to console that the employee at that restaurant, and ordered the specified food, with the first name of the teammates specified in the list.
Note: Notice that this signature doesn't require that the parameters to be named


Part 4:

Bangazon Orientation - Method Overloading

Method overloading in Python uses a single method, but utilizes parameter names and default values. This allows a single method to have multiple signatures.

Instructions

Create a new class to represent an Employee.

It's constructor should accept two parameters.

First name of employee
Last name of employee
Define a method named eat() that will allow it to be invoked with the following four signatures.

eat() - Will select a random restaurant name from a list of strings, print to console that the employee is at that restaurant, and also return the restaurant.
eat(food="sandwich") - Will output that the employee ate that specific food at the office.
eat(companions=[Sam, Dean, Alice]) - Will select a random restaurant name from a list of strings, print to console that the employee is at that restaurant, and also output the first name of each employee in the specified list.
eat("pizza", [Sam, Dean, Alice]) - Will select a random restaurant name from a list of strings, print to console that the employee at that restaurant, and ordered the specified food, with the first name of the teammates specified in the list.
Note: Notice that this signature doesn't require that the parameters to be named

Part 5:

Bangazon Orientation - Aggregation

Instructions

For this exercise, you need to modify the Department class so that Employees can be aggregated into them. In its constructor, initialize an empty set named self.employees.

Create three new methods.

add_employee(self, employee) - Add an employee to the set. The employee parameter accepts an existing instance of an employee.
remove_employee(self, employee) - Removes an employee from the set. The employee parameter accepts an existing instance of an employee.
get_employees(self) - Returns the set of employees.
Write a module that creates an instance of each of your Departments that you have defined. Then create two or three Employee instances for each Department, and add them to the appropriate Department instance.

Once you have defined all of your Employees and Departments, write logic to output the name of each Department, and the first/last name of each employee it contains to the command line.

Example CLI Output

Department: Sales
   Andri Alexandrou
   Wayne Hutchinson
   Sephora Rodriguez
   Matt Qualls
   Jen Solima

Department: Technology
   Caitlin Stein
   Ryan Tanay
   Jessawynn Parker
   Damon Romano
Once you've completed this basic output, modify it to display any other properties that might be applied to either the Department or Employee that you added from the previous exercises (e.g. handicap, employment status, etc.)