SELECT sender_username
FROM friends
WHERE receiver_username = %(username)s AND friendship_status = 'pending'