
WITH carts AS(
    SELECT * FROM "dev"."main"."carts_dim"
),
users AS(
    SELECT * FROM "dev"."main"."users_dim"
),
products AS(
    SELECT * FROM "dev"."main"."products_dim"
)
SELECT u.user_id, c.cart_id, p.product_id, p.product_price, p.product_rating_count,
         p.product_rating_count, c.cart_date, (c.quantity * p.product_price) AS total_amount, p.product_category
FROM carts c 
JOIN users u ON c.user_id = u.user_id
JOIN products p ON c.product_id = p.product_id