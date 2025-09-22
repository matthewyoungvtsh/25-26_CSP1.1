seconds = int(input("How many seconds? "))
hours = int(seconds / 3600)
secondsLeft = seconds % 3600
minutes = int(secondsLeft / 60)
Seconds = secondsLeft % 60

print("Lab03, 80 Point Version")
print()
print("Starting seconds:", seconds)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", Seconds)
print(seconds, "seconds =", hours, "hours,", minutes, "minutes, and", Seconds, "seconds")