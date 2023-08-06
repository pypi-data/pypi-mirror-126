from packetvisualization.models.pcap import Pcap
# from packetvisualization.backend_components.entity_operator import EntityOperator
import os, shutil
import platform

class Dataset:
    def __init__(self, name: str, parentPath: str) -> None:
        self.name = name
        self.pcaps = [] # will use children key instead
        self.mergeFilePath = None
        self.jsonFilePath = None
        self.path = os.path.join(parentPath, self.name)
        self.totalPackets = 0
        self.protocols = None
        self.create_folder()
        self.create_merge_file()
        # self.create_json_file()

    def add_pcap(self, new: Pcap) -> list:
        self.pcaps.append(new)
        self.merge_pcaps()

        return self.pcaps

    def del_pcap(self, old: Pcap): # Replace with DB Query
        self.pcaps.remove(old)
        if self.pcaps != []: # must have at least one pcap to merge
            self.merge_pcaps()
        os.remove(old.path) # delete file in dir
        old.remove()
        return self.pcaps

    def add_pcap_dir(self, location: str) -> list:  # when we receive directory w/PCAPs as user input
        for file in os.listdir(location):
            self.pcaps.append(Pcap(file, self))  # For each file, create instance of Packet
        return self.pcaps

    def create_folder(self) -> str: # create save location
        if not os.path.isdir(self.path):
            os.mkdir(self.path)
        return self.path

    def create_merge_file(self):
        filename = self.name + ".pcap"
        path = os.path.join(self.path, filename)
        self.mergeFilePath = path
        fp = open(path, 'a')
        fp.close()

    def save(self, f) -> None: # Save file
        f.write('{"name": "%s", "totalPackets": %s, "pcaps": [' % (self.name, self.totalPackets))
        for a in self.pcaps:
            a.save(f)
            if a != self.pcaps[-1]:
                f.write(',')
        f.write(']}')

    def merge_pcaps(self):
        pcapPaths = ""

        if platform.system() == 'Windows':
            for pcap in self.pcaps:
                pcapPaths += pcap.path + " "

            os.system('cd "C:\\Program Files\\Wireshark\\" & mergecap -w %s %s' % (self.mergeFilePath, pcapPaths))
            print("")
        elif platform.system() == 'Linux':
            for pcap in self.pcaps:
                pcapPaths += pcap.path + " "

            os.system('mergecap -w %s %s' % (self.mergeFilePath, pcapPaths))
            print("Linux")

    def remove(self) -> bool:
        return self.__del__()

    def __del__(self) -> bool:
        try:
            shutil.rmtree(self.path)
            for p in self.pcaps:
                p.remove()
            self.pcaps = [] # unlink all pcaps
            return True
        except:
            return False
