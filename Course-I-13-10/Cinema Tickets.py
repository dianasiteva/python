film = input()
all_tickets = 0
students = 0
kids = 0
standards = 0
flag = False

while film != 'Finish':
    places = int(input())
    ticket = input()
    film_tickets = 0

    while ticket != 'End':
        if ticket == 'Finish':
            flag = True
            break

        film_tickets += 1

        if ticket == 'standard':
            standards += 1
        elif ticket == 'kid':
            kids += 1
        elif ticket == 'student':
            students += 1

        if film_tickets == places:
            break

        ticket = input()

    print(f'{film} - {(film_tickets / places * 100):.2f}% full.')
    if flag:
        break
    film = input()

all_tickets = students + kids + standards

print(f'Total tickets: {all_tickets}')
print(f'{(students / all_tickets * 100):.2f}% student tickets.')
print(f'{(standards / all_tickets * 100):.2f}% standard tickets.')
print(f'{(kids / all_tickets * 100):.2f}% kids tickets.')
