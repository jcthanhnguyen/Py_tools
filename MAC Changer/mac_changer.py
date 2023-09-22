import subprocess, optparse
import termcolor
import re

# Change interface's MAC to new_mac
def change_mac(interface, new_mac):
	print(termcolor.colored('\nChanging MAC address for ' + interface + ' to ' + new_mac + '...\n', 'green'))

	subprocess.call(['sudo', 'ifconfig', interface, 'down'])
	subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
	subprocess.call(['sudo', 'ifconfig', interface, 'up'])
	#subprocess.call('ifconfig', shell=True)


# create options for the command to input arguments of interface, new MAC
def get_args():	
	parser = optparse.OptionParser()
	parser.add_option('-i', '--interface', dest='interface', help='Interface to change its MAC address')
	parser.add_option('-m', '--mac', dest='new_mac_address', help='New MAC address of interface')
	parser.add_option('-o', '--os', dest='OS', help='Operating System of your machine (Linux, Windows, macOs)')
	
	options = parser.parse_args()[0]
	if not options.interface:
		parser.error('!! Please specify an interface !!')
	elif not options.new_mac_address:
		parser.error('!! Please specify a MAC address !!')
	return options

	
# compare the MAC with the user's MAC input, then go to conclusion	
def compare_mac(interface, new_mac):
	result = subprocess.check_output(['ifconfig', interface]).decode()
	result = re.findall('ether (\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)',result)

	if new_mac in result:
		print(termcolor.colored('[+] MAC address changed to ' + new_mac + ' SUCCESSFULLY', 'blue'))
	else:
		print(termcolor.colored('[-] CANNOT CHANGE MAC ADDRESS', 'red'))


# MAIN		
options = get_args()	
change_mac(options.interface, options.new_mac_address)
compare_mac(options.interface, options.new_mac_address)
