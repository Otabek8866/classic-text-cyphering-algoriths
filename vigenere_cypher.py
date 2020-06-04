def decypher_text(string, key):
	decyphered_text = []
	key = generateKey(string, key)
	for x, y in zip(string, key):
		decyphered_text.append(chr(ord("A") + (ord(x) - ord(y) + 26) % 26))

	return ''.join(decyphered_txt)


def cypher_text(string, key):
	key = generateKey(string, key)
	cyphered_text = []
	for x, y in zip(string, key):
		cyphered_text.append(chr(ord("A") + (ord(x) + ord(y)) % 26))

	return "".join(cyphered_text)


def generateKey(string, key): 
	key = list(key)
	if len(string) == len(key):
		return key
	elif len(string) < len(key):
		return "".join(key[:len(mystring)])
	else:
		for i in range(len(string) - len(key)):
			key.append(key[i])
	
	return "".join(key)


def get_parameters():

	print("Please enter a text to cypher: ", end='')

	while True:
		try:
			text = input().split(' ')
			for item in text:
				if not item.isalpha() or not item.isascii():
					raise Exception
					break
			else:
				break

		except Exception:
			print("Wrong format")
			print("Please enter a text to cypher: ", end='')

	print("Please enter the key to cypher: ", end='')

	while True:
		try:
			key = input().strip()
			for item in key:
				if not item.isalpha() or not item.isascii() or ' ' in key:
					raise Exception
					break
			else:
				break

		except Exception:
			print("Wrong format")
			print("Please enter the key to cypher: ", end='')

	return text, key


if __name__ == "__main__":

	text, key = get_parameters()
	result_text = []
	
	for item in text:
		case_changed = []
		cases = []

		for i in item:
			if i.isupper():
				cases.append(1)
			else:
				cases.append(0)
		
		cyphered_text = cypher_text(item.upper(), key.upper())
		
		for char, case_item in zip(cyphered_text, cases):
			if case_item:
				case_changed.append(char)
			else:
				case_changed.append(char.lower())


		result_text.append("".join(case_changed))


	print(result_text)





