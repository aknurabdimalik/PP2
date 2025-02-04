def solve(numheads, numlegs):
    for i in range(1, numheads+1):
        y = numheads - i
        if 2*i + 4*y == numlegs:
            print(f"{i} rabbits, {y} chickens")

solve(35, 94)