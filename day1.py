# Formatting string
hour = 10
minute = 45
print("current time is %s : %s" % (hour, minute))

print("""It's saied triple quote can diplay
what ever I want.""")

print("Just to show ** is exponential: 5**2 = %d" %(5**2))

# string.format() built-in
# {[field name] ["!" conversion] [":" format spec]}
print("or write in this way {0:4d}:{1:4d}".format(hour, minute))

# python use dent to indicate scope
# more strict on style
prize = None

if hour < 11 :
    prize = True

if prize:
    gift = int( input("How much money would you like?"))
    print("gift card %.2f" % gift)

print("Enjoy")
