create dataBASE food_delivery

--- creating tables
-----1> customers
-----2>Resturants
-----3> Menu_items
----4>Orders
----5>delivery

CREATE TABLE customers (
    customer_id INT IDENTITY(1,1) PRIMARY KEY,
    customer_name VARCHAR(30) NOT NULL,
    gender VARCHAR(20) NOT NULL,
    contact CHAR(10) NOT NULL UNIQUE,
    Address VARCHAR(100) NOT NULL,
    signup_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

create  table Restaurants(Res_id int IDENTITY(1,1) PRIMARY KEY,
Res_name varchar(30),
contact char(10) not null unique,
address varchar(100) ,
cuisine char(20),
rating int check (rating>=1 and rating<=5))

CREATE TABLE Menu_Item (
    item_id INT IDENTITY(1,1) PRIMARY KEY,
    res_id INT,
    food_item VARCHAR(50) NOT NULL,
    cuisine CHAR(20),
    price FLOAT DEFAULT 0,
    availability BIT,
    FOREIGN KEY (res_id) REFERENCES Restaurants(res_id)
);

create table Orders(order_id INT IDENTITY(1,1) PRIMARY KEY,
                    customer_id int,
					item_id int,
					Res_id int,
					quantity  tinyint check (quantity>=1),
					discount float default 0,
					total_price float default 0,
					order_datetime datetime default current_timestamp,
					foreign key(customer_id) references customers(customer_id),
					foreign key (item_id) references Menu_Item(item_id),
					foreign key (Res_id) references Restaurants(res_id))

create table Delivery(delivery_id INT IDENTITY(1,1) PRIMARY KEY,
                       order_id int ,
					   customer_id int,
					   item_id int,
					   Res_id int,
					   assigned_executive varchar(30),
					   contact_executive varchar(10),
					   status varchar(30),
					   delivery_time datetime default current_timestamp,
					   foreign key (order_id) references Orders(order_id),
					   foreign key (customer_id) references customers(customer_id),
					   foreign key (item_id) references Menu_Item(item_id),
					   foreign key (Res_id) references Restaurants(Res_id)
					   )


INSERT INTO customers
    (customer_name, gender, contact, Address)
VALUES
('Aarav Sharma', 'Male', '9876500001', 'Sector 15, Noida'),
('Priya Verma', 'Female', '9876500002', 'Sector 62, Noida'),
('Rahul Singh', 'Male', '9876500003', 'Sector 18, Noida'),
('Ananya Gupta', 'Female', '9876500004', 'Indirapuram, Ghaziabad'),
('Vikram Yadav', 'Male', '9876500005', 'Sector 50, Noida'),
('Sneha Mishra', 'Female', '9876500006', 'Greater Noida West'),
('Aditya Kumar', 'Male', '9876500007', 'Sector 137, Noida'),
('Pooja Agarwal', 'Female', '9876500008', 'Vaishali, Ghaziabad'),
('Rohit Patel', 'Male', '9876500009', 'Sector 76, Noida'),
('Neha Saxena', 'Female', '9876500010', 'Sector 12, Noida'),
('Karan Malhotra', 'Male', '9876500011', 'Sector 22, Noida'),
('Simran Kaur', 'Female', '9876500012', 'Crossings Republik, Ghaziabad'),
('Amit Chauhan', 'Male', '9876500013', 'Sector 44, Noida'),
('Kavya Joshi', 'Female', '9876500014', 'Sector 121, Noida'),
('Manish Tiwari', 'Male', '9876500015', 'Sector 78, Noida'),
('Riya Kapoor', 'Female', '9876500016', 'Alpha 1, Greater Noida'),
('Saurabh Pandey', 'Male', '9876500017', 'Sector 51, Noida'),
('Ishita Mehta', 'Female', '9876500018', 'Sector 104, Noida'),
('Deepak Saini', 'Male', '9876500019', 'Sector 19, Noida'),
('Meera Nair', 'Female', '9876500020', 'Sector 137, Noida'),
('Arjun Thakur', 'Male', '9876500021', 'Beta 2, Greater Noida'),
('Divya Reddy', 'Female', '9876500022', 'Sector 75, Noida'),
('Nikhil Jain', 'Male', '9876500023', 'Sector 45, Noida'),
('Shreya Das', 'Female', '9876500024', 'Sector 100, Noida'),
('Varun Bansal', 'Male', '9876500025', 'Sector 16, Noida'),
('Aisha Khan', 'Female', '9876500026', 'Sector 49, Noida'),
('Mohit Rawat', 'Male', '9876500027', 'Raj Nagar, Ghaziabad'),
('Tanvi Arora', 'Female', '9876500028', 'Sector 93, Noida'),
('Rajat Choudhary', 'Male', '9876500029', 'Sector 120, Noida'),
('Nandini Roy', 'Female', '9876500030', 'Sector 34, Noida'),
('Abhishek Dubey', 'Male', '9876500031', 'Sector 52, Noida'),
('Sakshi Bhatia', 'Female', '9876500032', 'Sector 128, Noida'),
('Harsh Vardhan', 'Male', '9876500033', 'Surajpur, Greater Noida'),
('Muskan Ali', 'Female', '9876500034', 'Sector 70, Noida'),
('Gaurav Mishra', 'Male', '9876500035', 'Sector 41, Noida'),
('Palak Sinha', 'Female', '9876500036', 'Sector 143, Noida'),
('Yash Thakur', 'Male', '9876500037', 'Sector 63, Noida'),
('Komal Pandey', 'Female', '9876500038', 'Sector 21, Noida'),
('Pranav Goyal', 'Male', '9876500039', 'Sector 110, Noida'),
('Ritika Sen', 'Female', '9876500040', 'Sector 137, Noida'),
('Akash Tripathi', 'Male', '9876500041', 'Sector 27, Noida'),
('Payal Chawla', 'Female', '9876500042', 'Sector 48, Noida'),
('Shivam Saxena', 'Male', '9876500043', 'Knowledge Park, Greater Noida'),
(' Kriti Anand', 'Female', '9876500044', 'Sector 74, Noida'),
('Devendra Pal', 'Male', '9876500045', 'Sector 31, Noida'),
('Ira Malhotra', 'Female', '9876500046', 'Sector 135, Noida'),
('Sameer Qureshi', 'Male', '9876500047', 'Sector 55, Noida'),
('Bhavna Tomar', 'Female', '9876500048', 'Sector 122, Noida'),
('Ankit Srivastava', 'Male', '9876500049', 'Sector 20, Noida'),
('Tanya Bhardwaj', 'Female', '9876500050', 'Pari Chowk, Greater Noida');

INSERT INTO Restaurants
    (Res_name, contact, address, cuisine, rating)
VALUES
('Spice Garden', '9810000001', 'Sector 18, Noida', 'Indian', 5),
('Dragon House', '9810000002', 'Sector 62, Noida', 'Chinese', 4),
('Pizza Corner', '9810000003', 'Sector 15, Noida', 'Italian', 4),
('South Spice', '9810000004', 'Sector 50, Noida', 'South Indian', 5),
('Burger Point', '9810000005', 'Sector 12, Noida', 'Fast Food', 3),
('Royal Biryani', '9810000006', 'Sector 76, Noida', 'Indian', 5),
('Pasta Palace', '9810000007', 'Sector 137, Noida', 'Italian', 4),
('Tandoori Nights', '9810000008', 'Indirapuram, Ghaziabad', 'Indian', 5),
('Noodle Street', '9810000009', 'Sector 44, Noida', 'Chinese', 3),
('Sweet Treats', '9810000010', 'Sector 22, Noida', 'Dessert', 4),
('Curry House', '9810000011', 'Sector 51, Noida', 'Indian', 4),
('Momo Junction', '9810000012', 'Sector 18, Noida', 'Chinese', 5),
('Italian Bistro', '9810000013', 'Sector 104, Noida', 'Italian', 4),
('Dosa Express', '9810000014', 'Sector 75, Noida', 'South Indian', 4),
('Food Factory', '9810000015', 'Greater Noida West', 'Fast Food', 3),
('The Food Court', '9810000016', 'Alpha 1, Greater Noida', 'Indian', 4),
('Chilli Flames', '9810000017', 'Sector 63, Noida', 'Chinese', 5),
('Cafe Delight', '9810000018', 'Sector 49, Noida', 'Cafe', 4),
('Biryani Blues', '9810000019', 'Sector 120, Noida', 'Indian', 5),
('Pizza Hub', '9810000020', 'Sector 34, Noida', 'Italian', 3),
('Punjabi Dhaba', '9810000021', 'Sector 27, Noida', 'Punjabi', 4),
('Wok Express', '9810000022', 'Sector 93, Noida', 'Chinese', 4),
('Grill Masters', '9810000023', 'Sector 45, Noida', 'Fast Food', 5),
('Healthy Bites', '9810000024', 'Sector 128, Noida', 'Healthy Food', 4),
('Kebab Kingdom', '9810000025', 'Sector 19, Noida', 'Mughlai', 5),
('The Sweet Spot', '9810000026', 'Vaishali, Ghaziabad', 'Dessert', 4),
('Urban Tadka', '9810000027', 'Sector 78, Noida', 'Indian', 5),
('Cafe Mocha', '9810000028', 'Sector 100, Noida', 'Cafe', 3),
('Rolls & More', '9810000029', 'Sector 121, Noida', 'Fast Food', 4),
('Sushi World', '9810000030', 'Sector 137, Noida', 'Japanese', 4),
('Chaat Bazaar', '9810000031', 'Sector 15, Noida', 'Indian', 5),
('Steak House', '9810000032', 'Sector 62, Noida', 'Continental', 4),
('Taco Fiesta', '9810000033', 'Sector 50, Noida', 'Mexican', 3),
('The Biryani Pot', '9810000034', 'Sector 76, Noida', 'Indian', 4),
('Pancake Cafe', '9810000035', 'Sector 18, Noida', 'Cafe', 5),
('Flavours of India', '9810000036', 'Sector 110, Noida', 'Indian', 4),
('Chinese Wok', '9810000037', 'Sector 52, Noida', 'Chinese', 3),
('Wrap Station', '9810000038', 'Sector 143, Noida', 'Fast Food', 4),
('The Dessert Bar', '9810000039', 'Sector 74, Noida', 'Dessert', 5),
('Coastal Kitchen', '9810000040', 'Sector 41, Noida', 'Seafood', 4),
('Veggie Delight', '9810000041', 'Beta 2, Greater Noida', 'Vegetarian', 4),
('The Grill House', '9810000042', 'Sector 55, Noida', 'Continental', 5),
('Cafe Aroma', '9810000043', 'Sector 20, Noida', 'Cafe', 3),
('Royal Thali', '9810000044', 'Knowledge Park, Greater Noida', 'Indian', 4),
('Pasta & More', '9810000045', 'Sector 135, Noida', 'Italian', 5),
('Bowl Company', '9810000046', 'Sector 48, Noida', 'Healthy Food', 4),
('Street Food Hub', '9810000047', 'Sector 31, Noida', 'Street Food', 3),
('The Curry Leaf', '9810000048', 'Sector 122, Noida', 'South Indian', 5),
('Flame & Fork', '9810000049', 'Pari Chowk, Greater Noida', 'Continental', 4),
('Midnight Munchies', '9810000050', 'Crossings Republik, Ghaziabad', 'Fast Food', 4);

select * from Menu_Item

INSERT INTO Orders
(customer_id, item_id, Res_id, quantity, discount, total_price) VALUES
(1,1,1,2,10,450),
(2,2,2,1,0,199),
(3,3,3,3,5,282.15),
(4,4,4,2,10,504),
(5,5,5,1,0,240),
(6,6,6,2,5,342),
(7,7,7,3,0,360),
(8,8,8,2,10,180),
(9,9,9,1,0,220),
(10,10,10,2,5,247),
(11,11,11,1,10,189),
(12,12,12,2,0,520),
(13,13,13,2,5,285),
(14,14,14,3,10,378),
(15,15,15,1,0,190),
(16,16,16,2,5,380),
(17,17,17,1,10,288),
(18,18,18,3,0,480),
(19,19,19,2,5,190),
(20,20,20,1,0,120),
(21,21,21,2,10,630),
(22,22,22,2,5,266),
(23,23,23,4,0,320),
(24,24,24,1,10,252),
(25,25,25,2,5,342),
(26,26,26,3,0,510),
(27,27,27,1,5,218.50),
(28,28,28,2,10,522),
(29,29,29,2,0,320),
(30,30,30,1,5,237.50),
(31,31,31,3,10,297),
(32,32,32,2,5,456),
(33,33,33,1,0,220),
(34,34,34,4,10,324),
(35,35,35,2,5,570),
(36,36,36,2,0,340),
(37,37,37,3,0,240),
(38,38,38,2,5,228),
(39,39,39,1,10,144),
(40,40,40,2,5,608),
(41,41,41,3,0,390),
(42,42,42,4,10,324),
(43,43,43,1,5,228),
(44,44,44,2,10,396),
(45,45,45,1,0,280),
(46,46,46,5,5,332.50),
(47,47,47,2,10,378),
(48,48,48,3,0,450),
(49,49,49,2,5,342),
(50,50,50,1,10,269.10);

INSERT INTO Delivery
(order_id, customer_id, item_id, Res_id,
 assigned_executive, contact_executive, status) VALUES
(1,1,1,1,'Aman Kumar','9200000001','Delivered'),
(2,2,2,2,'Ravi Singh','9200000002','Delivered'),
(3,3,3,3,'Vijay Sharma','9200000003','Out for Delivery'),
(4,4,4,4,'Suresh Yadav','9200000004','Delivered'),
(5,5,5,5,'Rohit Verma','9200000005','Preparing'),
(6,6,6,6,'Amit Gupta','9200000006','Delivered'),
(7,7,7,7,'Karan Mishra','9200000007','Out for Delivery'),
(8,8,8,8,'Deepak Singh','9200000008','Delivered'),
(9,9,9,9,'Mohit Kumar','9200000009','Assigned'),
(10,10,10,10,'Arjun Patel','9200000010','Delivered'),
(11,11,11,11,'Rahul Jain','9200000011','Delivered'),
(12,12,12,12,'Nitin Das','9200000012','Out for Delivery'),
(13,13,13,13,'Varun Roy','9200000013','Delivered'),
(14,14,14,14,'Sanjay Pal','9200000014','Preparing'),
(15,15,15,15,'Ankit Raj','9200000015','Delivered'),
(16,16,16,16,'Pankaj Tiwari','9200000016','Delivered'),
(17,17,17,17,'Manoj Saini','9200000017','Out for Delivery'),
(18,18,18,18,'Yash Malhotra','9200000018','Delivered'),
(19,19,19,19,'Ajay Chauhan','9200000019','Assigned'),
(20,20,20,20,'Sumit Arora','9200000020','Delivered'),
(21,21,21,21,'Vikas Pandey','9200000021','Delivered'),
(22,22,22,22,'Tarun Joshi','9200000022','Out for Delivery'),
(23,23,23,23,'Gaurav Mehta','9200000023','Delivered'),
(24,24,24,24,'Harsh Kapoor','9200000024','Preparing'),
(25,25,25,25,'Abhishek Roy','9200000025','Delivered'),
(26,26,26,26,'Naveen Kumar','9200000026','Delivered'),
(27,27,27,27,'Rakesh Mishra','9200000027','Out for Delivery'),
(28,28,28,28,'Shivam Gupta','9200000028','Delivered'),
(29,29,29,29,'Pradeep Singh','9200000029','Assigned'),
(30,30,30,30,'Kunal Verma','9200000030','Delivered'),
(31,31,31,31,'Akhil Sharma','9200000031','Delivered'),
(32,32,32,32,'Rajesh Yadav','9200000032','Out for Delivery'),
(33,33,33,33,'Sahil Jain','9200000033','Delivered'),
(34,34,34,34,'Lokesh Kumar','9200000034','Preparing'),
(35,35,35,35,'Dinesh Patel','9200000035','Delivered'),
(36,36,36,36,'Sandeep Roy','9200000036','Delivered'),
(37,37,37,37,'Raman Singh','9200000037','Out for Delivery'),
(38,38,38,38,'Chirag Gupta','9200000038','Delivered'),
(39,39,39,39,'Akash Verma','9200000039','Assigned'),
(40,40,40,40,'Mukesh Kumar','9200000040','Delivered'),
(41,41,41,41,'Rajat Sharma','9200000041','Delivered'),
(42,42,42,42,'Vivek Mishra','9200000042','Out for Delivery'),
(43,43,43,43,'Nikhil Singh','9200000043','Delivered'),
(44,44,44,44,'Sachin Yadav','9200000044','Preparing'),
(45,45,45,45,'Piyush Jain','9200000045','Delivered'),
(46,46,46,46,'Anurag Verma','9200000046','Delivered'),
(47,47,47,47,'Varun Gupta','9200000047','Out for Delivery'),
(48,48,48,48,'Rohit Mishra','9200000048','Delivered'),
(49,49,49,49,'Aman Singh','9200000049','Assigned'),
(50,50,50,50,'Keshav Kumar','9200000050','Delivered')

select count(*) from Delivery
select count(*) from Menu_Item
select count(*) from Restaurants
select count(*) from Menu_Item
select count(*) from customers

----Average order Cost-------

select avg(total_price) as average_order_cost from Orders;

-- join the table customers and orders.

select customers.customer_id, customer_name ,Orders.order_id,order_datetime,food_item,Res_name,assigned_executive,contact_executive
from customers left join Orders on customers.customer_id=Orders.customer_id join Menu_item
on Orders.item_id=Menu_item.item_id join Restaurants on Restaurants.Res_id=Orders.Res_id
join Delivery on delivery.order_id=Orders.order_id;


BULK INSERT customers
FROM 'C:\Users\sidpa\OneDrive\Desktop\Food_Delievery_Customer_Analysis\sql\food_delivery_csv_file\customers.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    FIELDQUOTE = '"',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);

--- to show the column order in table---
EXEC sp_help 'customers';
select * from customers

--set global local_info=off;
--show global variables like 'local_infile';

--SQL Server does not have the local_infile system variable. If you want to check whether ad hoc bulk operations are enabled, use:
EXEC sp_configure 'show advanced options';

--If you need to configure advanced SQL Server settings, execute---
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;


EXEC sp_configure 'Ad Hoc Distributed Queries', 1;
RECONFIGURE;
--To check the configuration for bulk import permissions and options, you can use:
EXEC sp_configure 'Ad Hoc Distributed Queries';




BULK INSERT Orders
FROM 'C:\Users\sidpa\OneDrive\Desktop\Food_Delievery_Customer_Analysis\sql\food_delivery_csv_file\Orders.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    FIELDQUOTE = '"',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);

select * from Orders

BULK INSERT Delivery
FROM 'C:\Users\sidpa\OneDrive\Desktop\Food_Delievery_Customer_Analysis\sql\food_delivery_csv_file\Delivery.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    FIELDQUOTE = '"',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);
select * from Delivery


BULK INSERT Menu_item
FROM 'C:\Users\sidpa\OneDrive\Desktop\Food_Delievery_Customer_Analysis\sql\food_delivery_csv_file\Menu_item.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    FIELDQUOTE = '"',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);


BULK INSERT dbo.Orders
FROM 'C:\Users\sidpa\OneDrive\Desktop\Food_Delievery_Customer_Analysis\sql\food_delivery_csv_file\Orders.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);


BULK INSERT Restaurants
FROM 'C:\Users\sidpa\OneDrive\Desktop\Food_Delievery_Customer_Analysis\sql\food_delivery_csv_file\Restaurants.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    FIELDQUOTE = '"',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);
select * from Restaurants
select * from Orders
select * from Menu_Item
select * from Delivery
select * from customers
