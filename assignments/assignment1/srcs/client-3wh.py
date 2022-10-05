#!/usr/bin/env python

from scapy.all import *
import threading

SEND_PACKET_SIZE = 1000  # should be less than max packet size of 1500 bytes

# A client class for implementing TCP's three-way-handshake connection establishment and closing protocol,
# along with data transmission.


class Client3WH:

    def __init__(self, dip, dport):
        """Initializing variables"""
        self.dip = dip
        self.dport = dport
        # selecting a source port at random
        self.sport = random.randrange(0, 2**16)

        self.next_seq = 0                       # TCP's next sequence number
        self.next_ack = 0                       # TCP's next acknowledgement number

        self.ip = IP(dst=self.dip)              # IP header

        self.connected = False
        self.timeout = 3

    def _start_sniffer(self):
        t = threading.Thread(target=self._sniffer)
        t.start()

    def _filter(self, pkt):
        if (IP in pkt) and (TCP in pkt):  # capture only IP and TCP packets
            return True
        return False

    def _sniffer(self):
        while self.connected:
            sniff(prn=lambda x: self._handle_packet(
                x), lfilter=lambda x: self._filter(x), count=1, timeout=self.timeout)

    def _handle_packet(self, pkt):
        """TODO(1): Handle incoming packets from the server and acknowledge them accordingly. Here are some pointers on
           what you need to do:
           1. If the incoming packet has data (or payload), send an acknowledgement (TCP) packet with correct 
              `sequence` and `acknowledgement` numbers.
           2. If the incoming packet is a FIN (or FINACK) packet, send an appropriate acknowledgement or FINACK packet
              to the server with correct `sequence` and `acknowledgement` numbers.
        """

        ### BEGIN: ADD YOUR CODE HERE ... ###

        if Raw in pkt: # data
            self.next_ack += len(pkt[Raw])
            ACK = TCP(sport=self.sport, dport=self.dport, flags="A", seq=self.next_seq, ack=self.next_ack)
            send(self.ip/ACK)

        elif FIN in pkt: # FIN
            FIN = TCP(sport=self.sport, dport=self.dport, flags="FA", seq=self.next_seq, ack=self.next_ack)
            FINACK = sr1(self.ip/FIN)
            self.next_seq += 1
            self.next_ack = FINACK[TCP].seq + 1
            ACK = TCP(sport=self.sport, dport=self.dport, flags="A", seq=self.next_seq, ack=self.next_ack)
            send(self.ip/ACK)
        
        elif FINACK in pkt: # FINACK
            ACK = TCP(sport=self.sport, dport=self.dport, flags="A", seq=self.next_seq, ack=self.next_ack)
            send(self.ip/ACK)

        ### END: ADD YOUR CODE HERE ... #####

    def connect(self):
        """TODO(2): Implement TCP's three-way-handshake protocol for establishing a connection. Here are some
           pointers on what you need to do:
           1. Handle SYN -> SYNACK -> ACK packets.
           2. Make sure to update the `sequence` and `acknowledgement` numbers correctly, along with the 
              TCP `flags`.
        """

        ### BEGIN: ADD YOUR CODE HERE ... ###
        
        SYN = TCP(sport=self.sport, dport=self.dport, flags="S", seq=self.next_seq)
        SYNACK = sr1(self.ip/SYN)
        self.next_seq += 1
        self.next_ack = SYNACK[TCP].seq + 1
        ACK = TCP(sport=self.sport, dport=self.dport, flags="A", seq=self.next_seq, ack=self.next_ack)
        send(self.ip/ACK)
        
        ### END: ADD YOUR CODE HERE ... #####

        self.connected = True
        self._start_sniffer()
        print('Connection Established')

    def close(self):
        """TODO(3): Implement TCP's three-way-handshake protocol for closing a connection. Here are some
           pointers on what you need to do:
           1. Handle FIN -> FINACK -> ACK packets.
           2. Make sure to update the `sequence` and `acknowledgement` numbers correctly, along with the 
              TCP `flags`.
        """

        ### BEGIN: ADD YOUR CODE HERE ... ###
        
        FIN = TCP(sport=self.sport, dport=self.dport, flags="FA", seq=self.next_seq, ack=self.next_ack)
        FINACK = sr1(self.ip/FIN)
        self.next_seq += 1
        self.next_ack = FINACK[TCP].seq + 1
        ACK = TCP(sport=self.sport, dport=self.dport, flags="A", seq=self.next_seq, ack=self.next_ack)
        send(self.ip/ACK)

        ### END: ADD YOUR CODE HERE ... #####

        self.connected = False
        print('Connection Closed')

    def send(self, payload):
        """TODO(4): Create and send TCP's data packets for sharing the given message (or file):
           1. Make sure to update the `sequence` and `acknowledgement` numbers correctly, along with the 
              TCP `flags`.
        """

        ### BEGIN: ADD YOUR CODE HERE ... ###

        pkt = self.ip / TCP(sport=self.sport, dport=self.dport, flags="PA", seq=self.next_seq, ack=self.next_ack) / payload
        self.next_seq += len(pkt[Raw])
        ACK = sr1(pkt)

        ### END: ADD YOUR CODE HERE ... #####


def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit(
            "Usage: ./client-3wh.py [Server IP] [Server Port] < [message]")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    client = Client3WH(server_ip, server_port)
    client.connect()

    message = sys.stdin.read(SEND_PACKET_SIZE)
    while message:
        client.send(message)
        message = sys.stdin.read(SEND_PACKET_SIZE)

    client.close()


if __name__ == "__main__":
    main()

