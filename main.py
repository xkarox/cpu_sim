from Bit import Bit

def main():
    print(f"NAND(1 1): {nand_gate(Bit(1), Bit(1))}")
    print(f"NAND(0 1): {nand_gate(Bit(0), Bit(1))}")
    print(f"NAND(0 0): {nand_gate(Bit(0), Bit(0))}")

    print(f'NOT(1): {not_gate(Bit(1))}')
    print(f'NOT(0): {not_gate(Bit(0))}')

    print(f'AND(0 0): {and_gate(Bit(0), Bit(0))}')
    print(f'AND(0 1): {and_gate(Bit(0), Bit(1))}')
    print(f'AND(1 0): {and_gate(Bit(1), Bit(0))}')
    print(f'AND(1 1): {and_gate(Bit(1), Bit(1))}')

    print(f'OR(0 0): {or_gate(Bit(0), Bit(0))}')
    print(f'OR(0 1): {or_gate(Bit(0), Bit(1))}')
    print(f'OR(1 0): {or_gate(Bit(1), Bit(0))}')
    print(f'OR(1 1): {or_gate(Bit(1), Bit(1))}')

    print(f'XOR(0 0): {xor_gate(Bit(0), Bit(0))}')
    print(f'XOR(0 1): {xor_gate(Bit(0), Bit(1))}')
    print(f'XOR(1 0): {xor_gate(Bit(1), Bit(0))}')
    print(f'XOR(1 1): {xor_gate(Bit(1), Bit(1))}')

def nand_gate(a: Bit, b: Bit) -> Bit:
    return Bit(not (bool(a) and bool(b)))

def not_gate(a: Bit) -> Bit:
    return nand_gate(a, a)

def and_gate(a: Bit, b: Bit) -> Bit:
    return nand_gate(nand_gate(a, b), nand_gate(a, b))

def or_gate(a: Bit, b: Bit) -> Bit:
    return nand_gate(nand_gate(a, a), nand_gate(b, b))

def xor_gate(a: Bit, b: Bit) -> Bit:
    return nand_gate(nand_gate(a, nand_gate(a, b)), nand_gate(nand_gate(a, b), b))



if __name__ == "__main__":
    main()