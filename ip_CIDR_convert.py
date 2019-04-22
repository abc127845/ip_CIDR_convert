import ipaddr
import netaddr 

class Network():
    def __init__(self):
        pass
    def IPRange_To_CIDR(self,x,y):
        cidrs = netaddr.iprange_to_cidrs(x, y)
        print("ip's CIDR ",x,"to",y,"\n")
        for k, v in enumerate(cidrs):
            iplist = v
            print(iplist)

    
    def CIDR_to_IPRange(self,ip):
        #ipv4 = ipaddr.IPv4Address(ip)
        ipv4 = ipaddr.IPv4Network(ip)
        print(ipv4,"'s CIDR to IPRange\n")
        print("Is private IP: ",ipv4.is_private) 
        print("Total Host: ",ipv4.numhosts)
        print("(broadcast)Last IP: ",ipv4.broadcast)   ##廣播位址 Last IP
        print("Widlcard Bits: ",ipv4.hostmask)    ##Widlcard Bits
        print("Netmask: ",ipv4.netmask)     ##Netmask
        print("Is loopback IP?: ",ipv4.is_loopback)    ##是否是loopback位址
        print("ip range is : ",str(ipv4[0]),"to",ipv4.broadcast)

def main():   
    net = Network()
    net.IPRange_To_CIDR('140.192.30.78','140.192.30.90')
    print('--------------------------------------------------------------------')
    net.CIDR_to_IPRange('140.192.30.76/30')

if __name__ == '__main__':
    main()
