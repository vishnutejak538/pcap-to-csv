from scapy.all import *
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP , TCP, UDP
import pandas as pd
class Pcaper:
    def __init__(self):
        self.ip_list = self.tcp_list = self.eth_list = []
        self.ip_list = [field.name for field in IP().fields_desc]
        self.tcp_list = [field.name for field in TCP().fields_desc]
        self.eth_list = [field.name for field in Ether().fields_desc]
        self.udp_list = [field.name for field in UDP().fields_desc]
        try:
            self.ip_list.remove("options")
            self.tcp_list.remove("options")
            self.eth_list.remove("options")
            self.udp_list.remove["options"]
        except:
            pass
        self.tot_col = self.eth_list + self.ip_list + ["time"] + self.tcp_list

    def run(self,filepath:str,csvname:str):
        self.pack = rdpcap(filepath)
        df = pd.DataFrame(columns = self.tot_col)
        for pa in self.pack:
            try:
                if pa[ARP]:
                    continue
            except:
                pass
            field_val = []
            for field in self.eth_list:
                field_val.append(pa[Ether].fields[field])
            for field in self.ip_list:
                field_val.append(pa[IP].fields[field])
            field_val.append(pa.time)
            t = type(pa[IP].payload)
            for field in self.tcp_list:
                try:
                    field_val.append(pa[t].fields[field])
                except:
                    field_val.append(None)
            me = pd.DataFrame([field_val],columns=self.tot_col)
            df = pd.concat([df,me],axis=0)
        df.to_csv(path_or_buf=csvname+".csv",index=False)


