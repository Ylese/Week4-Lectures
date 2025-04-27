def movie_ticket_booking():
#list of available movies and their prices
    movies = ["Inception", "The Matrix", "Interstellar"]
    movie_prices = {"Inception": 10, "The Matrix": 12, "Interstellar": 15}

    while True:
        try: 
            tickets = int(input("How many tickets would you like to book?"))
            if tickets <= 0:
                print("You must at least book one ticket.")
                continue
            print("AVAILABLE MOVIES")
            for i, movie in enumerate(movies, 1):
                print(f"{i}. {movie}")

            movie_choice = int(input("Please select a movie by number: "))
            if movie_choice < 1 or movie_choice > len(movies):
                print("Invalid choice. Please select a valid movie number.")
                continue
            selected_movie = movies[movie_choice - 1]
            total_price = movie_prices[selected_movie] * tickets
            print(f"\nBooking Summary: {tickets} tickets for '{selected_movie}' at ${movie_prices[selected_movie]} each.")
            print(f"Total cost: ${total_price}")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")


movie_ticket_booking()
