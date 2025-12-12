SELECT
    CASE
        WHEN sender_username = %(username)s THEN receiver_username
        ELSE sender_username
    END AS friend
FROM friends
WHERE (sender_username = %(username)s OR receiver_username = %(username)s)
  AND friendship_status = 'accepted';
