#! /usr/bin/env python

from machine import Machine

machine 		= Machine()
prefix 			= "../text/"
binary			= True														#True for binary modes, False for text modes
file_mode  		= ["rb", "wb+", "wb"] if binary else ["r", "w+", "w"]
rotor_config	= "ABAE07D6CDEF28497234987A0BCD"							#Use any hexadecimal string
rotor_key		= 3490														#Use any integer
letter_key		= -23843													#Use any integer

with open(prefix + "file1.txt", file_mode[0]) as file1:
	plaintext 	= file1.read()

machine.configure(rotor_config)
machine.encrypt(machine, plaintext, rotor_key, letter_key, binary)

with open(prefix + "file2.txt", file_mode[1]) as file2:
	file2.write(machine.get_encrypted())
	file2.seek(0)
	ciphertext 	= file2.read()
	
machine.decrypt(machine, ciphertext, rotor_key, letter_key, binary)

with open(prefix + "file3.txt", file_mode[2]) as file3:
	file3.write(machine.get_decrypted())
