#! /usr/bin/env python

class Encoder:
	def encrypt(self, rotors, plaintext, rotor_key, letter_key):
		""" 
		Encrypts a message.
		
		@type      rotors: Rotors object
		@param     rotors: The set of rotors that will be used to encrypt the message
		
		@type   plaintext: string
		@param  plaintext: The message to be encrypted
		
		@type   rotor_key: number
		@param  rotor_key: A modifier that determines which rotor is used
		
		@type  letter_key: number
		@param letter_key: A modifier that determines which letter is used
		"""
		self.key_zero				= rotor_key
		self.key_tens				= letter_key
		self.original_list			= list(plaintext)
		self.original_count			= len(self.original_list)
		self.modifier_one			= 0
		self.modifier_two			= 0
		self.rotor_choice			= 0
		self.encrypted				= ""
		
		for self.index in range (0, self.original_count):
			self.ascii 				= ord(self.original_list[self.index])				
			self.modifier_one		= (self.modifier_one + 1) * -1
			self.modifier_two		= (self.modifier_two + self.modifier_one) * -1
			self.modifier_total		= self.ascii + self.key_tens + self.modifier_two
			
			while (self.modifier_total < 0):
				self.modifier_total += rotors.rotor_length
				
			self.modifier_total 	%= rotors.rotor_length				
			self.rotor_choice 		= (self.rotor_choice + self.key_zero + 1) % rotors.rotor_limit
			
			self.encrypted 			+= rotors.rotor_set[self.rotor_choice][self.modifier_total]
	
	def get_encrypted(self):
		"""
		Returns the encrypted message.
		"""
		return self.encrypted
		