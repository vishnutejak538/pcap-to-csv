from pcap_to_csv import Pcaper
import os
filename = str(input("enter the pcap file"))
csvname = str(input("enter the name to be given for the CSV file"))
obj = Pcaper()
obj.run(filename,csvname)
