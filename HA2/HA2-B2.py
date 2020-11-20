# Mix Network
# By Amanda Flote & Olivia Mattsson
# !/usr/bin/env python
from pcapfile import savefile

def main():
    testcap = open('HA2/cia.log.1339.pcap', 'rb')
    capfile = savefile.load_savefile(testcap, layers=2, verbose=True)
    with open('HA2/testquizB2.txt') as f:
        lines = f.read().splitlines()
        NazirIP = lines[0]
        MixIP = lines[1]
        NoParners = int(lines[2])
        NazirSent = False
        foundMix = False
        receivers = []
        # print the packets
        # print ('timestamp\teth src\t\t\teth dst\t\t\tIP src\t\tIP dst')
        for pkt in capfile.packets:
            timestamp = pkt.timestamp
            # all data is ASCII encoded (byte arrays). If we want to compare with strings
            # we need to decode the byte arrays into UTF8 coded strings
            eth_src = pkt.packet.src.decode('UTF8')
            eth_dst = pkt.packet.dst.decode('UTF8')
            ip_src = pkt.packet.payload.src.decode('UTF8')
            ip_dst = pkt.packet.payload.dst.decode('UTF8')
            if (NazirIP == ip_src):
                newreceivers = set()
                NazirSent = True
            if NazirSent and ip_src == MixIP:
                foundMix = True
            if foundMix and ip_src != MixIP:
                receivers.append(newreceivers)
                foundMix = False
                NazirSent = False
            elif foundMix:
                newreceivers.add(ip_dst)
            
            # print ('{}\t\t{}\t{}\t{}\t{}'.format(timestamp, eth_src, eth_dst, ip_src, ip_dst))
        # print(receivers)
        disjunct = disReceivers(receivers , NoParners)
        partners = exclusion_phase(disjunct, receivers)
        print(partners)
        ipSum = sumIP(partners)
        print(ipSum)

def disReceivers(receivers, noPartners):
    rec = receivers
    disjunct = []
    # För varje lista i receivers, kolla efterföljan de
    while len(disjunct) < noPartners:
        for iList in range(len(rec)-1):
            if is_disjunct(disjunct, rec[iList]):
                disjunct.append(rec[iList])
    return disjunct

def is_disjunct(disList, newSet):
    for disSet in disList:
        if not disSet.isdisjoint(newSet):
            return False
    return True

def exclusion_phase(dis, receivers):
    for receiver in receivers:
        foundIP = -1
        sameIP = False
        for indexDis in range(len(dis)):
            if not receiver.isdisjoint(dis[indexDis]):
                if foundIP == -1:
                    foundIP = indexDis
                else:
                    sameIP = True
                    break
                
        if not sameIP and not foundIP == -1:
            dis[foundIP] = dis[foundIP].intersection(receiver)

        singleIpLeft = True
        for s in dis:
            if len(s) != 1:
                singleIpLeft = False
        if singleIpLeft:
            break
    return dis



def sumIP(partners):
    ipSum = 0
    for s in partners:
        for ip in s:
            split = ip.split(".")
            for i in range(len(split)):
                split[i] = int_to_hexa(int(split[i]))
            hexstring = ''.join(split)
            print(hexstring)
            ipSum += hexa_to_int(hexstring)

    return ipSum


# Hexadecimal string to int
def hexa_to_int(inputVal):
    return int(inputVal, 16)


# Int to hexadecimal string
def int_to_hexa(inputVal):
    return hex(inputVal).lstrip('0x')

if __name__ == '__main__':
    main()

