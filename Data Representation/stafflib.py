

employee = {"first_name":'',"last_name":'',"age":'',
            "since":'',"salary":'',"role":'',"days":''}
storeAllData = []

def newEmployee(Fn,Ln,Age,Since,Salary,Role,Days):
    """
    This function create data for new employees
    :param Fn: first_name
    :param Ln: last_name
    :param Age: age
    :param Since: since
    :param Salary: salary
    :param Role: role
    :param Days: days
    :return:
    """
    employeeC = employee.copy()
    employeeC["first_name"] = Fn
    employeeC["last_name"] = Ln
    employeeC["age"] = Age
    employeeC["since"] = Since
    employeeC["salary"] = Salary
    employeeC["role"] = Role
    employeeC["days"] = Days
    storeAllData.append(employeeC)



def showEmployee():
    """
    This function prints out all the employees' condition
    :return:
    """
    n=1
    print("Showing registre of employees:")
    for employee in storeAllData :
        print("Staff #" + str(n) + ":",employee["first_name"],employee["last_name"],"age",employee["age"]
          ,"has been working",str(employee["days"]),"days","since",employee["since"],"as a",employee["role"],"for USD" + employee["salary"] + ',')
        n+=1
        employee["days"] += 1
        #incrementDay(employee["days"])
    print("Task Completed.")
    print("")

""" not able to function...
def incrementDay(day):
    This function increase the original day by 1
    :param day: original days
    :return:

    day+=1
"""

def deleteEmployees(num):
    """
    Enter a number to show which staff you are deleting from the list
    :param num: staff's number (position)
    :return:
    """
    storeAllData.pop(num-1)

