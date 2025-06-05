import subprocess,random,netfilterqueue
import scapy.all as scapy
def xss_attack(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    print(scapy_packet)
def intercept_packet(packet):
    try:
        xss_attack(packet)
        packet.accept()
    except Exception as error_message:
        print(error_message)
        packet.accept()
def interception_start(queue_table_number):
    queue_table = netfilterqueue.NetfilterQueue()
    queue_table.bind(queue_table_number,intercept_packet)
    queue_table.run()
def create_ip_table(queue_table_number):
    print(f"[+]Interception attack start, your queue table number is {queue_table_number}\n")
    subprocess.run(['iptables', '-I', 'INPUT', '-j', 'NFQUEUE', '--queue-num', str(queue_table_number)])
    subprocess.run(['iptables', '-I', 'OUTPUT', '-j', 'NFQUEUE', '--queue-num', str(queue_table_number)])
try:
    queue_table_number = random.randint(100, 10000)
    create_ip_table(queue_table_number)
    interception_start(queue_table_number)
finally:
    print("[-]Flush all iptables \n\n ")
    subprocess.run(['iptables', '--flush'])
