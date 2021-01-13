import pandas as pd
from scapy.all import *
from scapy.layers.inet import IP, TCP

columns = ['Timestamp'
          ,'SourceIP'
          ,'DestinationIP'
          ,'Source Port'
          ,'DestinationPort']

rows = []
pckNum = 0

with PcapReader('/home/Disciplinas/OficinaMakerPrepAnaliseDados/Wednesday-WorkingHours.pcap') as packets:
    for packet in packets:
        # print (packet.show())
        # print (packet.time)
        pckNum = pckNum + 1

        if (pckNum % 1000 == 0):
            print(pckNum, datetime.fromtimestamp(packet.time).strftime('%Y-%m-%d %H:%M:%S.%f'))

        if(TCP in packet):
            newRow = [packet.time
                    , packet[IP].src
                    , packet[IP].dst
                    , packet[TCP].sport
                    , packet[TCP].dport]
            rows.append(newRow)

df = pd.DataFrame(rows, columns = columns)
df.to_csv('/home2/ead2020/soares.v/Documents/out_pcap.csv',index=False)
