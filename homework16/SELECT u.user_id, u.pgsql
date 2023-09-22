SELECT u.user_id, u.name
FROM users u
JOIN (
    SELECT b.user_id_guest, COUNT(*) AS booking_count
    FROM booking b
    GROUP BY b.user_id_guest
    ORDER BY booking_count DESC
    LIMIT 1
) AS top_guest ON u.user_id = top_guest.user_id_guest;
