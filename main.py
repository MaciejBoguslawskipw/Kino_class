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
                self.rezerwacje = []

            def add_reservation(self, movie, time):
                if time in movie.showtimes:
                    self.rezerwacje.append((movie.title, time))
                else:
                    print(f"Seans o godzinie {time} nie jest dostępny dla filmu {movie.title}")

            def display_reservations(self):
                print(f"Rezerwacje dla {self.first_name} {self.last_name}:")
                for rezerwacja in self.rezerwacje:
                    print(f"Film: {rezerwacja[0]}, Godzina seansu: {rezerwacja[1]}")

        class VIPCustomer(Customer):
            def get_discounted_price(self, price):
                return price * 0.8

            def book_private_show(self, movie, time):
                if time in movie.showtimes:
                    print(f"Prywatny seans zarezerwowany dla {self.first_name} {self.last_name} na film {movie.title} o godzinie {time}")
                else:
                    print(f"Seans o godzinie {time} nie jest dostępny dla filmu {movie.title}")

        class Cinema:
            def __init__(self):
                self.movies = []
                self.customers = []

            def add_movie(self, movie):
                self.movies.append(movie)

            def add_customer(self, customer):
                self.customers.append(customer)

            def display_movies(self):
                print("Filmy w kinie:")
                for movie in self.movies:
                    movie.wyswietl_szczegoly()

        def main():
            # Create movies
            movie1 = Movie("Incepcja", 148, ["14:00", "18:00", "21:00"])
            movie2 = Movie("Interstellar", 169, ["12:00", "16:00", "20:00"])

            # Create customers
            customer1 = Customer("Jan", "Kowalski")
            vip_customer = VIPCustomer("Anna", "Nowak")

            # Create cinema
            cinema = Cinema()
            cinema.add_movie(movie1)
            cinema.add_movie(movie2)
            cinema.add_customer(customer1)
            cinema.add_customer(vip_customer)

            # Display movies
            cinema.display_movies()

            # Add reservations
            customer1.add_reservation(movie1, "14:00")
            vip_customer.add_reservation(movie2, "20:00")

            # Display reservations
            customer1.display_reservations()
            vip_customer.display_reservations()

            # VIP customer books a private show
            vip_customer.book_private_show(movie1, "18:00")

        if __name__ == "__main__":
            main()