from werkzeug.security import generate_password_hash, check_password_hash

hash = generate_password_hash('foobar')
print(hash)
# method$salt$hash

print(check_password_hash(hash, 'foobar'))