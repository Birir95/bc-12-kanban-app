class ToDo(object):
    def __init__(self):
        import sqlite3 as sq
        self._todo_data = {'to_do': {}, 'doing': {}, 'done': {}}
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
                             task_stop DATETIME)''')

            
        except sq.OperationalError:
            pass

            """This app organizes to_do tasks into three sections
        (1) to do
        (2)doing
        (3)done

        """
    def to_do(self, name, desc):
       
        self._db.execute('INSERT INTO todo(task_name, task_desc) VALUES (?,?)',(name,
                                                             desc))
        self._db.commit()

	def to_do(self,task_name,task_desc):
		pass

	def doing(self, taskid,task_start):
		pass

	def done(self,task_id,task_stop):
		pass

	def list_todo(self):
		pass

	def list_doing(self):
		pass

	def list_done(self):
		pass

	def list_all(self):
		pass

	def main():
		pass