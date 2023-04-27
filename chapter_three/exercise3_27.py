current_population = 7.9
growth_rate = 1.09
future_population = 0;


for years in range (101):
    anticipated_population = future_population - current_population
    future_population = current_population + (1 + growth_rate) **years
    print(f"{years} {current_population} {anticipated_population}")

