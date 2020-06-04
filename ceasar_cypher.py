def ceaser_cypher(text, num):
	num = num % 26
	cyphered_text = []

	for i in range(len(text)):
		item = ord(text[i])
		item += num
		if item > 122:
			item = 97 + (item - 122)

		cyphered_text.append(chr(item))		

	return ''.join(cyphered_text)


def get_parameters():

	print("Please enter cypher number: ", end='')

	while True:
		try:
			num = input()
			if  num.isdigit():
				num = int(num)
			else: 
				raise Exception

			if num > 0:
				break 
		except:
			print("Wrong format")
			print("Please enter cypher number: ", end='')

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

	return text, num

text, num = get_parameters()

for i in range(len(text)):
	text[i] = ceaser_cypher(text[i].lower(), num)

text = " ".join(text)

print("Cyphered text:", text)
