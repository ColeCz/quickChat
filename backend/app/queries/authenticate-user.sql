SELECT username
FROM user
WHERE username = %(username)s
AND passwrd = %(passwrd)s;