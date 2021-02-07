from system.service import Service

class AAService(Service):
    def OnCreate(self):
        print("init ", self.name)

        return 1 # delay to start

    def OnRun(self):
        print("run ", self.name)

        self.Send("bb", "ole")

        return 1 # seconds

    def OnAsyncEvent(self, source, data):
        return 0