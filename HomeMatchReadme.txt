# GenAI-personalized-real-estate-agent

## Repository Requirements

* langchain=0.0.305
* openai=0.28.1
* pydantic>=1.10.12
* pytest>=7.4.0
* sentence-transformers>=2.2.0
* transformers>=4.31.0
* chromadb==0.4.12
* jupyter==1.0.0
* tiktoken==0.8.0

### Get latest sqlite3 for Chroma

Sqlite3 is required to run Chroma. If your sqlite3 version is not sufficient, you can build your own sqlite3 with the following commands:

```
wget https://www.sqlite.org/2023/sqlite-autoconf-3410000.tar.gz
tar xvfz sqlite-autoconf-3410000.tar.gz
cd sqlite-autoconf-3410000
./configure
make
sudo make install
sqlite3 --version
export PATH=/usr/local/bin:$PATH
echo 'export PATH=/usr/local/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
```

## How to run

To run the application, first change the Q&A in `HomeMatch.py` to your liking, then execute `HomeMatch.py`

A sample run is shown here (based on the current Q&A defined in the code):

First, the LLM summarizes the user's Q&A:

The user is looking for a house that is at least 2,200 sqft in size. Their top priorities in choosing a property are access to a pool, top-rated schools, and grocery stores. They require a home office and value transportation options such as access to buses, highways, or airports. When it comes to entertainment options, they are content with a friendly and safe community.

Second, after consulting the Vector database and coming up with plausible options, the LLM summarizes the best matches:

1. Listing 2 in Sunset Heights:
- Price: $900,000
- Bedrooms: 5
- Bathrooms: 4
- House Size: 3,000 sqft
- Description: This luxurious 5-bedroom, 4-bathroom home in Sunset Heights features a state-of-the-art kitchen and a tranquil backyard oasis with a shimmering pool and rejuvenating spa. The impeccable finishes make this home a haven for those with discerning taste. Additionally, Sunset Heights offers easy access to public transportation, top-rated schools, lush parks, upscale shopping centers, and trendy cafes. You can enjoy community events and explore local attractions in this vibrant neighborhood.

2. Listing 8 in Pinecrest Heights:
- Price: $750,000
- Bedrooms: 4
- Bathrooms: 3.5
- House Size: 2,800 sqft
- Description: Step into this modern 4-bedroom, 3.5-bathroom home in Pinecrest Heights, featuring a sleek kitchen with quartz countertops and a large island. The spacious master suite boasts a spa-like bathroom with a soaking tub and dual vanities. With a fenced backyard and a covered patio, this home is perfect for entertaining. Pinecrest Heights offers easy access to public transportation, schools, parks, shopping centers, and restaurants, making it ideal for a convenient lifestyle.

3. Listing 9 in Maple Grove:
- Price: $600,000
- Bedrooms: 3
- Bathrooms: 2
- House Size: 2,100 sqft
- Description: Welcome to this charming 3-bedroom, 2-bathroom home in Maple Grove, featuring an updated kitchen with luxurious granite countertops and high-end stainless steel appliances. Cozy up by the fireplace in the spacious living room with elegant hardwood floors. The fenced backyard with a deck is perfect for hosting outdoor gatherings. Maple Grove offers a tranquil escape with easy access to public transportation, top-rated schools, lush parks, trendy cafes, and boutique shopping centers.

I hope these listings align with your preferences and help you find your dream home! Let me know if you would like more information on any of these properties.

## Rubric

### Synthetic Data Generation

Demonstrated in `generate_real_estate_listings.py`. The data generation took place in two distinct steps. The first one took the sample listing and created 10 random samples that looked similar. The LLM was already fed with some ideas to enhance the listing. In a second step, the listings were postprocessed one by one to individually augment them and make it clear to the LLM that features need to be added at random. The resulting listings can be found in `Listings.txt`.

### Semantic Search

The vector database is created in `vectordb.py`. It is populated with listings from `Listings.txt`. I used a Chroma database. Make sure that you have the appropriate `sqlite3` version available. If necessary, this can be built from source, as described above.

Semantic search is demonstrated in `toolkit.py::query_real_estate_agent`. First the user-provided Q&A is converted to a comprehensive description of user preferences, using the LLM. Then this string is passed to the semantic search function of the Chroma database to come up with matching listings.

### Augmented Response Generation

Matching listing descriptions are first searched in `toolkit.py::query_real_estate_agent`. The prompt template that is generated in `prompt_template.py::get_prompt_template` then instructs the LLM to take care of augmenting the listings. 
