from todotxt import TodoFile

import project, task

class Project:
    def __init__(self, name, create=False):
        self.name = name
        self.loaded = False
        self.create = create
        self.refresh()

    def refresh(self):
        try:
            self.project = TodoFile(self.name)
            self.project.load()
            self.loaded = True
            self.create = False
        except FileNotFoundError:
            if not self.create:
                raise

    def commit(self):
        self.project.save()

    def add(self, task):
        self.project.add_entry(task)
        task.project = self

    def entries(self):
        return sorted(f.todo_entries, key=lambda x: x.priority or 'ZZ')

    def first_entry(self, completed=True):
        entries = self.entries()
        for entry in entries:
            if completed and not entry.completed:
                continue
            return entry

        return None
