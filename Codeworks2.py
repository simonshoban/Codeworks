#! /usr/bin/env python

import sys

rotorI 		= [' ','!','"','$','%','&','\'','(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[','\\',']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~']
rotorII 	= ['B','r','`','9','\\','o','}','h',')','E','p','-','4','@','1','A',',','y','l','z','+','^','n','s','u','*','k','_','2','e','N','d','$','/','X','\'','S','<','w','b','i','O','|','(','v','0','!','6','R','t','&','I','Y','C','m','%','?','7','.','M','c','f','K','q','a','F','D','8','~','Q','P','3','>','{','T',';','"','[',']','5','x','W','Z','g',':','=','j','U','L','J','G','H',' ','V']
rotorIII	= ['"','p','d','7','{','B','W','U','y','i','>',' ','k',',','@','w','6','X','g','`','3','E','(','a','0','M','4','m','v','2','C','J','q',':',')','<','D','!','~','\'','o','h','N',';','*','t','5','\\','F','f','$','%','L','H','u','V','|','n','/','Z','A','P','I','b','_','.','&','1',']','=','^','+','Q','T','-','z','O','K','S','Y','R','8','r','e','?','}','s','[','G','l','c','9','x','j']
rotorIV 	= ['p','O','=','>',';','V','F','H',',','~','"','+','?','7','\'','u','`','0','2','%','D','@','d','r','k','j','f','l',':','3','P','J','b','c','X','x','i','G','v','[','$','E','\\','s','B',')','{','a','L','n','9','y','Z','4','5','1','-','t','q','M','.','A','8','6','Y','N','!','I','m','K','}','|','/','^','w','U','&','e','z','Q','R','C',']','<','_','o','g','T',' ','*','S','h','(','W']
rotorV 		= ['\'','X','%',':','D','<','_','h','6','/','V','9','`','s',',','H','z','i','o','.','n','A','y','T','1','2','v','Y','J','C','3','M','^','N',';','I','k','8','j','g','F','\\','@','0','U','7','5','(','Z','-','G','$','!','{','x','f','c','|','P','d','4','m','=',']','}','&','"','~','>',' ','+','a','E','*','l','?','W','e',')','r','t','b','L','S','p','w','q','u','R','O','[','B','Q','K']
rotorVI 	= ['D',')','t','7',']','u','}','G','H',';','$','c','.','(','6','`','1','E','4','%','w','!','d','/','=','M','B','~','a','>','m','Q','0','P','z','\\','9','V','N','v','f','j','2',',','T','\'','b','S','q','+','k','^','Y','X','h','@','R','W','e','A','x','i','n','{','J','g','O','-','8','<','5','L','U','[','_','|','Z','o','&','F','K',':','C','I','p','l','s',' ','*','3','y','r','"','?']
rotorVII	= [':','v','%','O','=','[','i','Z','{','W','I','n','.','8','J','C','Y','p','7','0','`','K',')','E','o','4','j','R','d','X','V','s','&','z','\\','w',' ','F','/','-','*','T','!','x','e','1','?',']','P','B',',','9','@','u','+','c','b','f','(','N','k','r','5','~','t','l','}','\'','$','G','S','M','<','A','"','D','2','^',';','m','L','6','|','>','3','Q','H','_','a','h','q','g','U','y']
rotorVIII	= ['"','n','C','^','L','f','u','i','A','.','>','Q','Z','%','J','?','x','5','0','*','U','2','V','{','\\','W','h','}',':','I','!','_','P','`','g','w',',','H',';','&','8','3','|',')','z','e','1','E','l','~','y','/','9','F','(','G','M','v','<','7','X','$','k','p','o','D','+','[','-','c','S','=','N','s',']','R','Y','6','t','m','O','\'','q','b','a','j','@','r','K','B','T','d','4',' ']
rotorIX		= ['z',',','H','Y','y','1','B','t','K','A','R','?','a','d','_','*','s','o','~','{','.','c','(','U','f','[','6','L','E','x','e','S','0','Q',')','"','k','j','p','G','g','M','u','\'','8','X','+','r','n','m','@','h','\\','4','/',':','b','>',';','w','&','`','q','W','O','|',']','!','^','P','N',' ','-','}','7','i','V','<','%','J','C','l','=','I','F','$','9','Z','D','T','3','2','5','v']
MalcolmX	= ['k','\'','*','-',';','8','|','g','!','H','~',')','6',' ','I',',','^','w','q','Q','<','?','%','o','[','>',']','i','t','@','E','K','R','1','A','z','_','b','Z','n','7','u','9','V','U','S','m','3','.','0','r','D','O','&','d','4','G','M','x','"','P','}','l',':','2','v','h','5','F','c','X','{','C','B','y','N','`','/','f','a','$','e','L','=','J','W','\\','T','s','p','(','j','Y','+']
rotorXI		= ['\'','@','z','1','i','{','_','d','0','R','\\','M','!','e','T','n','6','J','<','O','/','N',')','P','=','y','l','o','G','b','r',',','|','.','4','`','[','x','&','-','X','s','g','5','A','F',' ','"','W',':','C','L',']','w','Y','~','7','E','2','j','$','^','v','p','V','9','}',';','m','?','I','(','t','Z','+','%','f','>','a','8','k','*','u','K','3','B','H','D','S','U','Q','c','q','h']
rotorXII	= ['3','n','5','V','D','+','.','M','~','*','F','\'','E','A','w','e','J','G','/','m','!','_','Q','%','L','0','4','d','?','g','O','6','2','b','y','(','r',';','o','@','U','{','X','h','S','=','B','\\','v','s',']','<','t','q','"','>','u','7','-','p',':','}','|','c','Z','H','^','9','T','z','l',',','I',' ','j','Y','8','C','$','P','R','f','W','k','[','N','i','`','&',')','x','1','K','a']
rotorXIII	= ['m','i','F','&','b','W','q','+','4','<','\\','H','K','!','I','a','"','@','7','?','c','d','>','z','%','[','C','1','L',',','j','V','0','|','l','2','A','f','5',':','N','Z','^','w',';','E',' ','J','P','3','D','S','/','*','T','o','n','v','u','`','y','8','_','t','{','U','k','-','Q','s','e','p',']','r','B','=',')','(','~','}','M','O','x','$','.','\'','h','g','9','G','6','R','Y','X']
rotorXIV	= ['$','}','x','-','<','y','n','H','Q','M','L','l','S','K',')','\'','V','.','J','A','[','+','D','{',' ','%','5','0','_','O','@','7','`','C','T','e','Y',':','r','=','6','U','2','c','I','~','P','B','j','b','!','\\','*','N','m','h','E','&','g','(','/','i','3','a','q','?','o','k','|','W','^',';','d','X','s',']','f','p','Z','G','R','"','>','v','u','w','t','z','8',',','4','F','1','9']
rotorXV		= ['o','-','@','t','9','N','Q','?','*','\'','}','6','(','_','n','h','i',',','v','2','0','T','<','M','$','G','!','Y',')','r','H','\\','p','F','l','.','q','D','=','a','w','S','I','m','8','1','B','4','s',';','W','U','X','{','k','j','%','A',']','[','P','>','f','V','7','d','K','`','E','|','5',' ','O','c','&','u','e','L','~','^','C','J','+','R','"','g','z','b',':','3','y','/','Z','x']
rotorXVI	= ['{','\\','O','&','=','I','P','l','G','$','Y','8','(','r','s',')','/','n','2','3','m','T','h','C',':','%','u','H','X','L',';','a','K','W','V','?','\'',',','~','f','E','Z','Q','@','y','`','*','.','6','R','b','U','B','|','w',']','_','c','1','<','A','F','^','g','}','+','z','d','j','k','"','5','D','x','o','0','S','q','>','N','M','J','9','t','e','!','4','[','7','-',' ','p','v','i']

all_rotors	= [rotorI, rotorII, rotorIII, rotorIV, rotorV, rotorVI, rotorVII, rotorVIII, rotorIX, MalcolmX, rotorXI, rotorXII, rotorXIII, rotorXIV, rotorXV, rotorXVI]
rotor_set 	= [rotorI, rotorII, rotorIII, rotorIV, rotorV, rotorVI, rotorVII, rotorVIII, rotorIX, MalcolmX]

rotor_limit = len(rotor_set)
rotor_length = len(rotorI)

while True:
	choice = input("\nEncode, decode, or configure rotors? [E/D/C]	" )
	
	if choice == "c" or choice == "C":
		rotor_config 		= input("\nEnter the rotor configuration: ")
		rotor_list			= list(rotor_config)
		rotor_limit 		= len(rotor_list)
		
		for itm in range (0, rotor_limit):
			rotor_key		= int(rotor_list[itm], 16)
			
			if rotor_key == 0:
				rotor_key = 16
				
			rotor_list[itm]	= all_rotors[rotor_key - 1]
		
		rotor_set = rotor_list
			
	if choice == "e" or choice == "E":
		original 			= input("\nWhat would you like to encode?\n\n")
		key					= input("\nEnter a 3 digit key: ")
		key_zero			= int(key[0])
		key_tens			= int(key[1] + key[2])
		original_list		= list(original)
		original_count		= len(original_list)
		modifier_one		= 0
		modifier_two		= 0
		rotor_choice		= 0
		
		print(),
		
		for index in range (0, original_count):
			ascii 			= ord(original_list[index])
			convert			= ascii - 32			
			modifier_one	= (modifier_one + 1) * -1
			modifier_two	= (modifier_two + modifier_one) * -1
			modifier_total	= convert + key_tens + modifier_two
			
			while (modifier_total < 0):
				modifier_total += rotor_length
				
			modifier_total 	%= rotor_length				
			rotor_choice 	= (rotor_choice + key_zero + 1) % rotor_limit
			
			sys.stdout.write(rotor_set[rotor_choice][modifier_total])
	
		print(),
		
	if choice == "d" or choice == "D":
		encoded 			= input("\nWhat would you like to decode?\n\n")
		key					= input("\nEnter the 3 digit key: ")
		key_zero			= int(key[0])
		key_tens			= int(key[1] + key[2])
		encoded_list		= list(encoded)
		encoded_count		= len(encoded_list)
		original			= ""
		
		print(), 
		
		for index in range (encoded_count, 0, -1):
			rotor_choice 	= (index + index * key_zero) % rotor_limit
			modifier_total 	= rotor_set[rotor_choice].index(encoded_list[index - 1])
			modifier_two 	= index // 2 * -1 + (index % 2) * index
			convert 		= modifier_total - key_tens - modifier_two
			
			while (convert < 0):
				convert += rotor_length		
				
			convert 		%= rotor_length	
			ascii 			= chr(convert + 32)	
			original 		+= ascii
		
		original 			= list(original)
		
		for index in reversed (original):
			sys.stdout.write(index)
			
		print(),