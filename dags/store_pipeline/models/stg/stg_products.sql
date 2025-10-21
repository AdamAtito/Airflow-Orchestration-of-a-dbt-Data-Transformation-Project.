WITH raw_products AS(
    SELECT * FROM {{ source('raw', 'products') }}
)
SELECT CAST(id AS INT) AS product_id, 
        CAST(title AS VARCHAR) AS product_title,
        CAST(price AS FLOAT) AS product_price,
        CAST(description AS VARCHAR) AS product_description,
        CAST(category AS VARCHAR) AS product_category,
        CAST(rating_rate AS FLOAT) AS product_rating_rate,
        CAST(rating_count AS INT) AS product_rating_count
FROM raw_products
