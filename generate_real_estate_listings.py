#!/usr/bin/env python
# coding: utf-8

from toolkit import single_query_llm

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


def individual_augmentation():
    individual_augmentation_prompt = """
    ===RAW LISTING===
    Neighborhood: Riverfront District
    Price: $1,200,000
    Bedrooms: 4
    Bathrooms: 3.5
    House Size: 3,500 sqft

    Description: Live in luxury in this 4-bedroom, 3.5-bathroom home located in the coveted Riverfront District. This property features a chef's kitchen with high-end appliances, a spacious master suite with a private balcony overlooking the river, and a backyard with a fire pit and outdoor kitchen. With stunning views and access to the nearby riverfront trail, this home is perfect for outdoor enthusiasts.

    Neighborhood Description: The Riverfront District is known for its waterfront properties, upscale dining options, and vibrant arts scene. Residents can enjoy a morning paddle on the river or take a short walk to the Riverfront Plaza for shopping and entertainment. With easy access to public transportation and cultural attractions, this neighborhood offers the perfect blend of urban living and natural beauty.
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


individual_augmentation()