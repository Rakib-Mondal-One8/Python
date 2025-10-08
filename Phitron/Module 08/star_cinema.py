class Star_Cinema:
    hall_list = []

    def entry_hall(self,Hall):
        self.hall_list.append(Hall)

class Hall:

    def __init__(self,rows,cols,hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_show(self,id,movie_name,time):
        show = (id,movie_name,time)
        self.show_list.append(show)

    def view_show_list(self):
        for show in self.show_list:
            print(show)

    def view_available_seats(self):
        for show in self.show_list:
            print(show)
            for r in self.seats[show[0]]:
                for c in r:
                    if(c == True):print('✓',end=' ')
                    else: print('X',end='')
                print()

    def sell_ticket(self):
        for show in self.show_list:
            empty_seats = []
            for r in range(self.rows):
                row = []
                for c in range(self.cols):
                    row.append(True)
                empty_seats.append(row)
            self.seats[show[0]] = empty_seats

    def book_seats(self,id,seats_to_book): #id , list of tuples (row,col)
        if id not in self.seats:
            print('This Show is not currently Available!')
        else:
            for s in seats_to_book:
                if(self.seats[id][s[0]][s[1]] == False):
                    print(f"Sorry Seat no. {s} is already booked!")
                else:
                    self.seats[id][s[0]][s[1]] = False
                    print(f"Congratulations! Seat no. {s} is booked for you")





h1 = Hall(3,3,1)
h2 = Hall(3,3,2)
h3 = Hall(3,3,3)
star_cinema = Star_Cinema()
star_cinema.entry_hall(h1)
star_cinema.entry_hall(h2)
star_cinema.entry_hall(h3)

h1.entry_show(1,'Demon Slayer: Infinity Castle','10:00')
h1.entry_show(2,'Demon Slayer: Infinity Castle','01:30')
h1.entry_show(3,'Demon Slayer: Infinity Castle','06:30')
h1.sell_ticket()

h2.entry_show(1,'Iron Man','11:00')
h2.sell_ticket()

h3.entry_show(1,'Captain America: The Winter Soldier','12:00')
h3.sell_ticket()

print(f"Shows that are running:")
for hall in star_cinema.hall_list:
    hall.view_show_list()
    print('Available Tickets ---------------------')
    hall.view_available_seats()
