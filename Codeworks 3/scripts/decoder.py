#! /usr/bin/env python

class Decoder:
	def decrypt(self, rotors, ciphertext, rotor_key, letter_key):
		""" 
		Decrypts a message.
		
		@type      rotors: Rotors object
		@param     rotors: The set of rotors that were used to encrypt the original message
		
		@type  ciphertext: string
		@param ciphertext: The message to be decrypted
		
		@type   rotor_key: number
		@param  rotor_key: A modifier that determines which rotor is used
		
		@type  letter_key: number
		@param letter_key: A modifier that determines which letter is used
		"""
		self.key_zero				= rotor_key
		self.key_tens				= letter_key
		self.encoded_list			= list(ciphertext)
		self.encoded_count			= len(self.encoded_list)
		self.backwards 				= ""
		self.decrypted				= "" 
		
		for self.index in range (self.encoded_count, 0, -1):
			self.rotor_choice 		= (self.index + self.index * self.key_zero) % rotors.rotor_limit
			self.modifier_total 	= rotors.rotor_set[self.rotor_choice].index(self.encoded_list[self.index - 1])
			self.modifier_two 		= self.index // 2 * -1 + (self.index % 2) * self.index
			self.convert 			= self.modifier_total - self.key_tens - self.modifier_two
			
			while (self.convert < 0):
				self.convert 		+= rotors.rotor_length		
				
			self.convert 			%= rotors.rotor_length	
			self.ascii 				= chr(self.convert)
			self.backwards 			+= self.ascii
			
		for self.index in reversed (self.backwards):
			self.decrypted 			+= self.index;
	
	def get_decrypted(self):
		"""
		Returns the decrypted message.
		"""
		return self.decrypted
		