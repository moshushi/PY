import sys, socket, struct
def ip2long(ip):
	packedIP = socket.inet_aton(ip)
	return struct.unpack("!L", packedIP)[0]
def long2ip(lol):
	return socket.inet_ntoa(struct.pack('!L', lol))
a, b = sys.argv[1], sys.argv[2]
m = ip2long(a)
while m < (ip2long(b)+1):
	print (long2ip(m))
	m = m + 1
