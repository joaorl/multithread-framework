from system.service import Service

class CCService(Service):
    def OnCreate(self):
        print("init ", self.name)

        return 5 # delay to start

    def OnRun(self):
        return 15 # seconds

    def OnAsyncEvent(self, source, data):
        return 0