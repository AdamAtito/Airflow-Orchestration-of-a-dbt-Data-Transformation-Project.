
  
  create view "dev"."main"."products_dim__dbt_tmp" as (
    WITH products_dim AS(
    SELECT * FROM "dev"."main"."stg_products"
)
SELECT * FROM products_dim
  );
