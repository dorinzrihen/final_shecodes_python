import pandas as pd
import time


class Files:
    def __init__(self):
        super.__init__()

    ##employee file
    @classmethod
    def add_to_file(self, id, f_name, l_name, position, manager, manager_id, department):
        df = pd.read_excel("employees.xlsx")
        if df.loc[df.id == id, 'id'].empty:
            df2 = pd.DataFrame([[id, f_name, l_name, position, manager, manager_id, department]], columns=df.columns)
            df = df.append(df2, ignore_index=True)
            df.to_excel("employees.xlsx", index=False)
        else:
            print(f'[ERROR] {id} already employee')

    @classmethod
    def change_info(self, id, info, title):
        df = pd.read_excel("employees.xlsx")
        df.loc[df.id == id, title] = info
        df.to_excel("employees.xlsx", index=False)

    @classmethod
    def delete_employee(id):
        df = pd.read_excel("employees.xlsx")
        if not df.loc[df.id == id, 'id'].empty:
            df = df[df.id != id]
            df.to_excel("employees.xlsx", index=False)
        else:
            print(f"there is no {id} employee, please check your data")

    # entry and exit file data
    # we need to get the data from the employee.xlsx and put with our new information
    @classmethod
    def entry(self, id):
        entry_data = time.localtime()
        employee_data = Files.get_employee_data(id)
        df = pd.read_excel("reports.xlsx")
        if df.loc[(df["id"] == id) & (df["day"] == entry_data[2])].empty:
            df2 = pd.DataFrame([[entry_data[0], entry_data[1], entry_data[2], entry_data[3], entry_data[4],
                                 employee_data[0], employee_data[1],
                                 employee_data[2], employee_data[3], employee_data[4], employee_data[5],
                                 employee_data[6]]],
                               columns=['year', 'month', 'day', 'entry_hour', 'entry_minute', 'id', 'first_name',
                                        'last_name', 'position', 'manager', 'manager_id', 'department'])
            df = df.append(df2, ignore_index=True)
            print(df2)
            df.to_excel("reports.xlsx", index=False)
        else:
            print("already logged in")

        # entry_data = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

    # calculate exit and entry to know how much time the employee work
    @classmethod
    def exit(self,id):
        exit_data = time.localtime()
        df = pd.read_excel("reports.xlsx")
        if not df.loc[(df["id"] == id) & (df["day"] == exit_data[2])].empty:
            df.loc[(df["id"] == id) & (df["day"] == exit_data[2]), 'exit_hour'] = exit_data[3]
            df.loc[(df["id"] == id) & (df["day"] == exit_data[2]), 'exit_minute'] = exit_data[4]
            df.loc[(df["id"] == id) & (df["day"] == exit_data[2]), 'sum'] = self.cal_work_time(df.loc[(df["id"] == id) & (df["day"] == exit_data[2]), 'entry_hour'].values, df.loc[(df["id"] == id) & (df["day"] == exit_data[2]), 'entry_minute'].values, exit_data[3], exit_data[4])
            df.to_excel("reports.xlsx", index=False)
        else:
            print("[PROBLEM] this employee didnt sigh in")

    def dayoff(id, dd, mm, yy):
        pass

    def sick_day(id, dd, mm, yy):
        pass

    def select_report_by(self):
        pass

    def work_time_cal(self):
        pass

    def get_employee_data(id):
        df = pd.read_excel("employees.xlsx")
        if not df.loc[df.id == id, 'id'].empty:
            return df.loc[df.id == id].values[0]

    @classmethod
    def cal_work_time(self,entry_hour, entry_min, exit_hour, exit_min):
        print(self,entry_hour, entry_min, exit_hour, exit_min)
        if entry_min>exit_min:
            hour_sum = ((exit_hour - entry_hour-1) * 60) + (60 - entry_min) + exit_min
        else:
            hour_sum = exit_min-entry_min + ((exit_hour - entry_hour) * 60)
        return hour_sum/60



"""when i try to change a value we cant create it """
#Files.add_to_file(6060,0,0,0,0,0,0)
Files.exit(6060)