import random

def vernam_cypher(text, key):
	cyphered_text = []
	for x, y in zip(text, key):
		num = ord(x)^ord(y)
		cyphered_text.append(chr(num))

	return ''.join(cyphered_text)


def ceaser_cypher(text, num):
	cyphered_text = []

	for i in range(len(text)):
		item = ord(text[i])
		item += num
		if item > 122:
			item = 97 + (item - 122)

		cyphered_text.append(chr(item))		

	return ''.join(cyphered_text)


def get_parameters():

	print("Please enter a text to cypher: ", end='')

	while True:
		try:
			text = input().split(' ')
			for item in text:
				if not item.isalpha():
					raise Exception
					break
			else:
				break

		except Exception:
			print("Wrong format")
			print("Please enter a text to cypher: ", end='')

	return text

if __name__ == "__main__":

	text = get_parameters()
	key_text = []
	cyphered_text = []

	for i in range(len(text)):
		num = random.randint(1,25)
		key = ceaser_cypher(text[i].lower(), num)
		key_text.append(key)

	print(' '.join(key_text))

	for x, y in zip(text, key_text):
		cyphered_text.append(vernam_cypher(x, y))
	
	print("Cyphered text:", " ".join(cyphered_text))
