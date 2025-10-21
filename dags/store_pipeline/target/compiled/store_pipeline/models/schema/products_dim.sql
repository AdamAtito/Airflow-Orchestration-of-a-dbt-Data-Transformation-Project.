WITH products_dim AS(
    SELECT * FROM "dev"."main"."stg_products"
)
SELECT * FROM products_dim