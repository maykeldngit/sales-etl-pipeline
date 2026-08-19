-- ============================================
-- SALES ETL PIPELINE
-- Initial test data
-- ============================================


-- ============================================
-- CATEGORIES
-- ============================================

INSERT INTO categories (category_name)
VALUES
('Electronics'),
('Furniture'),
('Clothing');


-- ============================================
-- CUSTOMERS
-- ============================================

INSERT INTO customers
(first_name, last_name, email, city, country)
VALUES
('John', 'Smith', 'john.smith@email.com', 'Montevideo', 'Uruguay'),
('Maria', 'Garcia', 'maria.garcia@email.com', 'Buenos Aires', 'Argentina'),
('Carlos', 'Rodriguez', 'carlos.rodriguez@email.com', 'Santiago', 'Chile'),
('Ana', 'Martinez', 'ana.martinez@email.com', 'Cordoba', 'Argentina'),
('David', 'Wilson', 'david.wilson@email.com', 'Montevideo', 'Uruguay');


-- ============================================
-- PRODUCTS
-- ============================================

INSERT INTO products
(product_name, category_id, price, stock_quantity)
VALUES
('Laptop', 1, 1200.00, 15),
('Smartphone', 1, 800.00, 25),
('Headphones', 1, 150.00, 40),
('Office Desk', 2, 350.00, 10),
('Office Chair', 2, 250.00, 20),
('T-Shirt', 3, 30.00, 100),
('Jeans', 3, 60.00, 50),
('Jacket', 3, 120.00, 30);


-- ============================================
-- ORDERS
-- ============================================

INSERT INTO orders
(customer_id, order_date, status)
VALUES
(1, '2026-08-01 10:30:00', 'Completed'),
(2, '2026-08-02 14:15:00', 'Completed'),
(3, '2026-08-03 09:45:00', 'Pending'),
(1, '2026-08-04 16:20:00', 'Completed'),
(4, '2026-08-05 11:10:00', 'Cancelled'),
(5, '2026-08-06 13:50:00', 'Completed'),
(2, '2026-08-07 15:30:00', 'Pending'),
(3, '2026-08-08 10:00:00', 'Completed');


-- ============================================
-- ORDER DETAILS
-- ============================================

INSERT INTO order_details
(order_id, product_id, quantity, unit_price)
VALUES
(1, 1, 1, 1200.00),
(1, 3, 2, 150.00),

(2, 2, 1, 800.00),
(2, 6, 3, 30.00),

(3, 4, 1, 350.00),
(3, 5, 2, 250.00),

(4, 7, 2, 60.00),
(4, 8, 1, 120.00),

(5, 6, 5, 30.00),

(6, 1, 1, 1200.00),
(6, 5, 1, 250.00),

(7, 2, 2, 800.00),

(8, 3, 1, 150.00),
(8, 7, 1, 60.00);