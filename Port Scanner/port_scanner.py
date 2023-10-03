import socket, termcolor


# input function, return option 1 or 2

def opt_input():
	while True:
		try:
			print('\n1. Scan Specific Ports')
			print('2. Scan Series Of Ports')
			opt = int(input('[*] Choose your option (1/2): '))
			if opt < 1 or opt > 2:
				print(termcolor.colored('\n!! Invalid input, choose again !!', 'red'))
			else:
				return opt
		except:
			print(termcolor.colored('\n!! Invalid input, choose again !!', 'red'))

# input func, return yes or no

def cont_quit():
	while True:
		deci = input('\n[*] Do you want to scan again (y/n): ')
		if deci != 'y' and deci != 'n':
			print(termcolor.colored('!! Invalid input, choose again !!', 'red'))
		else:
			return deci
 
# scan 1 target, 1 port

def scan(target, port):
	try:
		sock = socket.socket()
		sock.connect((target, port))
		sock.settimeout(1)
		print(termcolor.colored('[+]', 'green') + ' Port Opened', port)
		sock.close()
	except:
		print(termcolor.colored('[-]', 'red') + ' Port Closed/Filterd', port)

# scan 1 target, scan serie of ports

def scan_series(target):
	start = int(input('\n[*] Enter your starting port for ' + target + ': '))
	end = int(input('[*] Enter your ending port for ' + target + ': '))
	print(termcolor.colored('\n' + ' Starting Scan For ' + str(target) + ' . . .\n', 'cyan'))
	for port in range(start, end+1):
		scan(target, port)

# scan 1 target, scan specific ports

def scan_spe(target):
	ports = input('\n[*] Enter ports you want to scan for ' + target +'(split with space): ').split()
	print(termcolor.colored('\n' + ' Starting Scan For ' + str(target) + ' . . .\n', 'cyan'))
	for port in ports:
		scan(target, int(port))
  

# main	
print(termcolor.colored('\n***** Port Scanner *****\n', 'magenta'))
while True:
        targets = input('\n[*] Enter your targets (split by space): ').split()
        option = opt_input()
        if option == 1:
                for target in targets:
                        scan_spe(target)
        else:
                for target in targets:
                        scan_series(target)
        deci = cont_quit()
        if deci == 'n':
                break
