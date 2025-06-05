# #My attempt to create an ARP Spoofing detector
#
# import scapy.all as scapy
#
# statusmessage = ''
#
# class ARPSpoofDetector:
#
#     def __init__(self,interface):
#         self.interface = interface
#
#     def getmac(self,ip):
#         arprequestframe = scapy.ARP(pdst=ip)
#         etherdataframe = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
#         arppacket = etherdataframe / arprequestframe
#         response = scapy.srp(arppacket, timeout=3, verbose=False)
#         answeredreqs = response[0]
#         targetmac=answeredreqs[0][1].hwsrc
#         return targetmac
#
#     def sniff(self):
#         scapy.sniff(iface=self.interface, store=False, prn=self.filtersniffoutput)
#
#     def filtersniffoutput(self,packet):
#         if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
#             routermac = self.getmac('192.168.68.2')
#             responsemac = packet[scapy.ARP].hwsrc
#             self.maccompare(routermac,responsemac)
#
#     def maccompare(self,routermac,responsemac):
#         global statusmessage
#         if routermac == responsemac:
#             if statusmessage == 'Everything appears to be normal.':
#                 pass
#             else:
#                 statusmessage = 'Everything appears to be normal.'
#                 print(statusmessage)
#         else:
#             if statusmessage == 'There might be an ARP Spoofing attack happening.':
#                 pass
#             else:
#                 statusmessage = 'There might be an ARP Spoofing attack happening.'
#                 print(statusmessage)
#
# if __name__ == '__main__':
#     ARPSpoofDetector('eth0').sniff()

#ARP Spoofing Detector - class

#There will be a lot of ARP-related traffic on the network
#if there is an ARP Spoofing atttack, we will se a lot of ARP Response packets

#We need to get the correct router info - IP and MAC
# ip -route and an ARP request

#Comparisons
#if the true MAC for the router is the same as the sniffed router's MAC --> no attack
#if the true MAC for the router is not the same as the sniffed router's MAC --> attack probable

import scapy.all as scapy

class ARPSpoofDetector: