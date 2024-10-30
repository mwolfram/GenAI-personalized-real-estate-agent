#!/usr/bin/env python
# coding: utf-8

from toolkit import single_query_llm

'''
Generates 10 random, imaginary real estate listings that look similar to the one provided.
'''
def initial_generation():
    initial_generation_prompt = """
    Generate 10 random, imaginary real estate listings that look similar to this:

    ===START SAMPLE LISTING===
    Neighborhood: Green Oaks
    Price: $800,000
    Bedrooms: 3
    Bathrooms: 2
    House Size: 2,000 sqft

    Description: Welcome to this eco-friendly oasis nestled in the heart of Green Oaks. This charming 3-bedroom, 2-bathroom home boasts energy-efficient features such as solar panels and a well-insulated structure. Natural light floods the living spaces, highlighting the beautiful hardwood floors and eco-conscious finishes. The open-concept kitchen and dining area lead to a spacious backyard with a vegetable garden, perfect for the eco-conscious family. Embrace sustainable living without compromising on style in this Green Oaks gem.

    Neighborhood Description: Green Oaks is a close-knit, environmentally-conscious community with access to organic grocery stores, community gardens, and bike paths. Take a stroll through the nearby Green Oaks Park or grab a cup of coffee at the cozy Green Bean Cafe. With easy access to public transportation and bike lanes, commuting is a breeze.
    ===END SAMPLE LISTING===

    Here are some ideas for properties that you can include in the listings:
    - Access to transportation (bus, tram, train, subway, etc.)
    - Proximity to schools, parks, shopping centers, grocery stores, restaurants, cafes, etc.
    - Proximity to highways, airports, train stations, etc.
    - Energy-efficient features (solar panels, energy-efficient appliances, etc.)
    - Eco-friendly amenities (community gardens, composting facilities, etc.)
    - Sustainable living options (bike paths, walking trails, etc.)
    - Local attractions (parks, museums, theaters, etc.)
    - Community events (farmers' markets, festivals, etc.)
    - Neighborhood characteristics (quiet, lively, family-friendly, etc.)
    - Architectural styles (modern, traditional, eco-friendly, etc.)
    - Outdoor spaces (backyard, garden, patio, etc.)
    - Interior features (hardwood floors, granite countertops, etc.)
    - Lifestyle amenities (swimming pool, fitness center, etc.)
    - Safety features (security system, gated community, etc.)
    - Accessibility features (ramps, elevators, etc.)
    - Pet-friendly features (dog park, pet spa, etc.)
    - Smart home technology (smart thermostats, lighting, etc.)
    - Historical significance (historic district, landmark, etc.)

    Feel free to augment the sample listing with ideas mentioned above to create diverse and imaginative real estate listings.

    """

    response = single_query_llm(initial_generation_prompt)

    print("\n\nThe Response is:")
    print(response)


'''
Used to individually enhance listing, one by one, with some of the ideas mentioned in the prompt.
'''
def individual_augmentation():
    individual_augmentation_prompt = """
    ===RAW LISTING===
    Neighborhood: Harbor View
    Price: $1,200,000
    Bedrooms: 4
    Bathrooms: 3.5
    House Size: 3,500 sqft

    Description: This waterfront property in Harbor View offers breathtaking views of the bay and luxurious coastal living. The 4-bedroom, 3.5-bathroom home features an open-concept floor plan, high-end finishes, and a private dock for boating enthusiasts. Relax on the expansive deck overlooking the water or entertain guests in the spacious living areas. Live the coastal lifestyle in Harbor View.

    Neighborhood Description: Harbor View is a sought-after waterfront community with marinas, yacht clubs, and waterfront restaurants. Residents can enjoy outdoor activities like sailing, fishing, and kayaking, as well as easy access to the beach and coastal trails for recreation.
    ===END RAW LISTING===

    Look at the raw listing and enhance it, at random, with some of the following features:

    - Access to transportation (bus, tram, train, subway, etc.)
    - Proximity to schools, parks, shopping centers, grocery stores, restaurants, cafes, etc.
    - Proximity to highways, airports, train stations, etc.
    - Energy-efficient features (solar panels, energy-efficient appliances, etc.)
    - Eco-friendly amenities (community gardens, composting facilities, etc.)
    - Sustainable living options (bike paths, walking trails, etc.)
    - Local attractions (parks, museums, theaters, etc.)
    - Community events (farmers' markets, festivals, etc.)
    - Neighborhood characteristics (quiet, lively, family-friendly, etc.)
    - Architectural styles (modern, traditional, eco-friendly, etc.)
    - Outdoor spaces (backyard, garden, patio, etc.)
    - Interior features (hardwood floors, granite countertops, etc.)
    - Lifestyle amenities (swimming pool, fitness center, etc.)
    - Safety features (security system, gated community, etc.)
    - Accessibility features (ramps, elevators, etc.)
    - Pet-friendly features (dog park, pet spa, etc.)
    - Smart home technology (smart thermostats, lighting, etc.)
    - Historical significance (historic district, landmark, etc.)

    Use imaginary values, properties to enhance the listing. Use no more than 30% of these properties, chosen at random, to enhance the listing.
    Be creative and make the listing more appealing and diverse.
    Change the wording to describe a specific property, don't use expressions like "such as" or "for example". Imagine that
    this is actually a property that exists and that you're trying to sell to a potential buyer.
    """

    response = single_query_llm(individual_augmentation_prompt)

    print("\n\nThe Response is:")
    print(response)

#initial_generation()
individual_augmentation()