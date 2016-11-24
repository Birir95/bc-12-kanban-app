import sqlite3 as sq
import datetime as dt
import time as timer
from tabulate import tabulate
from termcolor import cprint

class ToDo(object):

    def __init__(self):
        
        self.dt = dt
        self.time = timer
        self.__db_name = 'todo.db'

        self._db = sq.connect(self.__db_name)
        self._cursor = self._db.cursor()

        try:
            self._db.execute('''create table todo 
                             (task_id INTEGER PRIMARY KEY,
                             task_name TEXT NOT NULL,
                             task_desc TEXT NOT NULL,
                             task_status TEXT ,
                             task_start DATETIME,
                             time_stop DATETIME,
                             task_taken DATETIME)''')

            
        except sq.OperationalError:
            pass

            """This app organizes to_do tasks into three sections
        (1) to do
        (2)doing
        (3)done

        """
    def to_do(self, name, desc):
       
        self._db.execute('INSERT INTO todo(task_name, task_desc, task_status) VALUES (?,?,?)',(name,
                                                             desc, 'todo'))
        self._db.commit()
        cprint("Added New Todo", 'green', 'on_grey')
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
            print(upd)
            self._db.execute(upd)
            self._db.commit()
            print("Added New Doing")


    def done(self,task_id,task_stop):
        """The function stores all tasks whose progress is complete.
        :param task_id:
        :param task_start:
        :return:
        """
        if task_stop:
            stop_time = dt.datetime.fromtimestamp(timer.time()).strftime('%Y-%m-%d %H:%M:%S')
            upgrade='UPDATE todo SET task_status = "done",time_stop ="{}" WHERE task_id = {}'.format(stop_time,task_id)
            print(upgrade)
            self._db.execute(upgrade)
            self._db.commit()

    def time_taken(self,time_taken):
    	status= self._cursor.execute("SELECT* FROM todo WHERE task_status = 'done'")
    	done_all=self._cursor.fetchall()
    	for row in done_all:
			stop = (row[5])
			start = (row[4])
			stop_obj = dt.datetime.strptime(stop, '%Y-%m-%d %H:%M:%S')
			start_obj = dt.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
			duration = stop_obj - start_obj
			print duration
			timelapse = 'UPDATE todo SET task_taken ="{}" WHERE task_id = {}'.format(str(duration), row[0] )
			print timelapse
			self._db.execute(timelapse)
			self._db.commit()
    	


    def list_to_do(self):
        """The function Lists all tasks that are in the doing section .
        :param self:
        :return:
        """
        self._cursor.execute("SELECT * FROM todo WHERE task_status='todo'")
        all_todo=self._cursor.fetchall()
        print all_todo
        self._db.commit()

    def list_doing(self):
        """The function Lists all tasks that are in the doing section .
        :param self:
        :return:
        """
        self._cursor.execute("SELECT * FROM todo WHERE task_status='doing'")
        all_doing=self._cursor.fetchall()
        print all_doing
        self._db.commit()

    def list_done(self):
        """The function Lists all tasks that are in the doing section .
        :param self:
        :return:
        """
        self._cursor.execute("SELECT * FROM todo WHERE task_status='done'")
        all_done=self._cursor.fetchall()
        print all_done 
        self._db.commit()

    def list_all(self):
            self._cursor.execute("SELECT * FROM todo ")
            all_rows = self._cursor.fetchall()
            headers = ["Id", "Name", "Description", "Status"]
            table = []
            for row in all_rows:
                rec = [row[0], row[1], row[2], row[3]]
                table.append(rec)

            print(tabulate(table, headers, tablefmt="fancy_grid"))
                


db = ToDo()
#db.to_do( 'Appointment 3', 'Call samy at 5 pm') 
#db.doing(2,True)
db.time_taken("jdhjw")        




