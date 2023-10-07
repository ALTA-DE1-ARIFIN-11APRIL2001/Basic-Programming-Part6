def compare(a, b):
    pattern = ""

    min_len = min(len(a), len(b))
    for i in range(min_len):
        if a[i] == b[i]:
            pattern += a[i]
        else:
            break

    return pattern

if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA