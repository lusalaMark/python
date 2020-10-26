# If name is less than three characters long
#          Name must be at least 3 characters
# Otherwise if it is more than 50 characters long
#          Name can be a maximum of 50 characters
# Otherwise
#            Name looks good
name = 'jane'
if len(name) < 3:
    print("Name must be at least 3 characters ")
elif len(name) > 50:
    print("Name must be a maximum of 50 character")
else:
    print("Name looks good")
