import ConfigParser

class Parser_Functions():

	_instance = None
	global conf_file
	conf_file = "libFLIR.conf"
	conf_map = None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		self.sys_params = {'_device': '', '_baudrate': '', '_timeout': '', '_parity': '', \
				   '_stopbits': '', '_bytesize': '', '_inter_byte_delay': ''}

	def parser_init(self):
		self.conf = ConfigParser.ConfigParser()
		self.conf.read(conf_file)

	def ConfigSectionMap(self):
		sections = self.conf.sections()
		for section in sections:
			options = self.conf.options(section)
			for option in options:
				try:
					self.sys_params[option] = self.conf.get(section, option)
				except:
					self.sys_params[option] = None
		return self.sys_params

	# Input: getSectionOption ('Section', 'Option')
	def getSectionOption(self, _section, _option):
		return self.conf.get(_section, _option)

