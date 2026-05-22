#!/usr/bin/env python3
"""
Main application for Caribbean Delights.

Demonstrates the use of RestaurantIndex for efficient restaurant searching
and filtering using hash map-based indexing.
"""

from typing import List, Dict
from restaurant_index import RestaurantIndex
from data import RESTAURANT_DATA, CUISINE_TYPES


def convert_raw_data(raw_data: List[List]) -> List[Dict]:
    """
    Convert raw restaurant data (list format) to dictionary format.
    
    Args:
        raw_data: List of restaurant records in format 
                 [cuisine, name, rating_1, rating_2, address, country]
    
    Returns:
        List of restaurant dictionaries with properly formatted fields
    """
    restaurants = []
    for record in raw_data:
        restaurant = {
            'cuisine': record[0],
            'name': record[1],
            'rating_1': int(record[2]),
            'rating_2': int(record[3]),
            'address': record[4],
            'country': record[5]
        }
        restaurants.append(restaurant)
    return restaurants


def display_restaurants(restaurants: List[Dict], title: str = "") -> None:
    """
    Display a list of restaurants in a formatted manner.
    
    Args:
        restaurants: List of restaurant dictionaries to display
        title: Optional title for the display
    """
    if title:
        print(f"\n{title}")
        print("=" * 80)
    
    if not restaurants:
        print("No restaurants found.")
        return
    
    for restaurant in restaurants:
        print(f"  {restaurant['name']}")
        print(f"    Cuisine: {restaurant['cuisine'].title()}")
        print(f"    Country: {restaurant['country']}")
        print(f"    Address: {restaurant['address']}")
        print(f"    Ratings: {restaurant['rating_1']}/5, {restaurant['rating_2']}/5")
        print()


def display_menu() -> None:
    """Display the main menu options."""
    print("\n" + "=" * 80)
    print("CARIBBEAN DELIGHTS - MAIN MENU")
    print("=" * 80)
    print("1. Search restaurants by cuisine")
    print("2. Search restaurants by country")
    print("3. View all available cuisines")
    print("4. View all available countries")
    print("5. View all restaurants")
    print("6. Exit")
    print("=" * 80)


def search_by_cuisine(index: RestaurantIndex) -> None:
    """Allow user to search restaurants by cuisine type."""
    cuisines = index.get_all_cuisines()
    print("\nAvailable cuisines:")
    for i, cuisine in enumerate(cuisines, 1):
        print(f"  {i}. {cuisine}")
    
    try:
        choice = input("\nEnter the number or name of the cuisine (or 'back' to return): ").strip()
        
        if choice.lower() == 'back':
            return
        
        # Try to get cuisine by number
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(cuisines):
                selected_cuisine = cuisines[idx]
            else:
                print("Invalid selection.")
                return
        except ValueError:
            # Treat input as cuisine name
            selected_cuisine = choice
        
        restaurants = index.get_by_cuisine(selected_cuisine)
        display_restaurants(restaurants, f"Restaurants serving {selected_cuisine} cuisine")
        
        if not restaurants:
            print(f"No restaurants found for '{selected_cuisine}'.")
    
    except Exception as e:
        print(f"Error during search: {e}")


def search_by_country(index: RestaurantIndex) -> None:
    """Allow user to search restaurants by country."""
    countries = index.get_all_countries()
    print("\nAvailable countries:")
    for i, country in enumerate(countries, 1):
        print(f"  {i}. {country}")
    
    try:
        choice = input("\nEnter the number or name of the country (or 'back' to return): ").strip()
        
        if choice.lower() == 'back':
            return
        
        # Try to get country by number
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(countries):
                selected_country = countries[idx]
            else:
                print("Invalid selection.")
                return
        except ValueError:
            # Treat input as country name
            selected_country = choice
        
        restaurants = index.get_by_country(selected_country)
        display_restaurants(restaurants, f"Restaurants in {selected_country}")
        
        if not restaurants:
            print(f"No restaurants found in '{selected_country}'.")
    
    except Exception as e:
        print(f"Error during search: {e}")


def main() -> None:
    """Main application entry point with interactive menu."""
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + "WELCOME TO CARIBBEAN DELIGHTS".center(78) + "║")
    print("║" + "The Best Online Shopping for local Caribbean Cuisine".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "=" * 78 + "╝")
    
    # Convert raw data to proper format
    restaurants = convert_raw_data(RESTAURANT_DATA)
    
    # Create index
    try:
        index = RestaurantIndex(restaurants)
    except ValueError as e:
        print(f"Error creating index: {e}")
        return
    
    # Interactive menu loop
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            search_by_cuisine(index)
        elif choice == '2':
            search_by_country(index)
        elif choice == '3':
            cuisines = index.get_all_cuisines()
            print(f"\nAvailable cuisines ({len(cuisines)}):")
            for cuisine in cuisines:
                count = len(index.get_by_cuisine(cuisine))
                print(f"  • {cuisine} ({count} restaurants)")
        elif choice == '4':
            countries = index.get_all_countries()
            print(f"\nAvailable countries ({len(countries)}):")
            for country in countries:
                count = len(index.get_by_country(country))
                print(f"  • {country} ({count} restaurants)")
        elif choice == '5':
            display_restaurants(
                index.all_restaurants,
                f"All {len(index.all_restaurants)} Restaurants"
            )
        elif choice == '6':
            print("\nThank you for using Caribbean Delights! Enjoy your meal! 🍴🏝️\n")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == '__main__':
    main()
