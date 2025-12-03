SELECT username
FROM users
WHERE username = %(username)s
AND passwrd = %(passwrd)s;