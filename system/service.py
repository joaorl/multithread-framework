import threading
import logging

import queue
import abc

from time import *

format = "[%(asctime)s]%(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%Y-%m-%d %H:%M:%S")

class Service(metaclass=abc.ABCMeta):
    def __init__(self, name="", app_context=None):
        self._name = name
        self.__app_context = app_context
        self.__stopThread = False
        self.__queue = queue.Queue()

    @property
    def name(self):
        return self._name

    def _run(self):
        ret = 0

        logging.info("[%s][ON CREATE]" % (self.name))
        ret = self.OnCreate()

        ref = time()
        while (self.__stopThread == False):
            if not self.__queue.empty():
                data = self.__queue.get()
                logging.info("[%s][ON EVENT] %s" % (self.name, data))
                self.OnAsyncEvent(data['from'], data['data'])

            while time() >= ref + ret:
                logging.info("[%s][ ON RUN ]" % (self.name))

                ret = self.OnRun()
                ref = time()

            sleep(0.1)
        return ret

    def Stop(self):
        logging.info("[%s][STOP THREAD]" % (self._name))

        self.__stopThread = True

        while self._thread.is_alive():
            self._thread.join()

        return 0

    def Close(self):
        self.Stop()

        return 0

    def Start(self):
        logging.info("[%s][START THREAD]" % (self.name))
        self._thread = threading.Thread(target=self._run)
        self._thread.start()

    def Send(self, to, data):
        if to is self.name:
            return None

        self.__app_context.GetTask(to).__queue.put({
            'from': self.name,
            'data': data
        })

    @abc.abstractmethod
    def OnCreate(self):
        return 0

    @abc.abstractmethod
    def OnAsyncEvent(self, source, data):
        return 0

    @abc.abstractmethod
    def OnRun(self):
        return 0

