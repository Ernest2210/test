def get_shares_percentage_expression(shares):
    total_sum = sum(shares)
    result = []
    for share in shares:
        percentage = share / total_sum
        result.append(round(percentage, 3))

    return result


if __name__ == '__main__':
    N = int(input())
    data = [float(input()) for _ in range(N)]
    percentages = get_shares_percentage_expression(data)

    for percentage in percentages:
        print(percentage)
