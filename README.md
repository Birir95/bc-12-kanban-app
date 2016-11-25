# KanBan_App

KanBan is a console application that is used to manage to-do tasks using the KanBan way of organizing todo into 3 sections: todo, doing, done. The app also tracks the time taken on a particular task and displays each task in the doing and done section with the time-taken so far on the task.

# Installation of KanBan

To get started with KanBan Console, clone this repository:

* Go To KanBan Console GitHub Repository(https://github.com/Birir95/bc-12-kanban-app.git) .
* Clone the Repository.
* Install the Requirements From the requirements.txt File.
* Run The kanban.py file.

```sh
$ git clone https://github.com/Birir95/bc-12-kanban-app.git
$ cd bc-12-kanban_console
$ pip install -r requirements.txt
```
# Let Us Get Started
KanBan console was developed using python 2.7

'''Welcome to KanBan program!'type help for a list of commands.'''
=================WELL HELLO THERE!===============

Welcome to KanBan program! (type help for a list of commands.)
KanBan App>>help

Documented commands (type help <topic>):
========================================
doing  help      list_doing  list_to_do  time_taken
done   list_all  list_done   quit        todo


### 'todo' command
To add a task in the todo section type 'help todo' to see the parameters it takes.
'''KanBan App>>help todo then type the task name press enter then enter its description
Usage: todo <task_name>
KanBan App>>todo Church
Enter description :Go to church on sunday
Added New Todo
Name: Church
Description: Go to church on sunday
KanBan App>>'''


#### 'doing' command
To add a task in the doing section type 'help doing' to see the parameters it takes.
'''KanBan App>>doing 1 True
Added New Doing'''

### 'done' command
To add a task in the done section type 'help done' to see the parameters it takes 
'''KanBan App>>done 3 True
Task has been completed'''

### 'list_to_do' command
To list_to_do type 'list_to_do' and press enter


### 'list_doing' command
To list_doing tasks type 'list_doing' and press enter


### 'list_done' command
To list_done tasks type 'list_done' and press enter

KanBan App>>list_all
To list_all tasks type 'list_all' and press enter


### To list_all tasks type 'list_all' and press enter
Here is a small snippet of how it looks when you list all the tasks

![kanban_snip](https://cloud.githubusercontent.com/assets/19901599/20615463/618e83ce-b2eb-11e6-8c7f-02e3349f125d.png)







