import sqlite3 as sq
import datetime as dt
import time as timer
from tabulate import tabulate
from termcolor import cprint
from timeit import default_timer as tm


class ToDo(object):

    def __init__(self):
        
        self.dt = dt
        self.time = timer
        self.db_name = 'todo.db'

        self.db = sq.connect(self.db_name)
        self.cursor = self.db.cursor()

        try:
            self.db.execute('''create table todo 
                             (task_id INTEGER PRIMARY KEY,
                             task_name TEXT NOT NULL,
                             task_desc TEXT NOT NULL,
                             task_status TEXT ,
                             task_start DATETIME,
                             time_stop DATETIME,
                             time_taken DATETIME)''')

            
        except sq.OperationalError:
            pass

            """This app organizes to_do tasks into three sections
        (1) to do
        (2)doing
        (3)done
        """
    def to_do(self, name, desc):
       
        self.db.execute('INSERT INTO todo(task_name, task_desc, task_status) VALUES (?,?,?)',(name,
                                                             desc, 'todo'))
        self.db.commit()
        cprint("Added New Todo", 'yellow', 'on_grey')
        cprint("Name: {}\nDescription: {}".format(name, desc), 'cyan', 'on_grey')

    def doing(self, task_id, task_start):
        """The function stores all tasks currently on progress.
        :param task_id:
        :param task_start:
        :return:
        """
        if task_start:
            start_time = dt.datetime.fromtimestamp(timer.time()).strftime('%Y-%m-%d %H:%M:%S')
            upd='UPDATE todo SET task_status = "doing",task_start ="{}" WHERE task_id = {}'.format(start_time,task_id)
            self.db.execute(upd)
            self.db.commit()
            cprint("Added New Doing",'red','on_grey')


    def done(self,task_id,task_stop):
        """The function stores all tasks whose progress is complete.
        :param task_id:
        :param task_start:
        :return:
        """
        if task_stop:
            stop_time = dt.datetime.fromtimestamp(timer.time()).strftime('%Y-%m-%d %H:%M:%S')
            upgrade='UPDATE todo SET task_status = "done",time_stop ="{}" WHERE task_id = {}'.format(stop_time,task_id)
            self.db.execute(upgrade)
            self.db.commit()
            cprint("Task has been completed", 'green' ,'on_grey')

    def time_taken(self,time_taken):
    	status= self.cursor.execute("SELECT* FROM todo WHERE task_status = 'done'")
    	done_all=self.cursor.fetchall()
    	for row in done_all:
			stop = (row[5])
			start = (row[4])
			stop_obj = dt.datetime.strptime(stop, '%Y-%m-%d %H:%M:%S')
			start_obj = dt.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
			duration = stop_obj - start_obj
			timelapse = 'UPDATE todo SET time_taken ="{}" WHERE task_id = {}'.format(str(duration), row[0] )

			self.db.execute(timelapse)
			self.db.commit()
    	

    def list_to_do(self):
        """The function Lists all tasks that are in the doing section .
        :param self:
        :return:
        """
        self.cursor.execute("SELECT * FROM todo WHERE task_status='todo'")
        all_todo=self.cursor.fetchall()
        headers = ["Id", "Name", "Description", "Status"]
        tablet = []
        for row in all_todo:
            rows = [row[0], row[1], row[2], row[3]]
            tablet.append(rows)
            print(tabulate(tablet, headers, tablefmt="fancy_grid"))
        
        self.db.commit()

    def list_doing(self):
        """The function Lists all tasks that are in the doing section .
        :param self:
        :return:
        """
        self.cursor.execute("SELECT * FROM todo WHERE task_status='doing'")
        all_doing=self.cursor.fetchall()
        headers = ["Id", "Name", "Description", "Status"]
        tablee = []
        for row in all_doing:
            columns = [row[0], row[1], row[2], row[3]]
            tablee.append(columns)
            print(tabulate(tablee, headers, tablefmt="fancy_grid"))

        
        self.db.commit()

    def list_done(self):
        """The function Lists all tasks that are in the doing section .
        :param self:
        :return:
        """
        self.cursor.execute("SELECT * FROM todo WHERE task_status='done'")
        all_done=self.cursor.fetchall()
        headers = ["Id", "Name", "Description", "Status"]
        tab = []
        for row in all_done:
            rec = [row[0], row[1], row[2], row[3]]
            tab.append(rec)
            print(tabulate(tab, headers, tablefmt="fancy_grid"))
  
        self.db.commit()

    def list_all(self):
            self.cursor.execute("SELECT * FROM todo ")
            all_rows = self.cursor.fetchall()
            headers = ["Id", "Name", "Description", "Status", "Time"]
            table = []
            for row in all_rows:
                id = row[0]
                task_name = row[1]
                task_desc = row[2]
                task_status = row[3]
                time_taken = row[6]

                if task_status == 'do':
                    time_taken = "Not Started"
                elif task_status == 'doing':
                    time_taken = "Started"
                elif task_status == 'done':
                    time_taken = row[6]
                    rec = [id, task_name, task_desc, task_status, time_taken]
                    table.append(rec)

            print(tabulate(table, headers, tablefmt="fancy_grid"))


          


