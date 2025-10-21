WITH users_dim AS (
    SELECT * FROM "dev"."main"."stg_users"
)
SELECT * FROM users_dim