#! /usr/bin/env python

class Encoder:
	"""
	A class that can encrypt a message and return it to the calling environment
	"""
	def encrypt(self, rotors, plaintext, rotor_key, letter_key, binary):
		""" 
		Encrypts a message.
		
		@type      rotors: Rotors object
		@param     rotors: The set of rotors that will be used to encrypt the message
		
		@type   plaintext: string
		@param  plaintext: The message to be encrypted
		
		@type   rotor_key: integer
		@param  rotor_key: A modifier that determines which rotor is used
		
		@type  letter_key: integer
		@param letter_key: A modifier that determines which letter is used
		
		@type 	   binary: boolean
		@param     binary: A value that tells the function if it is dealing with binary modes or not
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
			self.ascii 				= self.original_list[self.index] if binary else ord(self.original_list[self.index])
			self.modifier_one		= (self.modifier_one + 1) * -1
			self.modifier_two		= (self.modifier_two + self.modifier_one) * -1
			self.modifier_total		= self.ascii + self.key_tens + self.modifier_two
			
			while (self.modifier_total < 0):
				self.modifier_total += rotors.rotor_length
				
			self.modifier_total 	%= rotors.rotor_length				
			self.rotor_choice 		= (self.rotor_choice + self.key_zero + 1) % rotors.rotor_limit
			
			self.encrypted 			+= rotors.rotor_set[self.rotor_choice][self.modifier_total]
		
		if binary:
			self.encrypted			= (self.encrypted).encode('utf-8')
	
	def get_encrypted(self):
		"""
		Returns the encrypted message.
		
		@rtype  self.encrypted: string if using text mode, bytes if using binary mode
		@return self.encrypted: The encrypted message
		"""
		return self.encrypted
