speeds = []

for runners in range(1, 11):
    speed = float(input(f"Enter the speed of the {runners} runner"))
    speeds.append(speed)

fastest = max(speeds)
lowest = min(speeds)

print(fastest)
print(lowest)
