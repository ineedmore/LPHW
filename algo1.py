class employee:
    def __init__(self,name="Anvar",emp_id="5545",exp=10,dept="R&D"):
        self.Name = name
        self.Emp_id = emp_id
        self.Exp = exp
        self.Dept = dept

    def calcSalary(self):
        if self.Exp > 5 and self.Dept == "R&D":
            self.Salary = 200000
        else:
            self.Salary = 80000

    def empDesc(self):
        print("Employee {} from {} department working with us for {} years".format(self.Name,self.Dept,self.Exp))


emp1 = employee()
emp1.Name
