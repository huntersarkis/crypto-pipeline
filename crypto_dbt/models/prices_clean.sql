SELECT
    UPPER(coin)          AS coin,
    price_usd,
    ROUND(change_24h, 2) AS change_24h_pct,
    CASE 
        WHEN change_24h >= 0 THEN 'UP' 
        ELSE 'DOWN' 
    END                  AS direction,
    loaded_at
FROM {{ source('raw', 'prices') }}