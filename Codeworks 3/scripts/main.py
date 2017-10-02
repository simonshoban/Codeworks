#! /usr/bin/env python

from machine import Machine

machine = Machine()

prefix = "../text/"

file1 = open(prefix + "file1.txt", "r")
file2 = open(prefix + "file2.txt", "w")
file3 = open(prefix + "file3.txt", "w")

rotor_config 	= "ABAE07D6CDEF28497234987A0BCD"							#Use any hexadecimal string
rotor_key		= 3490														#Use any number
letter_key		= -23843													#Use any number

machine.configure(rotor_config)
machine.encrypt(machine, file1.read(), rotor_key, letter_key)
machine.decrypt(machine, machine.get_encrypted(), rotor_key, letter_key)

file2.write(machine.get_encrypted())
file3.write(machine.get_decrypted())

file1.close()
file2.close()
file3.close()