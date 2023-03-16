DNS App
The DNS app is a Python-based application that allows users to check if a website is available for use. The app connects to four devices: ts1 and ts2 (root DNS servers), ls (local DNS server), and the client (user).

How it works
When a user types a website name into their browser, the browser sends a request to the local DNS server (ls) to resolve the domain name into an IP address. If ls does not have the IP address cached, it forwards the request to either ts1 or ts2, the root DNS servers. ts1 and ts2 are not connected to each other.

ts1 and ts2 have a complete list of all the IP addresses for every top-level domain. They will search for the IP address of the domain name that the client requested and will return the IP address to ls. ls will then cache the IP address and forward it to the client's browser. The browser will use the IP address to establish a connection to the server hosting the website.

If ts1 and ts2 both respond with different IP addresses, ls will choose the fastest response and return it to the client. If there is no response from ts1 and ts2, ls will return an error message to the client.

Files
The DNS app is composed of four Python files:

client.py: Sends a DNS query to the local DNS server and receives the IP address in response.
ls.py: Listens for DNS queries from the client and forwards them to either ts1 or ts2. Caches the IP address of the domain name for future use.
ts1.py: Listens for DNS queries from ls and responds with the IP address of the domain name.
ts2.py: Listens for DNS queries from ls and responds with the IP address of the domain name.
Conclusion
The DNS app is a Python-based application that connects to four devices to check if a website is available for use. The app follows the DNS protocol to resolve a domain name into an IP address. The app consists of four Python files, each of which has a specific role to play in the DNS resolution process.
