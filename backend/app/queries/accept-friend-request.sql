UPDATE friends
SET friendship_status = 'accepted'
WHERE sender_username = %(sender_username)s AND receiver_username = %(receiver_username)s