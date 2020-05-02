from pcap_to_csv import Pcaper
import os
file = []
for files in os.listdir("F:\\Damm_imp\\pro\\DATAS\\datasets\\USTC-TFC2016\\Malware"):
    file.append(files)
obj = Pcaper()
for f in file:
    obj.run(f,f.strip(".")[0])
