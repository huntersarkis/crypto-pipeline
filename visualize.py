import snowflake.connector
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

load_dotenv()

conn = snowflake.connector.connect(
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema="transforms"
)

df = pd.read_sql("SELECT * FROM crypto.transforms.prices_clean", conn)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Price bar chart
axes[0].bar(df["COIN"], df["PRICE_USD"], color=["orange", "blue", "green", "purple"])
axes[0].set_title("Crypto Prices (USD)")
axes[0].set_ylabel("Price (USD)")

# 24hr change bar chart
colors = ["green" if x > 0 else "red" for x in df["CHANGE_24H_PCT"]]
axes[1].bar(df["COIN"], df["CHANGE_24H_PCT"], color=colors)
axes[1].set_title("24hr Change (%)")
axes[1].set_ylabel("Change (%)")
axes[1].axhline(y=0, color="black", linewidth=0.8)

plt.tight_layout()
plt.savefig("crypto_chart.png")
plt.show()
print("Chart saved!")