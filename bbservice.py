from system.service import Service

class BBService(Service):
    def OnCreate(self):
        print("init ", self.name)

        return 1 # delay to start

    def OnRun(self):
        print("run ", self.name)

        return 5 # seconds

    def OnAsyncEvent(self, source, data):
        print("OnEvent= %s %s" % (source, data))

        return 0