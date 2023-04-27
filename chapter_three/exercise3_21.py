jump = float (input("Enter the achieved jump: "))

longest_jump = 8.85
difference = longest_jump - jump
if jump < longest_jump:
    print(f"You need to jump: {difference} additional meters to improve the world record.")
    print(f"Meters = {difference: .1f}")
    print(f"DeciMeters = {difference *10: .1f}")
    print(f"CentiMeters = {difference * 100: .1f}")
    print(f"MilliMeters = {difference * 1000: .1f}")