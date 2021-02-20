import random

_comp_score=0
_user_score=0

def jumble(user_input):
	# user_input possible values: s, p, r
	global _comp_score
	global _user_score
	options=['s','p','r']
	comp_choice=random.choice(options)

	if comp_choice == 's':
		print('\nComp > ', 'Stone')
	elif comp_choice == 'p':
		print('\nComp > ', 'Paper')
	elif comp_choice == 'r':
		print('\nComp > ', 'Scissors')
	print()

	# same
	if user_input==comp_choice:
		print('DRAW.')

	# stone and paper
	elif user_input=='s' and comp_choice=='p':
		_comp_score+=1
		print('COMPUTER WON! Better luck next time.')
		print('Score: \n\t Computer: ',_comp_score,'\n\t You: ', _user_score)
	elif user_input=='p' and comp_choice=='s':
		_user_score+=1
		print('YOU WON! Congratulations.')
		print('Score: \n\t Computer: ',_comp_score,'\n\t You: ', _user_score)

	# stone and scissors
	elif user_input=='r' and comp_choice=='s':
		_comp_score+=1
		print('COMPUTER WON! Better luck next time.')
		print('Score: \n\t Computer: ',_comp_score,'\n\t You: ', _user_score)
	elif user_input=='s' and comp_choice=='r':
		_user_score+=1
		print('YOU WON! Congratulations.')
		print('Score: \n\t Computer: ',_comp_score,'\n\t You: ', _user_score)

	# paper and scissors
	elif user_input=='p' and comp_choice=='r':
		_comp_score+=1
		print('COMPUTER WON! Better luck next time.')
		print('Score: \n\t Computer: ',_comp_score,'\n\t You: ', _user_score)
	elif user_input=='r' and comp_choice=='p':
		_user_score+=1
		print('YOU WON! Congratulations.')
		print('Score: \n\t Computer: ',_comp_score,'\n\t You: ', _user_score)





while True:
	print('______________________')
	print('e - Exit OR x - Score.\n')
	print('s - Stone\np - Paper\nr - Scissors')
	user_input=input('\n> ')

	if user_input == 'e':
		break
	elif user_input=='x':
		print('Score: \n\t Computer: ',_comp_score,'\n\t You: ', _user_score)

	elif user_input == 's':
		print('\nYou > ', 'Stone')
		jumble(user_input)
	elif user_input == 'p':
		print('\nYou > ', 'Paper')
		jumble(user_input)
	elif user_input == 'r':
		print('\nYou > ', 'Scissors')
		jumble(user_input)
	else:
		print('\nSorry, wrong input!!!')