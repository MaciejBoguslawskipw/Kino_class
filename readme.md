# Dokumentacja do kodu

## Spis treści
- [Klasa Movie](#klasa-movie)
  - [Opis](#opis)
  - [Metody](#metody)
- [Klasa Customer](#klasa-customer)
  - [Opis](#opis-1)
  - [Metody](#metody-1)
- [Klasa VIPCustomer](#klasa-vipcustomer)
  - [Opis](#opis-2)
  - [Metody](#metody-2)
- [Klasa Cinema](#klasa-cinema)
  - [Opis](#opis-3)
  - [Metody](#metody-3)
- [Funkcja main](#funkcja-main)

## Klasa Movie

### Opis
Klasa `Movie` reprezentuje film, który jest wyświetlany w kinie. Zawiera informacje o tytule filmu, czasie trwania oraz dostępnych godzinach seansów.

### Metody

- `__init__(self, title, duration, showtimes)`  
  Inicjalizuje obiekt filmu, przypisując tytuł, czas trwania oraz listę godzin seansów.

- `add_showtime(self, time)`  
  Dodaje nową godzinę seansu do listy godzin dostępnych dla filmu.

- `remove_showtime(self, time)`  
  Usuwa godzinę seansu z listy godzin dostępnych dla filmu, jeśli ta godzina znajduje się na liście.

- `wyswietl_szczegoly(self)`  
  Wyświetla szczegóły filmu, w tym tytuł, czas trwania oraz dostępne godziny seansów.

## Klasa Customer

### Opis
Klasa `Customer` reprezentuje klienta kina. Klient ma imię, nazwisko oraz listę rezerwacji na filmy. Może dokonywać rezerwacji oraz przeglądać swoje rezerwacje.

### Metody

- `__init__(self, first_name, last_name)`  
  Inicjalizuje obiekt klienta, przypisując imię i nazwisko oraz tworzy pustą listę rezerwacji.

- `add_reservation(self, movie, time)`  
  Dodaje rezerwację dla klienta na dany film o określonej godzinie, jeśli ta godzina jest dostępna w repertuarze filmu.

- `display_reservations(self)`  
  Wyświetla wszystkie rezerwacje klienta, w tym tytuł filmu i godzinę seansu.

## Klasa VIPCustomer

### Opis
Klasa `VIPCustomer` dziedziczy po klasie `Customer` i reprezentuje klienta VIP, który ma dodatkowe przywileje, takie jak zniżki na bilety i możliwość rezerwacji prywatnych seansów.

### Metody

- `get_discounted_price(self, price)`  
  Oblicza cenę biletu z 20% zniżką, zwracając zniżoną cenę na podstawie pierwotnej ceny.

- `book_private_show(self, movie, time)`  
  Rezerwuje prywatny seans dla klienta VIP na dany film i godzinę, jeśli ta godzina jest dostępna w repertuarze filmu.

## Klasa Cinema

### Opis
Klasa `Cinema` reprezentuje kino, które przechowuje listę filmów oraz klientów. Umożliwia dodawanie nowych filmów, klientów oraz wyświetlanie dostępnych filmów.

### Metody

- `__init__(self)`  
  Inicjalizuje obiekt kina, tworząc pustą listę filmów i klientów.

- `add_movie(self, movie)`  
  Dodaje film do repertuaru kina.

- `add_customer(self, customer)`  
  Dodaje klienta do listy klientów kina.

- `display_movies(self)`  
  Wyświetla szczegóły wszystkich filmów w repertuarze kina, korzystając z metody `wyswietl_szczegoly()` klasy `Movie`.

## Funkcja main

Funkcja `main` jest główną częścią programu, która tworzy obiekty filmów, klientów oraz kina. Umożliwia również testowanie rezerwacji i wyświetlania szczegółów filmów oraz rezerwacji klientów.

### Przebieg działania:

1. Tworzenie obiektów filmów (`movie1` i `movie2`).
2. Tworzenie obiektów klientów (`customer1` i `vip_customer`).
3. Tworzenie obiektu kina (`cinema`).
4. Dodanie filmów i klientów do kina.
5. Wyświetlenie dostępnych filmów w kinie.
6. Rezerwacja biletów przez klientów.
7. Wyświetlenie szczegółów rezerwacji.
8. Rezerwacja prywatnego seansu przez klienta VIP.

```python
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
    print("Dostępne filmy w repertuarze kina:")
    cinema.display_movies()

    # Add reservations
    print("\nRezerwacja biletu przez klienta:")
    customer1.add_reservation(movie1, "14:00")
    vip_customer.add_reservation(movie2, "20:00")

    # Display reservations
    print("\nSzczegóły rezerwacji klientów:")
    customer1.display_reservations()
    vip_customer.display_reservations()

    # VIP customer books a private show
    print("\nRezerwacja prywatnego seansu przez klienta VIP:")
    vip_customer.book_private_show(movie1, "18:00")
```

## Przykładowe wyniki:

```
Dostępne filmy w repertuarze kina:
Tytuł: Incepcja
Czas trwania: 148 minut
Godziny seansów:  14:00, 18:00, 21:00
Tytuł: Interstellar
Czas trwania: 169 minut
Godziny seansów:  12:00, 16:00, 20:00

Rezerwacja biletu przez klienta:
Rezerwacja dla Jana Kowalskiego na film Incepcja o godzinie 14:00.
Rezerwacja dla Anny Nowak na film Interstellar o godzinie 20:00.

Szczegóły rezerwacji klientów:
Rezerwacje dla Jan Kowalski:
Film: Incepcja, Godzina seansu: 14:00
Rezerwacje dla Anna Nowak:
Film: Interstellar, Godzina seansu: 20:00

Rezerwacja prywatnego seansu przez klienta VIP:
Prywatny seans zarezerwowany dla Anna Nowak na film Incepcja o godzinie 18:00
```