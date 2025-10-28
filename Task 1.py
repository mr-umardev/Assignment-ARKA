def get_users_older_than_18(users):
    older_users=[]
    for user in users:
        if user['age']>=18:
            older_users.append(user['name'])
    return older_users
    
user_list = [
    {'name': 'Umar','age':21},
    {'name': 'Afreen', 'age': 24}
    ]

print(get_users_older_than_18(user_list))
