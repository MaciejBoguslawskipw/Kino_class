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
        


