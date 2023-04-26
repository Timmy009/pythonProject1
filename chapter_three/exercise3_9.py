seconds = int(input("Enter seconds: "))
hours = 0
minute = 0
remaining_sec = 0
count = 0
sec = 0
while seconds >= count:
    if seconds >= 3600:
        hours = hours + seconds // 3600
        sec = hours * 3600
    elif seconds < 3600:
        minute = minute + (seconds % 3600) // 60
        sec = minute * 60
    else:
        remaining_sec = remaining_sec + (seconds % 3600) % 60

    seconds = seconds - sec - remaining_sec

print(f"{hours}-{minute}-{remaining_sec}")
