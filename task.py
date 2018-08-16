from todotxt import TodoEntry

class Task:
    def __init__(self, name, project=None):
       self.entry = TodoEntry(name)
       self.project = project

    def complete(complete=True):
        self.entry.complete = complete
