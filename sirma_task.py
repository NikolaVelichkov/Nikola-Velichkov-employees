import datetime

class Employee:
    def __init__(self,EmpID,ProjectID,DateFrom,DateTo):
        self.EmpID = EmpID
        self.ProjectID = ProjectID
        self.DateFrom = DateFrom
        self.DateTo = DateTo
        self.chek_dates()
        self.to_date_format()

    def chek_dates(self):
        if self.DateTo == 'NULL':
            now = datetime.datetime.now()
            year = str(now.year)
            month = str(now.month)
            day = str(now.day)
            date = year + '-' + month + '-' + day

            self.DateTo = date
    def to_date_format(self):
        self.DateFrom = datetime.datetime.strptime(self.DateFrom, '%Y-%m-%d')
        self.DateTo = datetime.datetime.strptime(self.DateTo, '%Y-%m-%d')
           

def read_file():
    filepath = 'input.txt'
    information =''
    for i in filepath:
        with open(filepath) as fp:  
            line = fp.read()
            information = line
    information = information.replace(',',' ')
    information = information.split()
    return information

def create_objects(arr):
    employees = []
    for i in range(0,len(arr),4):
        
        employees.append(Employee(arr[i],arr[i+1],arr[i+2],arr[i+3]))
    return employees
def sort(arr):
    sorted_by_project = sorted(arr, key=lambda x: x.ProjectID)
    return sorted_by_project

def check_if_overlapse(emp1,emp2):
    if (emp1.DateFrom < emp2.DateFrom and emp1.DateTo < emp2.DateTo) or (emp1.DateFrom > emp2.DateFrom and emp1.DateTo > emp2.DateTo):
        return
    else:
        if (emp1.DateFrom <= emp2.DateFrom) and (emp2.DateTo <= emp1.DateTo):
            return -(emp2.DateFrom - emp2.DateTo)
        elif (emp1.DateFrom >= emp2.DateFrom) and (emp2.DateTo >= emp1.DateTo):
            return -(emp1.DateFrom - emp1.DateTo)
        elif (emp1.DateFrom <= emp2.DateFrom and emp1.DateTo <= emp2.DateTo):
            return -(emp2.DateFrom - emp1.DateTo)
        elif (emp2.DateFrom <= emp1.DateFrom) and (emp2.DateTo <= emp1.DateTo):
            return -(emp1.DateFrom - emp2.DateTo)
    
def max(days):
   value = datetime.datetime.strptime('2010-01-01', '%Y-%m-%d')
   value1 = datetime.datetime.strptime('2010-01-02', '%Y-%m-%d')
   holder = value1-value
   keyholder = ''
   for x,y in days.items():
        if type(y) != int:
                if y > holder:
                     holder = y
                     keyholder = x
       
   print('The two employees are: ' +keyholder[0:3]+ ' and ' +keyholder[3:6])


def calculate_time_on_project(arr):
    sorting_dict = {}
    for i in arr:
        for j in arr:
            if i.EmpID!=j.EmpID:
                if i.ProjectID == j.ProjectID:
                    if (i.EmpID + j.EmpID) in sorting_dict.keys():
                        try:
                            sorting_dict[i.EmpID + j.EmpID] += check_if_overlapse(i,j)
                        except:
                            continue
                    elif (j.EmpID + i.EmpID) not in sorting_dict.keys():
                        
                        sorting_dict[i.EmpID + j.EmpID] = check_if_overlapse(i,j)
                       
    for x,y in sorting_dict.items():
        if y == None:
            sorting_dict[x] = 0
             
    max(sorting_dict)
    
     
def main():
    from_txt = read_file()
    arr_object_emp = create_objects(from_txt)
    emp_sorted = sort(arr_object_emp)
    calculate_time_on_project(emp_sorted)
    
    
if __name__ == "__main__":
    main()

