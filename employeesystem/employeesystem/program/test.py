from employee import Employee

class Testing:
    def __init__(self):
        self.employee_test()

    def employee_test(self):
        print("[TEST] employee")
        x = Employee(505050)
        y = Employee(2012,"dorin","zrihen","photoshop","beni","website")
        assert x.id == 505050
        assert y.first_name == "dorin"
        assert y.last_name == "zrihen"
        assert y.position == "photoshop"
        assert y.manager == "beni"
        assert y.department == "website"
        y.change_first_name("BOB")
        assert y.first_name == "BOB"
        y.change_last_name("Zamiliy")
        assert y.last_name == "Zamiliy"
        y.change_position("sell")
        assert y.position == "sell"
        y.change_manager("yaron")
        assert y.manager == "yaron"
        y.change_department("store")
        assert y.department == "store"

        print("[TEST] employee done")








