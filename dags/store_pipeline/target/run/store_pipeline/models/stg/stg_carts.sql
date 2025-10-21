
  
  create view "dev"."main"."stg_carts__dbt_tmp" as (
    WITH raw_carts AS(
    SELECT * FROM "dev"."main"."carts"
)
SELECT CAST(product_id AS INT) AS product_id,
        CAST(user_id AS INT) AS user_id,
        CAST(cart_id AS INT) AS cart_id,
        CAST(cart_date AS TIMESTAMP) AS cart_date,
        CAST(quantity AS INT) AS quantity
FROM raw_carts
  );
