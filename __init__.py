
import sys

from os.path import dirname

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
LOGGER = getLogger(__name__)
LOGGER.debug('Mycroft-Todo '+sys.version)
LOGGER.debug('Mycroft-Todo '+str(sys.path))


from .project import Project
from .task import Task

__author__ = 'gerlachry'

class TodoSkill(MycroftSkill):
    def __init__(self):
        super().__init__(name="TodoSkill")

    def initialize(self):
        add_intent = IntentBuilder("TodoIntent")\
            .require("Add")\
            .build()
        self.register_intent(add_intent, self.handle_add)

    def _get_project(self, name):
        """lookup project by name, create if not found"""
        return Project(name, create=True)

    def handle_add(self, message):
        task = message.data.get('Task', None)
        project = message.data.get('Project', None)
        LOGGER.debug('adding task {0} to {1} project'.format(task, project))

        try:
            self.speak_dialog('add.task')
            prj = self._get_project(project)
            prj.add(Task(task))
            prj.commit()

            self.speak_dialog('add.task.complete')

        except Exception as e:
            LOGGER.exception("Error: {0}".format(e))

    def stop(self):
        pass


def create_skill():
    return TodoSkill()
