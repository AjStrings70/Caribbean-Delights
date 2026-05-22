#!/usr/bin/env python3
"""
Restaurant data for Caribbean Delights application.

Contains cuisine types and raw restaurant data with the following structure:
[cuisine_type, restaurant_name, rating_1, rating_2, address, country]
"""

CUISINE_TYPES = [
    'jamaican', 'dominican', 'haitian', 'cuban', 'puerto_rican', 
    'trinidadian', 'barbadian', 'bahamian', 'belizean', 'grenadian',
    'caymanian', 'st_lucia', 'virgin_islands', 'seafood', 'vegetarian',
    'fusion', 'cafe', 'bakery'
]

RESTAURANT_DATA = [
    ['jamaican', "Irie Vibes Jamaica Kitchen", '4', '5', '123 Reggae Ave.', 'Jamaica'],
    ['jamaican', 'Jerk Palace', '5', '4', '456 Island St.', 'Jamaica'],
    ['jamaican', "Nanny's Kitchen", '3', '4', '789 Bob Marley Blvd.', 'Jamaica'],
    ['jamaican', 'Yellow Bird Cafe', '4', '3', '321 Kingston Way', 'Jamaica'],
    ['jamaican', 'Rastafarian Feast', '4', '5', '654 Peace Lane', 'Jamaica'],
    ['dominican', 'Merengue Dreams', '4', '4', '111 Samaná Rd.', 'Dominican Republic'],
    ['dominican', 'Casa del Mangú', '5', '4', '222 Santo Domingo St.', 'Dominican Republic'],
    ['dominican', 'Los Tres Golpes', '3', '5', '333 Punta Cana Dr.', 'Dominican Republic'],
    ['dominican', 'Mofongo Magic', '4', '3', '444 Cabarete Way', 'Dominican Republic'],
    ['haitian', 'Port-au-Prince Kitchen', '4', '4', '555 Haitian Blvd.', 'Haiti'],
    ['haitian', 'Diri ak Djon-Djon', '5', '3', '666 Hispaniola St.', 'Haiti'],
    ['haitian', 'Ti Legume Caribbean Bistro', '4', '5', '777 Cap-Haïtien Ln.', 'Haiti'],
    ['cuban', 'Havana Nights', '5', '5', '888 Mojito Ave.', 'Cuba'],
    ['cuban', 'El Malecón', '4', '4', '999 Cienfuegos Rd.', 'Cuba'],
    ['cuban', 'Ropa Vieja House', '4', '5', '101 Varadero Way', 'Cuba'],
    ['puerto_rican', 'Sofrito Soul', '5', '4', '202 San Juan St.', 'Puerto Rico'],
    ['puerto_rican', 'Tostones Express', '4', '3', '303 Salsa Lane', 'Puerto Rico'],
    ['puerto_rican', 'Alcapurrias Deluxe', '4', '4', '404 Ponce Blvd.', 'Puerto Rico'],
    ['trinidadian', 'Carnival Eats', '4', '5', '505 Trinidad Ave.', 'Trinidad and Tobago'],
    ['trinidadian', 'Doubles Stop', '3', '4', '606 Tacos Rd.', 'Trinidad and Tobago'],
    ['trinidadian', 'Chutney Kitchen', '4', '4', '707 Port of Spain St.', 'Trinidad and Tobago'],
    ['barbadian', 'Bridgetown Kitchen', '4', '3', '808 Cuttlefish Ln.', 'Barbados'],
    ['barbadian', 'Flying Fish Tavern', '5', '5', '909 Carlisle Bay Blvd.', 'Barbados'],
    ['bahamian', 'Conch Paradise', '4', '5', '1010 Nassau Ave.', 'Bahamas'],
    ['bahamian', 'Island Hopper Kitchen', '5', '4', '1111 Freeport Rd.', 'Bahamas'],
    ['belizean', 'Garifuna Taste', '4', '4', '1212 Belmopan St.', 'Belize'],
    ['belizean', 'Rice and Beans House', '4', '3', '1313 Ambergris Way', 'Belize'],
    ['grenadian', 'Nutmeg Island Bistro', '4', '4', '1414 St Georges Lane', 'Grenada'],
    ['caymanian', 'Turtle Reef Restaurant', '5', '5', '1515 Grand Cayman Ave.', 'Cayman Islands'],
    ['st_lucia', 'Pitons Kitchen', '4', '5', '1616 Castries Rd.', 'St.Lucia'],
    ['virgin_islands', 'Sandy Bottom Cafe', '4', '4', '1717 Charlotte Amalie Blvd.', 'U.S. Virgin Islands'],
    ['seafood', 'Island Catch', '5', '5', '1818 Marlin Dr.', 'Bahamas'],
    ['seafood', 'Coral Reef Grill', '4', '5', '1919 Lobster Lane', 'Barbados'],
    ['seafood', 'Ocean Treasures', '5', '4', '2020 Sunset Pier St.', 'Jamaica'],
    ['seafood', 'Groupers Delight', '4', '3', '2121 Fish Market Rd.', 'Cayman Islands'],
    ['vegetarian', 'Green Island Kitchen', '4', '4', '2222 Garden Ave.', 'St.Lucia'],
    ['vegetarian', 'Root Vegetable Delight', '4', '5', '2323 Organic Way', 'Grenada'],
    ['seafood', 'Bequia Bay Grill', '4', '4', '2828 Beachfront Drive', 'St. Vincent and the Grenadines'],
    ['fusion', 'Caribbean Fusion Bistro', '5', '4', '2424 Creative Blvd.', 'Trinidad and Tobago'],
    ['fusion', 'Island Modern Kitchen', '4', '5', '2525 Innovation St.', 'Puerto Rico'],
    ['cafe', 'Tropical Brew Cafe', '4', '4', '2626 Coffee Lane', 'Jamaica'],
    ['bakery', 'Island Sunrise Bakery', '5', '3', '2727 Fresh Bread Way', 'Barbados']
]
