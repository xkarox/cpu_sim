def main():
    print(f"NAND(1 1): {nand_gate(True, True)}")
    print(f"NAND(0 1): {nand_gate(False, True)}")
    print(f"NAND(0 0): {nand_gate(False, False)}")

    print(f'NOT(1): {not_gate(True)}')
    print(f'NOT(0): {not_gate(False)}')

    print(f'AND(0 0): {and_gate(False, False)}')
    print(f'AND(0 1): {and_gate(False, True)}')
    print(f'AND(1 0): {and_gate(True, False)}')
    print(f'AND(1 1): {and_gate(True, True)}')

    print(f'OR(0 0): {or_gate(False, False)}')
    print(f'OR(0 1): {or_gate(False, True)}')
    print(f'OR(1 0): {or_gate(True, False)}')
    print(f'OR(1 1): {or_gate(True, True)}')

    print(f'XOR(0 0): {or_gate(False, False)}')
    print(f'XOR(0 1): {or_gate(False, True)}')
    print(f'XOR(1 0): {or_gate(True, False)}')
    print(f'XOR(1 1): {or_gate(True, True)}')

def nand_gate(a: bool, b: bool) -> bool:
    if a and b:
        return False
    else:
        return True


def not_gate(a: bool) -> bool:
    return nand_gate(a, a)


def and_gate(a: bool, b: bool) -> bool:
    return nand_gate(nand_gate(a, b), nand_gate(a, b))

def or_gate(a: bool, b: bool) -> bool:
    return nand_gate(nand_gate(a, a), nand_gate(b, b))

def xor_gate(a: bool, b: bool) -> bool:
    pass # das ist bissl kniffliger


if __name__ == "__main__":
    main()