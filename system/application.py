
from system.singleton_meta import *

class Application(metaclass=SingletonMeta):
    def __init__(self, name="TBD"):
        self.__task = {}
        self.__name = name

    def Add(self, name, task):
        task.__init__(name, self)
        self.__task[name] = task

    def Start(self):
        for _, task in self.__task.items():
            task.Start()

    def Stop(self):
        for _, task in self.__task.items():
            task.Stop()
            task = None

    def GetName(self):
        return self.__name

    def GetTask(self, name):
        return self.__task[name]