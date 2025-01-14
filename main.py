class Movie:
    def __init__(self, title, duration, showtimes):
        self.title = title
        self.duration = duration
        self.showtimes = showtimes

    def add_showtime(self, time):
        self.showtimes.append(time)

    def remove_showtime(self, time):
        if time in self.showtimes:
            self.showtimes.remove(time)

    def wyswietl_szczegoly(self):
        print(f"Tytuł: {self.title}")
        print(f"Czas trwania: {self.duration} minut")
        print("Godziny seansów: ", ", ".join(self.showtimes))
        
        class Customer:
            def __init__(self, first_name, last_name):
                self.first_name = first_name
                self.last_name = last_name
                self.reservations = []

            def add_reservation(self, movie, time):
                if time in movie.showtimes:
                    self.reservations.append((movie.title, time))
                else:
                    print(f"Showtime {time} not available for movie {movie.title}")

            def display_reservations(self):
                print(f"Reservations for {self.first_name} {self.last_name}:")
                for reservation in self.reservations:
                    print(f"Movie: {reservation[0]}, Showtime: {reservation[1]}")

        class VIPCustomer(Customer):
            def get_discounted_price(self, price):
                return price * 0.8

            def book_private_show(self, movie, time):
                if time in movie.showtimes:
                    print(f"Private show booked for {self.first_name} {self.last_name} for movie {movie.title} at {time}")
                else:
                    print(f"Showtime {time} not available for movie {movie.title}")

