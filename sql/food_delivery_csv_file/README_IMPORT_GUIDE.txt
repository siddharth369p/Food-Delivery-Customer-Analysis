FOOD DELIVERY CSV IMPORT PACK

Files: customers.csv, Restaurants.csv, Menu_item.csv, Orders.csv, Delivery.csv

This is extra sample data for the existing food_delivery schema. It contains repeat orders
by the same customers, repeated items, varied order dates, and intentional cleaning issues:
extra spaces, mixed capitalization, inconsistent delivery statuses, and some incorrect
stored totals. Clean these values in a staging copy or after import.

IMPORTANT:
- IDs are explicitly set to 1001+ to keep foreign keys consistent across this pack.
- Before importing, check that IDs 1001+ are not already in use in any target table.
- Back up the database first.
- Import in this order: customers -> Restaurants -> Menu_item -> Orders -> Delivery.
- Import the ID columns as well. Ensure the wizard maps columns by name.
- The pack's internal foreign keys are consistent: each order references a customer,
  menu item, and restaurant in this pack; each delivery references an order in this pack.

Check for repeat customers:
SELECT customer_id, COUNT(*) AS order_count
FROM Orders GROUP BY customer_id ORDER BY order_count DESC;

Check row counts:
SELECT COUNT(*) FROM customers;
SELECT COUNT(*) FROM Restaurants;
SELECT COUNT(*) FROM Menu_item;
SELECT COUNT(*) FROM Orders;
SELECT COUNT(*) FROM Delivery;
