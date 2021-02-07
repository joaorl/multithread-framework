from system.service import Service

class DDService(Service):
    def OnCreate(self):
        print("init ", self.name)

        return 5 # delay to start

    def OnRun(self):
        print("run ", self.name)

        return 20 # seconds

    def OnAsyncEvent(self, source, data):

        return 0