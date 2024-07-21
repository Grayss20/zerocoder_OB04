class User():
    def __init__(self, user):
        self.user = user


class UserNameChanger():
    def __init__(self, user):
        self.user = user

    def change_name(self, new_name):
        self.user.user = new_name


class SaveUser():
    def __init__(self, user):
        self.user = user

    def save(self):
        file = open("users.txt", "a")
        file.write(self.user)
        file.close()


# Initialize a user
user1 = User("Alice")

# Change the user's name
name_changer = UserNameChanger(user1)
name_changer.change_name("Alice Cooper")

# Save the new name to a file
#saver = SaveUser(name_changer.user)
#saver.save()

print(user1.user)
print(name_changer.user.user)
