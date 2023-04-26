n = 0;
print(f"{'hour': <10}{'bacteria'}")
for hour in range(0, 16, 5):
    bacteria = 400 * 2 ** hour
    print(f"{hour: <10}{bacteria}")

