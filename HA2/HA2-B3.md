https://www.onion-router.net/Publications/locating-hidden-servers.pdf

# Summary Report on attacks
The report is about attacks using a hostile Tor node to reveal hidden servers.

## Introduction
Tor is the largest anonymity network and it uses onion routing. Resistant do DDoS attack on a hidden server since it requires a DDoS attack on the entire hidden network. It has been recommended by numerous sources to hide a server through these networks to preserve anonymity and resist censorship, but the Tor development team insists that you should not use Tor to rely on strong anonymity. 

The attacks used are cheap and fast and locates the hidden servers in a matter of minutes.

## Previous work on hiding services and anonymity
In onion routing each jump between nodes in the network removes or adds a layer, hence the name onion routing. All layers use public key encryption. The keys are shared between the client and the node that was given the key in establishing the circuit. 

Not sure this part is needed for the quiz answers..

## Location-hidden services in Tor
One vulnerability for a hidden service in Tor is the selection of the first and last node in the path through the network. If an adversary can watch the edges (first and last node), she can confirm the identity of the one who is communicating. This is true because of the low-latency requirements, it is easy to confirm the timings

The normal use flow of hidden services and rendezvous servers:
![](https://i.gyazo.com/3d64826adc4265e2194fe72da4b81d9e.png)

All the message flows are anonymized, ther are routed through several nodes on their way to the receiver. 
- The Hidden Server (HS) connects to a node in the Tor network and asks if the node can act as an Introduction Point (IP) for his service. If the node accepts, the new circuit is created. Otherwise the HS will ask other nodes until it gets accepted. The connection is kept until a node restart or decides to put it down.
- The HS now contacts the Directory Server and asks for its contact information to be published of its hidden services. In the Directory Server, all the contact information from the hidden services are stored.
- The Client asks the DS for the contact information to the HS, including addresses of the IPs of the service. Could be more than one.
- The Client now selects a node in the network to act as a Rendezvous Point (RP) and contacts it. The RP will listen for connections from the hidden server on the Client's behalf. 
- When a node accepts the role, the Client will contact the IP and asks the IP to forward the information about the RP to the HS. 
- The HS chooses if it should accept and connect to the RP. If OK, the HS connects and asks to be connected to the circuit.
- The RP forwards the request to the Client, and the anonymous data tunnel through the RP is created. 

Some facts that come out of this:
* The client does not know the location (IP address) of the HS, but knows the location of RP
* Same goes for the HS
* RP does not know the location of either one, and neither the contect of the message or what service it is serving.
* There are 2 or more nodes between HS and RP as well as RP and the Client to hide traffic and create a degree of anonymity.
* Any member of the network which claims to offer stability can be used by HS to form an anonymous tunnel to RP, including the Client if it is a node in the anonymization network. This is the basis of the attacks presented below!

## Attacks and Experimental Results
