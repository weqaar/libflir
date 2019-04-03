import serial
from configInit import *

class Serial_Functions_FLIR():

	def __init__(self):
		self.parse = Parser_Functions()
		self.parse.parser_init()
		self.parse.ConfigSectionMap()

	def serial_init_FLIR(self):
		_section = 'FLIR'
		_device = self.parse.getSectionOption(_section, 'device')
		_baudrate = int(self.parse.getSectionOption(_section, 'baudrate'))
		_parity = self.parse.getSectionOption(_section, 'parity')
		_stopbits = int(self.parse.getSectionOption(_section, 'stopbits'))
		_bytesize = int(self.parse.getSectionOption(_section, 'bytesize'))
		_timeout = int(self.parse.getSectionOption(_section, 'timeout'))
		_inter_byte_delay = float(self.parse.getSectionOption(_section, 'inter_byte_delay'))
		self.ser = serial.Serial (port = _device, baudrate = _baudrate, timeout = _timeout, \
			   interCharTimeout = _inter_byte_delay, parity = _parity, stopbits = _stopbits, bytesize = _bytesize)
		self.ser.flush()

	def receive(self, _bufsize):
        	_buf = self.ser.read(_bufsize).encode('hex')
		self.flush_buffer()
		return _buf

	def serial_write(self, _cmd):
		self.ser.write(_cmd)
		print "wrote: " + _cmd

	def serial_read(self, _bytes):
		return self.ser.read(_bytes).encode('hex')

	def get_serial_conf(self):
		print self.ser.getSettingsDict()

	def flush_buffer(self):
		self.ser.flush()

