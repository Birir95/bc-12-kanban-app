import sqlite3 as sq
import datetime as dt
import time as timer

class ToDo(object):

    def __init__(self):
        
        self.dt = dt
        self.time = timer
        self.__db_name = 'todo.db'

        self._db = sq.connect(self.__db_name)
        self._cursor = self._db.cursor()

        try:
            self._db.execute('''create table if not exist todo
                             (task_id INTEGER PRIMARY KEY,
                             task_name TEXT NOT NULL,
                             task_desc TEXT NOT NULL,
                             task_status TEXT ,
                             task_start DATETIME,
                             task_stop DATETIME)''')

            
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
