# -*- coding: utf-8 -*-

#!/usr/bin/env python

__author__ =    "Weqaar Janjua"
__contact__ = 	"weqaar.janjua@gmail.com"
__revision__ =  "$Id$"
__version__ =   "2.3"
__project__ =   "libFLIR"


import serial
import sys
import crc16 # https://code.google.com/p/pycrc16/
from commands_struct_FLIR import *


class FLIR_Functions():

	def __init__(self):
		global commands_struct 
		commands_struct = libflir_structs()


	# Returns: tuple (command, length of command)
	# _mode: cmd, get, set
	def _construct_cmd(self, _function_byte, _mode, _function_cmd='\x00'):

		# create function byte
		commands_struct._frame['function'] = commands_struct._function_code[_function_byte][0]
		
		# command mode
		if _mode not in commands_struct._function_code[_function_byte][1]:
			print "_mode not in commands_struct._function_code[_function_byte][1]\n"
			return False

		# create byte_count
		commands_struct._frame['byte_count'] = commands_struct._function_code[_function_byte][1][_mode]

		# Bytes 1 - 6
		bytes_1to6 = commands_struct._frame['pcode'] + commands_struct._frame['status'] + \
			     commands_struct._frame['reserved'] + commands_struct._frame['function'] + \
			     commands_struct._frame['byte_count']
			    
		# calculate crc1
		# crc16.crc16xmodem() returns int
		_crc1 = crc16.crc16xmodem(bytes_1to6)
		(_x, _y) = self.crc_to_hex(_crc1) 
		commands_struct._frame['crc1'] = _x + _y

		# Data byte (payload)
		if _mode == 'set':
			commands_struct._frame['data'] = commands_struct._function_code[_function_byte][2][_function_cmd]

		# Bytes 1 - N
		bytes_1toN = commands_struct._frame['pcode'] + commands_struct._frame['status'] + \
 			    commands_struct._frame['reserved'] + commands_struct._frame['function'] + \
			    commands_struct._frame['byte_count'] + commands_struct._frame['crc1'] + \
			    commands_struct._frame['data']

		print "bytes_1toN: \n"
		for i in commands_struct._frame:
			print i + " : " + commands_struct._frame[i].encode('hex')
		print "\n"

		# calculate crc2
		_crc2 = crc16.crc16xmodem(bytes_1toN)
		(_x, _y) = self.crc_to_hex(_crc2) 
		commands_struct._frame['crc2'] = _x + _y

		# assemble command
		_cmd = commands_struct._frame['pcode'] + commands_struct._frame['status'] + \
		       commands_struct._frame['reserved'] + commands_struct._frame['function'] + \
		       commands_struct._frame['byte_count'] + commands_struct._frame['crc1'] + \
		       commands_struct._frame['data'] + commands_struct._frame['crc2']		

		# Debug
		print "Resp: " + commands_struct._function_code[_function_byte][1]['resp'].encode('hex')
		print "Resp Int: " + str(int(commands_struct._function_code[_function_byte][1]['resp'].encode('hex')))

		return (_cmd, 10 + int(commands_struct._function_code[_function_byte][1]['resp'].encode('hex'))) 


	############ Commands #############


	### NO-OP ############################################### 

	# 
	def noop(self):
		retval = self._construct_cmd('NO-OP', 'cmd')
		return retval


	### SET DEFAULTS ############################################### 

	# 
	def set_defaults(self):
		retval = self._construct_cmd('SET_DEFAULTS', 'cmd')
		return retval


	### CAMERA RESET ############################################### 

	# 
	def camera_reset(self):
		retval = self._construct_cmd('CAMERA_RESET', 'cmd')
		return retval


	### RESET FACTORY DEFAULTS ############################################### 

	# 
	def reset_factory_defaults(self):
		retval = self._construct_cmd('RESET_FACTORY_DEFAULTS', 'cmd')
		return retval


	### SERIAL NUMBER ############################################### 

	# Serial Number
	def get_serial(self):
		retval = self._construct_cmd('SERIAL_NUMBER', 'cmd')
		return retval


	### GET REVISION ############################################### 

	# Get Revision
	def get_revision(self):
		retval = self._construct_cmd('GET_REVISION', 'cmd')
		return retval


	### GAIN MODE ############################################### 

	# Get Gain Mode
	def get_gain_mode(self):
		retval = self._construct_cmd('GAIN_MODE', 'get')
		return retval

	# Set Gain Mode - Automatic
	def set_gain_mode_automatic(self):
		retval = self._construct_cmd('GAIN_MODE', 'set', 'automatic')
		return retval

	# Set Gain Mode - Low Gain Only
	def set_gain_mode_low_gain(self):
		retval = self._construct_cmd('GAIN_MODE', 'set', 'lowgain')
		return retval

	# Set Gain Mode - High Gain Only
	def set_gain_mode_high_gain(self):
		retval = self._construct_cmd('GAIN_MODE', 'set', 'highgain')
		return retval

	# Set Gain Mode - Manual
	def set_gain_mode_manual_gain(self):
		retval = self._construct_cmd('GAIN_MODE', 'set', 'manualgain')
		return retval


	### FFC MODE SELECT ############################################### 

	# FFC MODE SELECT - manual
	def set_ffc_mode_select_manual(self):
		retval = self._construct_cmd('FFC_MODE_SELECT', 'set', 'manual')
		return retval

	# FFC MODE SELECT - automatic
	def set_ffc_mode_select_automatic(self):
		retval = self._construct_cmd('FFC_MODE_SELECT', 'set', 'automatic')
		return retval

	# FFC MODE SELECT - external
	def set_ffc_mode_select_external(self):
		retval = self._construct_cmd('FFC_MODE_SELECT', 'set', 'external')
		return retval


	### DO FFC ############################################### 

	# DO FFC
	def do_ffc(self):
		retval = self._construct_cmd('DO_FFC', 'cmd')
		return retval

	# DO FFC - Short
	def do_ffc_short(self):
		retval = self._construct_cmd('DO_FFC', 'set', 'short')
		return retval

	# DO FFC - Long
	def do_ffc_long(self):
		retval = self._construct_cmd('DO_FFC', 'set', 'long')
		return retval


	### FFC PERIOD ############################################### 

	# Get FFC PERIOD
	def get_ffc_period(self):
		retval = self._construct_cmd('FFC_PERIOD', 'get')
		return retval

	# Set FFC Period - Current
	def set_ffc_period_current(self, _ffc_interval):
		if type (_ffc_interval) == int:
			retval = self._construct_cmd('FFC_PERIOD_CURRENT', 'set', _ffc_interval)
		else:
			retval = False
		return retval

	# Set FFC Period - High Low
	def set_ffc_period_high_low(self, _ffc_interval_high, _ffc_interval_low ):
		if type (_ffc_interval_high) == int:
			if type (_ffc_interval_high) == int:
				retval = self._construct_cmd('FFC_PERIOD_HIGH_LOW', 'set', _ffc_interval_high + _ffc_interval_low)
			else:
				retval = False
		else:
			retval = False
		return retval


	### VIDEO MODES - ZOOM ############################################### 

	# Realtime
	def set_zoom_realtime(self):
		retval = self._construct_cmd('VIDEO_MODE', 'set', 'realtime')
		return retval

	# Freeze Frame
	def set_zoom_freeze_frame(self):
		retval = self._construct_cmd('VIDEO_MODE', 'set', 'freeze_frame')
		return retval

	# Zoom 2x
	def set_zoom_2x(self):
		retval = self._construct_cmd('VIDEO_MODE', 'set', '2x_zoom')
		return retval

	# Zoom 4x
	def set_zoom_4x(self):
		retval = self._construct_cmd('VIDEO_MODE', 'set', '4x_zoom')
		return retval

	# Video Modes
	def get_video_mode(self):
		retval = self._construct_cmd('VIDEO_MODE', 'get')
		return retval


	### VIDEO ORIENTATION - Invert, Revert, Normal, Invert + Revert ############################################### 

	# Normal
	def set_orientation_normal(self):
		retval = self._construct_cmd('VIDEO_ORIENTATION', 'set', 'normal')
		return retval

	# Invert
	def set_orientation_invert(self):
		retval = self._construct_cmd('VIDEO_ORIENTATION', 'set', 'invert')
		return retval

	# Revert
	def set_orientation_revert(self):
		retval = self._construct_cmd('VIDEO_ORIENTATION', 'set', 'revert')
		return retval

	# Invert + Revert
	def set_orientation_invert_revert(self):
		retval = self._construct_cmd('VIDEO_ORIENTATION', 'set', 'invert_revert')
		return retval


	### SPOT METER MODE - Disabled, (F) Farenheight, (C) Centigrade  ############################################### 

	# Disabled
	def set_spot_meter_disabled(self):
		retval = self._construct_cmd('SPOT_METER_MODE', 'set', 'disabled')
		return retval

	# F
	def set_spot_meter_F(self):
		retval = self._construct_cmd('SPOT_METER_MODE', 'set', 'F')
		return retval

	# C
	def set_spot_meter_C(self):
		retval = self._construct_cmd('SPOT_METER_MODE', 'set', 'C')
		return retval

	### SPOT DISPLAY - Off, Numeric, Thermometer, Numeric + Thermometer ############################################### 

	# Off
	def set_spot_display_off(self):
		retval = self._construct_cmd('SPOT_DISPLAY', 'set', 'off')
		return retval

	# Numeric
	def set_spot_display_numeric(self):
		retval = self._construct_cmd('SPOT_DISPLAY', 'set', 'numeric')
		return retval

	# Thermometer
	def set_spot_display_thermometer(self):
		retval = self._construct_cmd('SPOT_DISPLAY', 'set', 'thermometer')
		return retval

	# Numeric + Thermometer
	def set_spot_display_numeric_thermometer(self):
		retval = self._construct_cmd('SPOT_DISPLAY', 'set', 'numeric_thermometer')
		return retval


	###################################################################### 
	### VIDEO LUT - White hot,Black hot, Fusion, Rainbow, Globow, Ironbow1
        ### 		Ironbow 2, Sepia, Color1, Color2, Ice and Fire, Rain 
	###################################################################### 

	# White hot
	def set_lut_whitehot(self):
		retval = self._construct_cmd('VIDEO_LUT', 'set', 'whitehot')
		return retval

	# Black hot
	def set_lut_blackhot(self):
		retval = self._construct_cmd('VIDEO_LUT', 'set', 'blackhot')
		return retval

	# Fusion
	def set_lut_fusion(self):
		retval = self._construct_cmd('VIDEO_LUT', 'set', 'fusion')
		return retval

	# Rainbow
	def set_lut_rainbow(self):
		retval = self._construct_cmd('VIDEO_LUT', 'set', 'rainbow')
		return retval

	# Globow
	def set_lut_globow(self):
		retval = self._construct_cmd('VIDEO_LUT', 'set', 'globow')
		return retval

	# Ironbow1
	def set_lut_ironbow1(self):
		retval = self._construct_cmd('VIDEO_LUT', 'set', 'ironbow1')
		return retval

	# Ironbow2
	def set_lut_ironbow2(self):
		retval = self._construct_cmd('VIDEO_LUT', 'set', 'ironbow2')
		return retval

	# Sepia
	def set_lut_sepia(self):
		retval = self._construct_cmd('VIDEO_LUT', 'set', 'sepia')
		return retval

	# Color1
	def set_lut_color1(self):
		retval = self._construct_cmd('VIDEO_LUT', 'set', 'color1')
		return retval

	# Color2
	def set_lut_color2(self):
		retval = self._construct_cmd('VIDEO_LUT', 'set', 'color2')
		return retval

	# Ice and Fire
	def set_lut_iceandfire(self):
		retval = self._construct_cmd('VIDEO_LUT', 'set', 'iceandfire')
		return retval

	# Rain
	def set_lut_rain(self):
		retval = self._construct_cmd('VIDEO_LUT', 'set', 'rain')
		return retval

	# User-defined Custom
	def set_lut_custom(self):
		retval = self._construct_cmd('VIDEO_LUT', 'set', 'custom')
		return retval


	### ISOTHERM - Disabled, Enabled  ############################################### 

	# Disabled
	def set_isotherm_disabled(self):
		retval = self._construct_cmd('ISOTHERM', 'set', 'disabled')
		return retval

	# Enabled
	def set_isotherm_enabled(self):
		retval = self._construct_cmd('ISOTHERM', 'set', 'enabled')
		return retval


	############ Supporting Functions #############

	# Integer to Hex Converter
	#def int_to_hex (self, _int):
	#	print "int_to_hex input: " + str(_int) + "\n"
	#	hexchars = hex(_int)[2:]
	#	hexcharsa = hexchars[:2]
	#	hexcharsb = hexchars[-2:]
	#	hexcharsax = hexcharsa.decode('hex')
	#	hexcharsbx = hexcharsb.decode('hex')
	#	hexcharfull = hexcharsax + hexcharsbx
	#	return hexcharfull


	# Returns: two bytes hex tuple (MSB, LSB)
	def crcformat(self, crc):
    		msb = hex(crc >> 8)
    		lsb = hex(crc & 0x00FF)
    		return (msb, lsb)


	# Returns: two bytes hex encoded string tuple (MSB, LSB)
	def crc_to_hex(self, _crc):
		(_msb, _lsb) = self.crcformat(_crc)

		if len(_msb[2:]) is 1:
			hex_msb = '0' + _msb[2:]
		else:
			hex_msb = _msb[2:]

		if len(_lsb[2:]) is 1:
			hex_lsb = '0' + _lsb[2:]
		else:
			hex_lsb = _lsb[2:]

		return (hex_msb.decode('hex'), hex_lsb.decode('hex'))

# EOF
