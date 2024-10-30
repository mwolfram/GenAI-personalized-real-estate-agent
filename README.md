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

## Get latest sqlite3 for Chroma

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

To run the application, execute `HomeMatch.py`

A sample run is shown here:

TODO

## Step-by-step breakdown

-- most important: query_real_estate_agent


