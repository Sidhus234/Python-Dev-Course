is_magician = True
is_expert = False

# Check if magician and expert: "you are master magician"
# if magician but not expert: "At least you are getting there"
# if not magician: "You need magic power"

if is_magician and is_expert:
    print("You are Master Magician")
elif is_magician and not is_expert:
    print("At Least you are getting there")
elif not is_magician:
    print("You need magic power")