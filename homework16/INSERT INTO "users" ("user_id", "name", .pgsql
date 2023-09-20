INSERT INTO "users" ("user_id", "name", "user_type")
VALUES (1, 'John Doe', 'Host'),
       (2, 'Jane Smith', 'Guest'),
       (3, 'Alice Johnson', 'Guest');

INSERT INTO "rooms" ("room_id", "user_id", "name_room", "residents", "price", "air_conditioning", "refrigerator", "reservation")
VALUES (101, 1, 'Cozy Studio', 2, 75.00, TRUE, TRUE, TRUE),
       (102, 1, 'Spacious Loft', 4, 150.00, TRUE, TRUE, TRUE),
       (103, 2, 'Private Suite', 2, 100.00, TRUE, FALSE, TRUE);

INSERT INTO "booking" ("booking_id", "user_id_guest", "room_id", "start_date", "end_date", "paid")
VALUES (1001, 2, 101, '2023-09-20', '2023-09-25', TRUE),
       (1002, 3, 103, '2023-10-05', '2023-10-10', TRUE),
       (1003, 2, 102, '2023-09-15', '2023-09-20', FALSE);
