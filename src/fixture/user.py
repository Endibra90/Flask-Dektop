from model.user import User
def load(db):
    for user in [
        {'email': 'guest@guest.net', 'password': 'guest_secret', 'postal_code': '00001',
         'role': 'guest', 'username': 'Guest'},
        {'email': 'user@user.net', 'password': 'user_secret', 'postal_code': '00002',
         'username': 'User'},
        {'email': 'admin@admin.net', 'password': 'admin_secret', 'postal_code': '00003',
         'role': 'admin', 'username': 'Administrator'}
    ]:
        db.session.add(User(**user))