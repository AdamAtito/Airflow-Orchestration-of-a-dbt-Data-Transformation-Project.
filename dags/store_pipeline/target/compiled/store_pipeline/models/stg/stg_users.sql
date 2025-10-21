WITH raw_users AS(
    SELECT * FROM "dev"."main"."users"
)
SELECT CAST(id AS INT) AS user_id, 
        CAST(email AS VARCHAR) AS user_email,
        CAST(username AS VARCHAR) AS user_username,
        CAST(password AS VARCHAR) AS user_password,
        CAST(name_firstname AS VARCHAR) AS user_name_firstname,
        CAST(name_lastname AS VARCHAR) AS user_name_lastname,
        CAST(address_city AS VARCHAR) AS user_address_city,
        CAST(address_street AS VARCHAR) AS user_address_street,
        CAST(address_number AS INT) AS user_address_number,
        CAST(address_zipcode AS VARCHAR) AS user_address_zipcode,
        CAST(phone AS VARCHAR) AS user_phone
FROM raw_users