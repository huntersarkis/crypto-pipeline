import requests
import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to Snowflake
conn = snowflake.connector.connect(
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
)

# Pull crypto prices from CoinGecko
url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "bitcoin,ethereum,solana,ripple",
    "vs_currencies": "usd",
    "include_24hr_change": "true"
}

response = requests.get(url, params=params)
data = response.json()

# Load into Snowflake
cursor = conn.cursor()
for coin, values in data.items():
    cursor.execute(
        "INSERT INTO raw.prices (coin, price_usd, change_24h) VALUES (%s, %s, %s)",
        (coin, values["usd"], values["usd_24h_change"])
    )

print("Data loaded successfully!")
conn.close()