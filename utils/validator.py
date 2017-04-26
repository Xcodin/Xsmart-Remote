import ConfigParser, os, inspect


config = ConfigParser.ConfigParser()
# Main Folder
mainFolder = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))), os.pardir))
# configuration file path
confPath = mainFolder + '/etc/Xsmart.conf'

try:
	config.readfp(open(confPath))
except Exception as e:
	print "configuration file not found"


