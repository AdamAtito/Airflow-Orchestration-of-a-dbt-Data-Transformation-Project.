
  
  create view "dev"."main"."carts_dim__dbt_tmp" as (
    WITH carts_dim AS(
    SELECT * FROM "dev"."main"."stg_carts"
)
SELECT * FROM carts_dim
  );
