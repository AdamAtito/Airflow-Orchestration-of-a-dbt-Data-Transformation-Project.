WITH carts_dim AS(
    SELECT * FROM {{ ref('stg_carts') }}
)
SELECT * FROM carts_dim