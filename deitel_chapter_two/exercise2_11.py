seconds = int(input("Enter seconds: "))

hours = seconds // 3600

minute = (seconds % 3600) // 60

seconds = (seconds % 3600) % 60

print(f"{hours}-{minute}-{seconds}")
