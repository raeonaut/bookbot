from stats import get_num_chars, get_num_words, sort_chars
import sys

if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

path_to_book = sys.argv[1]

def get_book_text(path):
	with open(path) as f:
		file_contents = f.read()
		return file_contents

def main():
	file_contents = get_book_text(path_to_book)
	num_words = get_num_words(file_contents)
	num_chars = get_num_chars(file_contents)
	sorted_chars = sort_chars(num_chars)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path_to_book}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("----------- Character Count ----------")
	for char in sorted_chars:
		if char.isalpha():
			print(f"{char}: {sorted_chars[char]}")

main()
