'''
Contains schemas for users and roles
'''


# Format user for schema
def user_schema(id, name, points):
    user = {
        "discord_ID": id,
        "name": name,
        "roles": [],
        "points": points
    }
    return user

def role_schema(role_id, role_name, role_max_pts):
    role = {
        "role_id": role_id,
        "role_name": role_name,
        "max_pts": role_max_pts
    }
    return role


