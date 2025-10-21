WITH products_dim AS(
    SELECT * FROM {{ ref('stg_products') }}
)
SELECT * FROM products_dim