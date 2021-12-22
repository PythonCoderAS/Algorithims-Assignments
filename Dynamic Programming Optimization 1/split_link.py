def split_link(prices):
    """Splits the chain on a link. Variable prices is an array of possible prices."""
    data = [0] * (len(prices) + 4)
    current_index = len(prices) - 3
    while current_index >= 0:
        option_1 = sum(prices[current_index:current_index+3]) + data[current_index + 4]
        option_2 = sum(prices[current_index:current_index+2]) + data[current_index + 3]
        data[current_index] = max(option_1, option_2)
        current_index -= 1
    return max(data[0:3])
