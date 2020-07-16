from files import Files


class Employee:
    def __init__(self, id, first_name=None, last_name=None, position=None, manager=None ,manager_id =None, department=None ):
        self.id = id
        self.first_name=first_name
        self.last_name = last_name
        self.position = position
        self.manager = manager
        self.manager_id = manager_id #get from the excel pandas
        self.department = department
        Files.add_to_file(self.id,self.first_name,self.last_name,self.position,self.manager,self.manager_id,self.department)


    def change_first_name(self,name):
        self.first_name = name
        Files.change_info(self.id,self.first_name,title="first_name")

    def change_last_name(self,l_name):
        self.last_name = l_name
        Files.change_info(self.id,self.first_name,title="last_name")

    def change_position(self,position):
        self.position = position
        Files.change_info(self.id, self.position, title="position")

    def change_manager(self,manager,manager_id):
        self.manager = manager
        self.manager_id = manager_id
        Files.change_info(self.id, self.manager, title="manager")
        Files.change_info(self.id, self.manager_id, title="manager_id")

    def change_department(self,department):
        self.department = department
        Files.change_info(self.id, self.department, title="department")

    def delete_employee(self):
        Files.delete_employee(self.id)




x = Employee(6060,"rotem","cohen")
x.change_first_name("eli")

