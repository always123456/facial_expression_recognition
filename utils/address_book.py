friend_emails = {
    "Anne": "anne@example.com",
    "Brent": "brent@example.com",
    "Dan": "dan@example.com",
    "David": "david@example.com",
    "Fox": "fox@example.com",
    "Jane": "jane@example.com",
    "Kevin": "kevin@example.com",
    "Robert": "robert@example.com",
}

def look_up(name):
    try:
        return friend_emails[name]
    except KeyError as e:
        # str(e)可返回刚才尝试查询的键的值
        print(f"无法查询到{str(e)}的email")

while True:
    name = input("Enter name to look up:")
    email = look_up(name)
    print(f"Email: {email}")