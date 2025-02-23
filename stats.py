def get_num_words(text):
	words = text.split()
	return len(words)

def get_num_chars(text):
	chars = {}
	for char in text.lower():
		if char in chars:
			chars[char] += 1
		else:
			chars[char] = 1
	return chars

def sort_chars(chars):
	chars_list = chars.items()
	sorted_chars = {k: v for k, v in sorted(chars_list, key=lambda item: item[1], reverse=True)}
	return sorted_chars