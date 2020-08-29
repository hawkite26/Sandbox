ages_dict = {"Bill": 21, "Jane": 34, "Jack": 56}
user_name = input("Name: ")
user_age = input("Age: ")
ages_dict[user_name] = user_age
for name in ages_dict:
    print("{:7} - {:>5}".format(name, ages_dict[name]))
