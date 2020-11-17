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
* There are 3 nodes between HS and RP and 2 between the RP and the Client to hide traffic and create a degree of anonymity. (Fixed numbers for the experiments, can be more I guess?)
* Any member of the network which claims to offer stability can be used by HS to form an anonymous tunnel to RP, including the Client if it is a node in the anonymization network. This is the basis of the attacks presented below!

## Attacks and Experimental Results
![](https://i.gyazo.com/e15da7a7837d28cce219e837049eea44.png)
The attacks are all used to determine the IP address of the HS. There are four attack methods, and all of these can be carried out by an adversary as long as it controls at least one node in the network. Anyone can volunteer to be a Tor node, so it is trivial. 

To describe the general case:
An attacker controls the Client and one node in the network. As you can see in the picture, the attacker wants to control the first node in the communication channel from the HS to the RP. Among the circuits created by her controlled node, the attacker can analyze the traffic pattern when she sends to and receives from the HS. If she finds a match, then her node is part of the circuit to the HS. Since she controls the Client, she knows the IP address of the RS. If both of the IP addresses used in the controlled node when the messages are forwarded are unknown to the attacker, then she knows that it is either node 1 or node 2. If there is an known address, the IP of the RP, she knows that it is node 3. By continuously abandon the circuit and perform the attack again, the attacker can sample information about the different addresses. When she has enough information, the attacker can know when she is connected as node 1 and thereby know the IP address of the HS. 

### Experimental setup
Not really important for the quizes, I think. This part just describes the setup of the experiment

### Timing analysis
The attacker uses the logged timing data and direction from the generated data set and the sampled data set from the circuits created in that period of time to find two things:
* Confirm that the attacker's node is part of a circuit
* If it is true, determine which position it is located in (Node 1, 2, or 3)

The sampled data set, the generated set by the Client, and the sampled data done by the server are all compared to each other to identify the generated data set. The match confirmation is an extended version of the packet counting attack described by Serjantov and Sewell (No clue what it is). 

I didn't quite understand the technical parts here. Something about comparing the data packets depending on when they were sent and received from the different data sets. 

### Service Location Attack
There are two different scenarios for the HS:
1: *Server Scenario* - When the hidden service is located on a node within the anonymous network. Ofter used to hide service traffic within all the other trafic happening in the network. 
2: *Client Scenario* - When the hidden service is located on a Client node using but not participating in a network. Often used when it is desired that the HS should not be listed in the Directory Service as a participating node of the network. 

When using the Server Scenario, it is possible to correlate information about the availability of the service and the availability of the nodes listed in the DS. An attacker could poll each listed server every five minutes and correlate the lists of available active servers. 