def count_sheep(sheeps):
    if not sheeps:
        return 0
    return len(list(filter(lambda x: x, sheeps)))