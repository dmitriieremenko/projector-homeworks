CREATE TABLE "users" (
  "user_id" integer PRIMARY KEY,
  "name" varchar,
  "user_type" varchar
);

CREATE TABLE "rooms" (
  "room_id" integer PRIMARY KEY,
  "user_id" integer,
  "name_room" varchar,
  "residents" integer,
  "price" decimal,
  "air_conditioning" boolean,
  "refrigerator" boolean,
  "reservation" boolean
);

CREATE TABLE "booking" (
  "booking_id" integer PRIMARY KEY,
  "user_id_guest" integer,
  "room_id" integer,
  "start_date" date,
  "end_date" date,
  "paid" boolean
);

CREATE TABLE "payments" (
  "payment_id" integer PRIMARY KEY,
  "booking_id" integer,
  "amount" decimal,
  "payment_date" date
);

CREATE TABLE "users_reviews" (
  "review_id" integer PRIMARY KEY,
  "booking_id" integer,
  "text_review" varchar,
  "rating" integer
);

ALTER TABLE "rooms" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "booking" ADD FOREIGN KEY ("user_id_guest") REFERENCES "users" ("user_id");

ALTER TABLE "booking" ADD FOREIGN KEY ("room_id") REFERENCES "rooms" ("room_id");

ALTER TABLE "payments" ADD FOREIGN KEY ("booking_id") REFERENCES "booking" ("booking_id");

ALTER TABLE "users_reviews" ADD FOREIGN KEY ("booking_id") REFERENCES "booking" ("booking_id");
