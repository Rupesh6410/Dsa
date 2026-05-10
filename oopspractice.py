# class Movie:
#     def __init__(self, movie_name, total_seat, ticket_price):
#         self.movie_name = movie_name
#         self.total_seat = total_seat
#         self.ticket_price = ticket_price
#         self.booked_seats = 0

#     def book_ticket(self, num_tickets):
#         if self.booked_seats + num_tickets <= self.total_seat:
#             self.booked_seats += num_tickets
#             print("Price:", num_tickets * self.ticket_price)
#         else:
#             print("Not enough seats available")

#     def show_status(self):
#         print("Movie name:", self.movie_name)
#         print("Total seats:", self.total_seat)
#         print("Booked seats:", self.booked_seats)
#         print("Available seats:", self.total_seat - self.booked_seats)
#         print("Ticket price:", self.ticket_price)


# movie1 = Movie("Movie 1", 100, 10)

# movie1.book_ticket(10)
# movie1.book_ticket(500)

# movie1.show_status()


class Dog:
    def __init__(self , name ,breed):
        self.name = name
        self.breed = breed
        print("Dog created woff-woff")
        print(f"Name: {self.name}, Breed: {self.breed}")
    
    def bark(self):
        print("Dog is barking")

class Puppy(Dog):
    def __init__(self, name, breed , age):
        super().__init__(name, breed)
        self.age = age
        print("Puppy created")
        print(f"Name: {self.name}, Breed: {self.breed}, Age: {self.age}")
    
    def bark(self):
        print("Puppy is roaring")

puppy = Puppy("Buddy", "Labrador", 2)
puppy.bark()





