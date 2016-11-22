import sq
class ToDo(object):
	"""KanBan is a console application that is used to manage to-do 
	tasks using the KanBan way of organizing todo into 
	3 sections: todo, doing, done.""" 
	def __init__(self):
		import sqlite3 as sq
    self._todo_data = {'to_do': {}, 'doing': {}, 'done': {}}
    self.__db_name = 'KanBan.db'

    self._db = sq.connect(self.__db_name)
    self._cursor = self._db.cursor()

    try:
        self._db.execute('''create table TODO
                             (task_id INTEGER PRIMARY KEY,
                             task_name TEXT NOT NULL,
                             task_desc TEXT NOT NULL)''')

        self._db.execute('''create table DOING
                            (task_id INTEGER,
                             task_name TEXT NOT NULL,
                             task_desc TEXT NOT NULL)''')

        self._db.execute('''create table DONE
                            (task_id INTEGER,
                             task_name TEXT NOT NULL,
                             task_desc TEXT NOT NULL)''')
    except sq.OperationalError:
        pass


	pass

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