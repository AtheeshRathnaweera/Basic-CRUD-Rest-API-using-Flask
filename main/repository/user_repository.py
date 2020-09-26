from flask import jsonify


class UserRepository:
    users = [
        {'id': 1,
         'name': 'Atheesh Rathnaweera',
         'email': 'rathnaweeraatheesh72@gmail.com'
         },
        {'id': 2,
         'name': 'Buddhika Rathnaweera',
         'email': 'buddhikarathnaweera@gmail.com'
         },
        {'id': 3,
         'name': 'Danushi Karunarathne',
         'email': 'danushi@gmail.com'
         }
    ]

    def get_all(self):
        return jsonify(self.users)

    def get_by_id(self, user_id):
        result = {}
        for user in self.users:
            if user["id"] == user_id:
                result = jsonify(user)
                break

        return result

    def save(self, new_user):
        result = None

        for user in self.users:
            if user["id"] == new_user["id"]:
                return result

        self.users.append(new_user)
        result = jsonify(new_user)
        return result

    def update(self, user_id, new_user):
        result = None

        for user in self.users:
            if user["id"] == user_id:
                print("user found")
                user["name"] = new_user["name"]
                user["email"] = new_user["email"]
                result = jsonify(user)
                break

        return result

    def delete(self, user_id):
        result = "delete failed"

        for user in self.users:
            if user["id"] == user_id:
                self.users.remove(user)
                result = "delete success"
                break

        return result
