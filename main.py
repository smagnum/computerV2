import sys

elms = {'a' : 1, 'b' : 2, 'c' : 3}


# a = 'a'
# if a in elms: 
# 	print (elms['b'])


var = input('> ')

while True:
	# Shell simulation and take input
	# var = input('> ')
	# test = {'a' : 1, 'b': 2}
	# test['c'] = 3
	# if 'b' in test :
	# 	print('kakkak')

	# print ('===VAR===')
	# print (var)
	# print ('===elms===')
	# print (elms)

	
	if '=' in var :
		param = var.split('=')
		elms[param[0]] = param[1]
		print (param[1])
		
	elif param[0] in elms:
		print (elms)
		print(elms[param[0]])

	if var == 'quit' or var == 'x':
		sys.exit()
