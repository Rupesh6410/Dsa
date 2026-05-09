class Movie:
    def __init__(self, movie_name, total_seat, ticket_price):
        self.movie_name = movie_name
        self.total_seat = total_seat
        self.ticket_price = ticket_price
        self.booked_seats = 0

    def book_ticket(self, num_tickets):
        if self.booked_seats + num_tickets <= self.total_seat:
            self.booked_seats += num_tickets
            print("Price:", num_tickets * self.ticket_price)
        else:
            print("Not enough seats available")

    def show_status(self):
        print("Movie name:", self.movie_name)
        print("Total seats:", self.total_seat)
        print("Booked seats:", self.booked_seats)
        print("Available seats:", self.total_seat - self.booked_seats)
        print("Ticket price:", self.ticket_price)


movie1 = Movie("Movie 1", 100, 10)

movie1.book_ticket(10)

movie1.show_status()

