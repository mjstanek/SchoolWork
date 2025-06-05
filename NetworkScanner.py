# step 0- arping - built-in tool

# import scapy.all as scapy
#
# def scan(ip):
#     scapy.arping(ip)
#
# scan('192.168.68.128/25')

# step 1 - create an arp_dataframe

# import scapy.all as scapy
#
# def scan(ip):
#     arprequestframe = scapy.ARP(pdst=ip)
#     print(arprequestframe) <-- shows the summary of the request
#     print(arprequestframe.show()) <-- shows the detailed request
#     print(scapy.ls(scapy.ARP)) <-- displays all potential fields so that we can figure out how to manipulate the data
#
# scan('192.168.68.128/25')

# step 2 - create an ethernet broadcast dataframe

# import scapy.all as scapy
#
# def scan(ip):
#     arprequestframe = scapy.ARP(pdst=ip)
#     etherdataframe = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
#     # print(scapy.ls(scapy.Ether))
#     print(etherdataframe)
#     print(etherdataframe.show())
#
# scan('192.168.68.128/25')

# step 3 - stacking - create an ARP packet
# STACK packet by sending the data frames in sequence

# import scapy.all as scapy
#
# def scan(ip):
#     arprequestframe = scapy.ARP(pdst=ip)
#     etherdataframe = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
#     arppacket = etherdataframe/arprequestframe
#     print(arppacket.show())
#
# scan('192.168.68.0/24')

#step 4 - sending packet and recieving a response

# import scapy.all as scapy
#
# def scan(ip):
#     arprequestframe = scapy.ARP(pdst=ip)
#     etherdataframe = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
#     arppacket = etherdataframe/arprequestframe
#     #answeredreqs, ignoredreqs = scapy.srp(arppacket, timeout = 1)
#     response = scapy.srp(arppacket, timeout = 1)
#     answeredreqs = response[0]
#     ignoredreqs = response[1]
#     # print(type(output))
#     # print(answeredreqs)
#     # print('\n')
#     # print(ignoredreqs)
#     for device in answeredreqs:
#         print(device,'\n')
#
# scan('192.168.68.0/24')

#step 5 - output parsing - Save IP and MAC only

# import scapy.all as scapy
#
# def scan(ip):
#     arprequestframe = scapy.ARP(pdst=ip)
#     etherdataframe = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
#     arppacket = etherdataframe/arprequestframe
#     response = scapy.srp(arppacket, timeout = 1)
#     answeredreqs = response[0]
#     ignoredreqs = response[1]
#
#     for device in answeredreqs:
#         print('The device at IP Address', device[1].psrc, 'has a MAC Address of',device[1].hwsrc)
#         # print(device[1].hwsrc)#Victim MAC Address
#
# scan('192.168.68.0/24')

#step 6 - Separate the functions

# import scapy.all as scapy
#
# def scan(ip):
#     arprequestframe = scapy.ARP(pdst=ip)
#     etherdataframe = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
#     arppacket = etherdataframe/arprequestframe
#     response = scapy.srp(arppacket, timeout = 1)
#     answeredreqs = response[0]
#     ignoredreqs = response[1]
#     return answeredreqs
#
#
# def report(newip):
#     devicelist = scan(newip)
#     print('IP Address' + '\t|' + 'MAC Address')
#     for device in devicelist:
#         print( device[1].psrc + '\t|' + device[1].hwsrc)
#
# #scan('192.168.68.0/24') #no need to call this function because the report function calls the scan function
# report('192.168.68.0/24')

#step 7 - increase reusability of the scan function

# import scapy.all as scapy
#
# def scan(ip):
#     arprequestframe = scapy.ARP(pdst=ip)
#     etherdataframe = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
#     arppacket = etherdataframe/arprequestframe
#     response = scapy.srp(arppacket, timeout = 1)
#     answeredreqs = response[0]
#     ignoredreqs = response[1]
#     # return answeredreqs #goal is not to return raw data
#     listofdevices = []
#     for device in answeredreqs:
#         deviceprofile = {'IP':device[1].psrc, 'MAC':device[1].hwsrc}
#         # print(deviceprofile)
#         listofdevices.append(deviceprofile)
#
#     return listofdevices
#
# def report(newip):
#     devicelist = scan(newip)
#     print('IP Address' + '\t|' + 'MAC Address')
#     for device in devicelist:
#         print( device['IP'] + '\t|' + device['MAC'])
#
# report('192.168.68.0/24')
# # scan('192.168.68.0/24')

#step 8 - create a table

# import scapy.all as scapy
#
# def scan(ip):
#     arprequestframe = scapy.ARP(pdst=ip)
#     etherdataframe = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
#     arppacket = etherdataframe/arprequestframe
#     response = scapy.srp(arppacket, timeout = 1)
#     answeredreqs = response[0]
#     ignoredreqs = response[1]
#     listofdevices = []
#     for device in answeredreqs:
#         deviceprofile = {'IP':device[1].psrc, 'MAC':device[1].hwsrc}
#         listofdevices.append(deviceprofile)
#
#     return listofdevices
#
# def report(newip):
#     devicelist = scan(newip)
#     print('IP Address' + '\t|' + 'MAC Address')
#     print('----------------+-----------------')
#     for device in devicelist:
#         print(f"{device['IP']}\t|{device['MAC']}")
#
# report('192.168.68.0/24')

#step 9 - convert script to a class

import scapy.all as scapy

class Network_scanner:
    def __init__(self,iprange):
        self.iprange = iprange

    def scan(self, ip):
        arprequestframe = scapy.ARP(pdst=ip)
        etherdataframe = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
        arppacket = etherdataframe/arprequestframe
        response = scapy.srp(arppacket, timeout = 1)
        answeredreqs = response[0]
        ignoredreqs = response[1]
        listofdevices = []
        for device in answeredreqs:
            deviceprofile = {'IP':device[1].psrc, 'MAC':device[1].hwsrc}
            listofdevices.append(deviceprofile)

        return listofdevices

    def report(self):
        devicelist = self.scan(self.iprange)
        print('IP Address' + '\t|' + 'MAC Address')
        print('----------------+-----------------')
        for device in devicelist:
            print(f"{device['IP']}\t|{device['MAC']}")

if __name__ == '__main__':

    Network_scanner('192.168.68.128/27').report()