import hashlib
import random
import time


def h(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def last_B_bytes(M,B):
	# Return last B bytes after hashing 
	h_M = h(str(M)) # convert M to a string and hash it
	# Note: h_M is returned in hex, each byte needs 2 characters
	last_byte = h_M[(-2*B):] # last B bytes of h(M)
	last_byte_int = int(last_byte, 16) # convert to int
	format_string = '0'+str(8*B)+'b'
	last_byte_bin = format(last_byte_int,format_string)
	return last_byte_bin

total_time = time.time()
for B in range(1,9):
	M = 'ab'
	P = random.getrandbits(8*B)
	format_string = '0'+str(8*B)+'b'
	P_bin = format(P,format_string)
	last_byte_bin = last_B_bytes(M,B)

	start_time = time.time()
	for counter in range(1,1001):
		M = 'ab'
		last_byte_bin = last_B_bytes(M,B)
		while(last_byte_bin != P_bin):
			# Generate random M
			M = random.randint(0,999999999999999999999)
			# last_byte_bin has last bits of hashed M in binary
			last_byte_bin = last_B_bytes(M,B)
			# Perform check on last byte
			if(last_byte_bin == P_bin):
				if(counter == 10):
					print('-------------------------')
					print('B =',B,', Success Count =',counter)
					print(time.time()-start_time,'seconds')
					print('-------------------------')
				if(counter == 100):
					print('-------------------------')
					print('B =',B,', Success Count =',counter)
					print(time.time()-start_time,'seconds')
					print('-------------------------')
	B_time = time.time()-start_time #B_time is the time for each B
	print('############# B =',B,'completed #############')
	print('Total Time (seconds)', (B_time))
	print('Total Time (minutes)',((B_time)/60))
	print('Average Time Per Success (seconds) =',(B_time/(counter)))
	
end_time = time.time()
print('!!!!!!!!!!!!---- Program Completed ----!!!!!!!!!!!!')
print('Total Program Time (seconds):',end_time-start_time)	
print('Total Program Time (minutes):',(end_time-start_time)/60)									