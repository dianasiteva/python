books_number = 0
search_book_name = input()
current_book_name = ''

current_book_name = input()
while current_book_name != 'No More Books':
    books_number += 1
    if current_book_name == search_book_name:
        print(f'You checked {books_number - 1} books and found it.')
        break
    current_book_name = input()
else:
    print(f'The book you search is not here!')
    print(f'You checked {books_number} books.')
