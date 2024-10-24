def calculate_bond_income(N, S, bonds):
    lots = []
    for bond in bonds:
        day, name, price, quantity = bond
        cost = int(price * 10 * quantity)
        coupon_income = quantity * (N + 30 - day)
        nominal_income = 1000 * quantity
        total_income = coupon_income + nominal_income

        lots.append((day, name, price, quantity, cost, total_income, total_income - cost))

    dp = [[[0, []] for s in range(S + 1)] for n in range(N + 1)]

    for n in range(1, N + 1):
        for s in range(0, S + 1):
            if lots[n][4] <= s:
                if dp[n][s] > dp[n - 1][s - lots[n][4]]:
                    dp[n][s][0] = dp[n - 1][s][0]
                    dp[n][s][1] = dp[n - 1][s][1].copy()
                else:
                    dp[n][s][0] = dp[n - 1][s - lots[n][4]][0] + lots[n][6]
                    dp[n][s][1] = dp[n - 1][s - lots[n][4]][1].copy()
                    dp[n][s][1].append(lots[n])

    return dp[N][S]


if __name__ == '__main__':
    N, M, S = map(int, input().split())
    bonds = []
    while True:
        line = input().strip()
        if not line:
            break
        data = line.split()
        bonds.append([int(data[0]), data[1], float(data[2]), int(data[3])])

    result = calculate_bond_income(N, S, bonds)

    print(result[0])
    for lot in result[1]:
        print(f"{lot[0]} {lot[1]} {lot[2]} {lot[3]}")
    print()
