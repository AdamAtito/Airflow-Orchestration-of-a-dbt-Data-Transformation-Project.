WITH users_dim AS (
    SELECT * FROM {{ ref('stg_users') }}
)
SELECT * FROM users_dim