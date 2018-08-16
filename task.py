from todotxt import TodoEntry

class Task:
    def __init__(self, name, project=None):
        if isinstance(name, TodoEntry):
            self.entry = name
        else:
            self.entry = TodoEntry(name)
        self.project = project

    def complete(self, complete=True):
        self.entry.completed = complete
