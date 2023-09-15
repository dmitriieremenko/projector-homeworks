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
  "user_id_host" integer,
  "room_id" integer,
  "start_date" date,
  "end_date" date,
  "paid" boolean
);

CREATE TABLE "users_reviews" (
  "review_id" integer PRIMARY KEY,
  "user_id_guest" integer,
  "user_id_host" integer,
  "text_review" varchar,
  "rating" integer
);

ALTER TABLE "rooms" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "booking" ADD FOREIGN KEY ("user_id_guest") REFERENCES "users" ("user_id");

ALTER TABLE "booking" ADD FOREIGN KEY ("user_id_host") REFERENCES "users" ("user_id");

ALTER TABLE "booking" ADD FOREIGN KEY ("room_id") REFERENCES "rooms" ("room_id");

ALTER TABLE "users_reviews" ADD FOREIGN KEY ("user_id_guest") REFERENCES "users" ("user_id");

ALTER TABLE "users_reviews" ADD FOREIGN KEY ("user_id_host") REFERENCES "users" ("user_id");
