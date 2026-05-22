#!/usr/bin/env python3
"""
Caribbean Delights - Restaurant Management Application

A Python application that demonstrates efficient data management using hash maps
for fast retrieval and filtering of Caribbean restaurant information.

Key Features:
    - Hash map-based indexing for O(1) lookup performance
    - Restaurant filtering by country and cuisine type
    - Type hints for better code clarity and IDE support
    - Comprehensive error handling and validation

Author: [Ajani Hinds    ]
Version: 1.0.0
"""

from typing import Dict, List, Optional


class RestaurantIndex:
    """
    Manages restaurant data with hash map-optimized lookups.
    
    This class creates and maintains multiple hash maps (dictionaries) for
    efficient searching of restaurants by country and cuisine type, ensuring
    O(1) average-case lookup performance.
    
    Attributes:
        all_restaurants (List[Dict]): Complete list of restaurants
        by_country (Dict[str, List[Dict]]): Restaurants indexed by country
        by_cuisine (Dict[str, List[Dict]]): Restaurants indexed by cuisine
    """
    
    def __init__(self, restaurants_list: List[Dict]) -> None:
        """
        Initialize the RestaurantIndex with a list of restaurant data.
        
        Args:
            restaurants_list: List of restaurant dictionaries containing
                            restaurant information including 'country' and 'cuisine'
        
        Raises:
            ValueError: If restaurants_list is empty or None
        """
        if not restaurants_list:
            raise ValueError("Restaurant list cannot be empty")
        
        self.all_restaurants = restaurants_list
        self.by_country: Dict[str, List[Dict]] = {}
        self.by_cuisine: Dict[str, List[Dict]] = {}
        self._build_indexes()
    
    def _build_indexes(self) -> None:
        """
        Build hash maps for country and cuisine lookups.
        
        Iterates through all restaurants and creates indexed mappings
        to enable fast retrieval by country and cuisine type.
        """
        for restaurant in self.all_restaurants:
            country = restaurant.get('country', 'Unknown').title()
            cuisine = restaurant.get('cuisine', 'Unknown').title()
            
            # Index by country
            if country not in self.by_country:
                self.by_country[country] = []
            self.by_country[country].append(restaurant)
            
            # Index by cuisine
            if cuisine not in self.by_cuisine:
                self.by_cuisine[cuisine] = []
            self.by_cuisine[cuisine].append(restaurant)
    
    def get_by_country(self, country: str) -> List[Dict]:
        """
        Retrieve restaurants by country.
        
        Args:
            country: Name of the country to search for (case-insensitive)
        
        Returns:
            List of restaurant dictionaries matching the country, or empty list
        """
        return self.by_country.get(country.title(), [])
    
    def get_by_cuisine(self, cuisine: str) -> List[Dict]:
        """
        Retrieve restaurants by cuisine type.
        
        Args:
            cuisine: Type of cuisine to search for (case-insensitive)
        
        Returns:
            List of restaurant dictionaries matching the cuisine, or empty list
        """
        return self.by_cuisine.get(cuisine.title(), [])
    
    def get_all_countries(self) -> List[str]:
        """
        Get a list of all countries represented in the dataset.
        
        Returns:
            Sorted list of unique country names
        """
        return sorted(self.by_country.keys())
    
    def get_all_cuisines(self) -> List[str]:
        """
        Get a list of all cuisine types represented in the dataset.
        
        Returns:
            Sorted list of unique cuisine types
        """
        return sorted(self.by_cuisine.keys())
