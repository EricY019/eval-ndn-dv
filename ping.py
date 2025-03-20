from minindn.apps.application import Application

class PingServer(Application):
    prefix: str

    def __init__(self, node):
        Application.__init__(self, node)
        self.logFile = 'pingserver.log'
        self.prefix = f'/minindn/{node.name}/32=DV'

    def start(self):
        # Application.start(self, ['ndnpingserver', self.prefix], logfile=self.logFile)
        Application.start(self, ['ndnd', 'pingserver', '--expose', self.prefix], logfile=self.logFile)

class Ping(Application):
    prefix: str

    def __init__(self, node, pfx, logname):
        Application.__init__(self, node)
        self.logFile = f'ping-{logname}.log'
        self.prefix = pfx

    # hardcode nodejs path
    def start(self):
        Application.start(self, ['node', '/mini-ndn/eval-ndn-dv/dist/ping.js', self.prefix], logfile=self.logFile)
