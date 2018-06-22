# used for correcting the data 
import re
from tokenizer import print_list

corrected = './tok_corrected.txt'
uncorrected = './TECCL_tokenized.txt'

# if it ends in a comma or doesn't have a period in it, it's not a sentence, this is for everything
def remove_salutations(file):
	""" Removes salutations and returns as a list """
	with open(file) as f:
		g = f.read()
	g = g.split('\n')
	new = []
	dum = 1
	for index, line in enumerate(g):
		# if starts with nubmer + punct, get rid of that 
		if re.search(r'^[0-9]+[.,:]*',line) != None:
			g[index]=re.sub(r'^[0-9]+[.,:]*','',line)
	for index,line in enumerate(g):
		if '.' not in line or len(line)<3 or line[-1] not in ['.','!','?']:
			#print('got here')
			# it's a salutation and should be removed
			dum = 0
		else:
			new.append(line)
	return (new)

""" These are just for the corrected version """

def remove_sals_from_list (g):
	new = []
	dum = 1
	for index, line in enumerate(g):
		# if starts with nubmer + punct, get rid of that 
		if re.search(r'^[0-9]+[.,:]*',line) != None:
			g[index]=re.sub(r'^[0-9]+[.,:]*','',line)
	for index,line in enumerate(g):
		if '.' not in line or len(line)<3 or line[-1] not in ['.','!','?']:
			#print('got here')
			# it's a salutation and should be removed
			dum = 0
		else:
			new.append(line)
	return (new)

def fix_punctuation(list_of_lines):
	new_list = []
	new_lines = ''
	for index, line in enumerate(list_of_lines):
		# if it's of the form word.word, make it word.\nword, but not .com or .cn
		new_line  = line
		new_line = re.sub(r'(?<!(www))\.(?![\s(com)(cn)0-9])','.\n',new_line)

		# if it's of the form word,word or word ,word, make it word, word
		new_line = re.sub(r',(?![\s0-9])',', ',new_line)

		# if it's of the form word;word  make it word; word
		new_line = re.sub(r';(?!\s)','; ',new_line)

		# if word"word -> word " word
		new_line = re.sub(r'(?<!\s)"(?!\s)',' " ',new_line)

		# word!word
		new_line = re.sub(r'!(?!\s)','!\n',new_line)

		# word?word
		new_line = re.sub(r'\?(?!\s)','?\n',new_line)
		# if word :word, word: word

		# if word:word, word: word
		new_line = re.sub(r':(?![\s0-9])',': ',new_line)

		# if the last char isn't newline, make it so
		if len(new_line)>1 and new_line[-1]!='\n':
			new_line +='\n'
		if not len(new_line)<=2:	
			new_lines += new_line
		
		

	new_list = new_lines.split('\n')		

	return (new_list)

def read_a_list (file):
	with open(file) as f:
		g = f.read()
	return(g.split('\n'))

print_list(remove_salutations(uncorrected),'./tokenized_uncorrected.txt')


print_list(remove_sals_from_list(fix_punctuation(read_a_list(corrected))),'./tokenized_corrected.txt')