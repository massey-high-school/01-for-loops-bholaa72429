# Time Converter, 31/10/2019, GTT
# v1: converts seconds to minutes and seconds

# Get number of seconds
seconds = int(input("How many seconds?"))

# Convert to minutes and seconds
minutes = seconds // 60
seconds_left = seconds % 60

# Output answer
print("{} is {} minutes and {} seconds".format(seconds, minutes, seconds_left))






