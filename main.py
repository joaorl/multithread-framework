import time

from system.application import Application

from aaservice import AAService
from bbservice import BBService
from ccservice import CCService
from ddservice import DDService

if __name__ == "__main__":
    try:
        app = Application("demo")

        app.Add("aa", AAService())
        app.Add("bb", BBService())
        app.Add("cc", CCService())
        app.Add("dd", DDService())

        app.Start()

        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        app.Stop()
