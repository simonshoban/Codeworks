#! /usr/bin/env python

from rotors import Rotors
from encoder import Encoder
from decoder import Decoder

class Machine(Rotors, Encoder, Decoder):
	pass