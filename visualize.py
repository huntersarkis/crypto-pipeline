import snowflake.connector
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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

colors = {"BITCOIN": "#F7931A", "ETHEREUM": "#627EEA", "RIPPLE": "#00AAE4", "SOLANA": "#9945FF"}

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
fig.patch.set_facecolor("#1e1e1e")

for i, (_, row) in enumerate(df.iterrows()):
    ax = axes[i]
    coin = row["COIN"]
    change = row["CHANGE_24H_PCT"]
    color = colors.get(coin, "gray")
    change_color = "#00ff88" if change >= 0 else "#ff4444"

    ax.set_facecolor("#2a2a2a")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.5, 0.75, coin, ha="center", va="center",
            fontsize=14, fontweight="bold", color=color)
    ax.text(0.5, 0.5, f"${row['PRICE_USD']:,.2f}", ha="center", va="center",
            fontsize=18, fontweight="bold", color="white")
    ax.text(0.5, 0.25, f"{change:+.2f}% {row['DIRECTION']}", ha="center", va="center",
            fontsize=12, color=change_color)

plt.suptitle("Crypto Portfolio Dashboard", fontsize=16,
             fontweight="bold", color="white", y=1.02)
plt.tight_layout()
plt.savefig("crypto_chart.png", bbox_inches="tight", facecolor="#1e1e1e")
plt.show()
print("Chart saved!")