#! /usr/bin/env python

class Decoder:
	"""
	A class that can decrypt a message and return it to the calling environment
	"""
	def decrypt(self, rotors, ciphertext, rotor_key, letter_key, binary):
		""" 
		Decrypts a message.
		
		@type      rotors: Rotors object
		@param     rotors: The set of rotors that were used to encrypt the original message
		
		@type  ciphertext: string
		@param ciphertext: The message to be decrypted
		
		@type   rotor_key: integer
		@param  rotor_key: A modifier that determines which rotor is used
		
		@type  letter_key: integer
		@param letter_key: A modifier that determines which letter is used
		
		@type 	   binary: boolean
		@param     binary: A value that tells the function if it is dealing with binary modes or not
		"""
		self.key_zero				= rotor_key
		self.key_tens				= letter_key
		self.encoded_list			= list(ciphertext)
		self.encoded_count			= len(self.encoded_list)
		self.backwards 				= ""
		self.decrypted				= "" 
		
		for self.index in range (self.encoded_count, 0, -1):
			self.rotor_choice 		= (self.index + self.index * self.key_zero) % rotors.rotor_limit
			self.current_symbol		= chr(self.encoded_list[self.index -1]) if binary else self.encoded_list[self.index - 1]
			self.modifier_total 	= rotors.rotor_set[self.rotor_choice].index(self.current_symbol)
			self.modifier_two 		= self.index // 2 * -1 + (self.index % 2) * self.index
			self.convert 			= self.modifier_total - self.key_tens - self.modifier_two
			
			while (self.convert < 0):
				self.convert 		+= rotors.rotor_length		
				
			self.convert 			%= rotors.rotor_length	
			self.ascii 				= chr(self.convert)
			self.backwards 			+= self.ascii
			
		for self.index in reversed (self.backwards):
			self.decrypted 			+= self.index;
			
		if binary:
			self.decrypted 			= (self.decrypted).encode('utf-8')
	
	def get_decrypted(self):
		"""
		Returns the decrypted message.
		
		@rtype  self.decrypted: string if using text mode, bytes if using binary mode
		@return self.decrypted: The decrypted message
		"""
		return self.decrypted
