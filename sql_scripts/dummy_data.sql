BEGIN;

-- Insert into Inventory table
INSERT INTO inventory_inventoryitem (name, stock)
VALUES
    ('Wireless Mouse', 120),
    ('Gaming Keyboard', 80),
    ('Monitor 24-inch', 50),
    ('USB-C Cable', 200),
    ('External SSD 1TB', 30);

-- Insert into Orders table
INSERT INTO orders_order (user_id, status, created_at)
VALUES
    (101, 'created', '2024-12-02 10:30:00'),
    (102, 'shipped', '2024-12-02 11:00:00'),
    (103, 'delivered', '2024-12-02 12:00:00'),
    (101, 'created', '2024-12-02 13:00:00'),
    (104, 'shipped', '2024-12-02 14:00:00');

COMMIT;


