from todotxt import TodoFile

from .task import Task



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
        self.project.add_entry(task.entry)
        task.project = self

    def _entries(self):
        return sorted(self.project.todo_entries, key=lambda x: x.priority or 'ZZ')

    def tasks(self):
        return map(Task, self._entries())

    def first_task(self, skip_completed=True):
        tasks = self.tasks()
        for task in tasks:
            if skip_completed and task.entry.completed:
                continue
            return task

        return None
