# Structures for Frame and Command Definitions

class libflir_structs():

	# Frame format:		|pcode|status|reserved|function|byte_count|crc1|data|crc2|
	_frame = {
		   'pcode':	'\x6E',		# Process Code			-	1 byte
		   'status':	'\x00',		# Status Code			-	1 byte
		   'reserved':	'\x00',		# Reserved			-	1 byte
		   'function':	'\x00', 	# Function Byte (_function_code)-	1 byte
		   'byte_count':'\x00\x00', 	# Byte Count			-	2 bytes
		   'crc1':	'\x00\x00', 	# CRC CCITT-16, bytes 1:6	- 	2 bytes
		   'data':	'\x00\x00', 	# Data (Payload)		-	0 - 32 bytes
		   'crc2':	'\x00\x00'	# CRC CCITT-16, bytes 1:N(data)	-       2 bytes
		 }


	# Format: Command Hex Code, Byte Size (command, response, get, set)
	_function_code = {
			  'NO-OP':			('\x00', {'cmd':'\x00\x00', 'resp':'\x00\x00'}),
			  'SET_DEFAULTS':		('\x01', {'cmd':'\x00\x00', 'resp':'\x00\x00'}),
			  'CAMERA_RESET':		('\x02', {'cmd':'\x00\x00', 'resp':'\x00\x00'}),
			  'RESET_FACTORY_DEFAULTS':	('\x03', {'cmd':'\x00\x00', 'resp':'\x00\x00'}),
			  'SERIAL_NUMBER':		('\x04', {'cmd':'\x00\x00', 'resp':'\x00\x08'}),
			  'GET_REVISION':		('\x05', {'cmd':'\x00\x00', 'resp':'\x00\x08'}),
			  'GAIN_MODE':			('\x0A', {'resp':'\x00\x00', 'get':'\x00\x00', 'set':'\x00\x02'}),
			  'FFC_MODE_SELECT':		('\x0B', {'resp':'\x00\x02', 'get':'\x00\x00', \
								  'set':'\x00\x02'}, {'manual':'\x00\x00', \
								  'automatic':'\x00\x01', 'external':'\x00\x02'}),
			  'DO_FFC_SHORT':		('\x0C', {'cmd':'0', 'resp':'0', 'get':'0', 'set':'0'}),
			  'DO_FFC_LONG':		('\x0C', {'cmd':'2', 'resp':'2', 'get':'0', 'set':'0'}),
			  'FFC_PERIOD_CURRENT':		('\x0D', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'FFC_PERIOD_HIGH_LOW':	('\x0D', {'cmd':'0', 'resp':'4', 'get':'0', 'set':'4'}),
			  'FFC_TEMP_DELTA_CURRENT':	('\x0E', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'FFC_TEMP_DELTA_HIGH_LOW':	('\x0E', {'cmd':'0', 'resp':'4', 'get':'0', 'set':'4'}),
			  'VIDEO_MODE':			('\x0F', {'resp':'\x00\x02', 'get':'\x00\x00', 'set':'\x00\x02'}, \
								 {'2x_zoom': '\x00\x04', 'freeze_frame': '\x00\x01', \
							 	  '4x_zoom': '\x00\x08', 'realtime': '\x00\x00'}),
			  'VIDEO_LUT':			('\x10', {'resp':'\x00\x02', 'get':'\x00\x00', 'set':'\x00\x02'}, \
                                                                 {'whitehot': '\x00\x00', 'blackhot': '\x00\x01', \
                                                                  'fusion': '\x00\x02', 'rainbow': '\x00\x03', \
								  'globow': '\x00\x04', 'ironbow1': '\x00\x05', \
								  'ironbow2': '\x00\x06', 'sepia': '\x00\x07', \
								  'color1': '\x00\x08', 'color2': '\x00\x09', \
								  'iceandfire': '\x00\x0A', 'rain': '\x00\x0B', \
								  #'custom': '\x00\x00', \ # Use only if implemented
								  }),
			  'VIDEO_ORIENTATION':		('\x11', {'resp':'\x00\x02', 'get':'\x00\x00', 'set':'\x00\x02'}, \
								 {'normal': '\x00\x00', 'invert': '\x00\x01', \
								  'revert': '\x00\x02', 'invert_revert': '\x00\x03'}),
			  'DIGITAL_OUTPUT_MODE':	('\x12', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'AGC_TYPE':			('\x13', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'CONTRAST':			('\x14', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'BRIGHTNESS':			('\x15', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'BRIGHTNESS_BIAS':		('\x18', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'SPOT_METER_MODE':		('\x1F', {'resp':'\x00\x02', 'get':'\x00\x00', 'set':'\x00\x02'}, \
								 {'disabled': '\x00\x00', 'F': '\x00\x01', 'C': '\x00\x02'}),
			  'READ_SENSOR':		('\x20', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'EXTERNAL_SYNC':		('\x21', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'ISOTHERM':			('\x22', {'resp':'\x00\x02', 'get':'\x00\x00', 'set':'\x00\x02'}, \
                                                                 {'disabled': '\x00\x00', 'enabled': '\x00\x01'}),
			  'ISOTHERM_THRESHOLDS':	('\x23', {'cmd':'0', 'resp':'4', 'get':'0', 'set':'4'}),
			  'TEST_PATTERN':		('\x25', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'GET_SPOT_METER':		('\x2A', {'resp':'\x00\x02', 'get':'\x00\x00'}),
			  'SPOT_DISPLAY':		('\x2B', {'resp':'\x00\x02', 'get':'\x00\x00', 'set':'\x00\x02'}, \
								 {'off': '\x00\x00', 'numeric': '\x00\x01', \
                                                                  'thermometer': '\x00\x02', 'numeric_thermometer': '\x00\x03'}),
			  'FFC_WARN_TIME':		('\x3C', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'AGC_FILTER':			('\x3E', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'PLATEAU_LEVEL':		('\x3F', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'GET_SPOT_METER_DATA':	('\x43', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'0'}),
			  'AGC_ROI':			('\x4C', {'cmd':'0', 'resp':'8', 'get':'0', 'set':'0'}),
			  'AGC_ROI_NORMAL':		('\x4C', {'cmd':'0', 'resp':'\x00\x18', 'get':'2', 'set':'\x00\x18'}),
			  'ITT_MIDPOINT':		('\x55', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'CAMERA_PART':		('\x66', {'cmd':'0', 'resp':'\x00\x20', 'get':'0', 'set':'0'}),
			  'MAX_AGC_GAIN':		('\x6A', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'PAN_AND_TILT':		('\x70', {'cmd':'0', 'resp':'4', 'get':'0', 'set':'4'}),
			  'VIDEO_STANDARD':		('\x72', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'SHUTTER_POSITION':		('\x79', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'DDE_GAIN':			('\x2C', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'DDE_THRESHOLD':		('\xE2', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'SPATIAL_THRESHOLD':		('\xE3', {'cmd':'0', 'resp':'2', 'get':'0', 'set':'2'}),
			  'GAIN_SWITCH_PARAMS':		('\xDB', {'cmd':'0', 'resp':'8', 'get':'0', 'set':'\x00\x08'})
			}

# END 
