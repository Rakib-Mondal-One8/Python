class CPU:
    def __init__(self,core):
        self.core = core
class RAM:
    def __init__(self,size):
        self.size = size
class HDD:
    def __init__(self,capacity):
        self.capacity = capacity

class PC:
    def __init__(self,core,ram,hdd):
        self.cpu = CPU(core)
        self.ram = RAM(ram)
        self.hdd = HDD(hdd)

mac = PC(10,16,512)
