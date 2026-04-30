# Crypto Data Pipeline

A end-to-end ELT pipeline that pulls live cryptocurrency prices and stores them in a cloud data warehouse for analysis.

## Stack
- **Python** — data extraction from CoinGecko API and visualization
- **Snowflake** — cloud data warehouse
- **dbt** — SQL transformations
- **matplotlib** — dashboard visualization

## Pipeline Overview
1. `extract.py` pulls live prices for Bitcoin, Ethereum, Solana, and XRP from the CoinGecko API
2. Raw data is loaded into Snowflake (`crypto.raw.prices`)
3. dbt transforms the raw data into a clean model (`crypto.transforms.prices_clean`)
4. `visualize.py` generates a dashboard showing current prices and 24hr change

## How to Run
1. Add your Snowflake credentials to a `.env` file
2. Run `python extract.py` to pull and load fresh data
3. Run dbt to transform: `dbt run --project-dir crypto_dbt`
4. Run `python visualize.py` to generate the dashboard