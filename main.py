from typing import Callable

from Bit import Bit

def main():
    # NAND Tests (2 inputs)
    print_gate("NAND", "1", "1", "", "0", str(nand_gate(Bit(1), Bit(1))))
    print_gate("NAND", "0", "1", "", "1", str(nand_gate(Bit(0), Bit(1))))
    print_gate("NAND", "0", "0", "", "1", str(nand_gate(Bit(0), Bit(0))))
    print("-" * 25)  # Trennlinie

    # NOT Tests (1 input)
    print_gate("NOT", "1", "", "", "0", str(not_gate(Bit(1))))
    print_gate("NOT", "0", "", "", "1", str(not_gate(Bit(0))))
    print("-" * 25)  # Trennlinie

    # AND Tests (2 inputs)
    print_gate("AND", "0", "0", "", "0", str(and_gate(Bit(0), Bit(0))))
    print_gate("AND", "0", "1", "", "0", str(and_gate(Bit(0), Bit(1))))
    print_gate("AND", "1", "0", "", "0", str(and_gate(Bit(1), Bit(0))))
    print_gate("AND", "1", "1", "", "1", str(and_gate(Bit(1), Bit(1))))
    print("-" * 25)  # Trennlinie

    # OR Tests (2 inputs)
    print_gate("OR", "0", "0", "", "0", str(or_gate(Bit(0), Bit(0))))
    print_gate("OR", "0", "1", "", "1", str(or_gate(Bit(0), Bit(1))))
    print_gate("OR", "1", "0", "", "1", str(or_gate(Bit(1), Bit(0))))
    print_gate("OR", "1", "1", "", "1", str(or_gate(Bit(1), Bit(1))))
    print("-" * 25)  # Trennlinie

    # XOR Tests (2 inputs)
    print_gate("XOR", "0", "0", "", "0", str(xor_gate(Bit(0), Bit(0))))
    print_gate("XOR", "0", "1", "", "1", str(xor_gate(Bit(0), Bit(1))))
    print_gate("XOR", "1", "0", "", "1", str(xor_gate(Bit(1), Bit(0))))
    print_gate("XOR", "1", "1", "", "0", str(xor_gate(Bit(1), Bit(1))))
    print("-" * 25)  # Trennlinie

    # MUX Tests (Inputs: a, b, sel)
    print("MUX Tests (a, b, sel)")
    # Wenn sel=0, erwarte a
    print_gate("MUX", "0", "0", "0", "0", str(mux_2_to_1(Bit(0), Bit(0), Bit(0))))
    print_gate("MUX", "0", "1", "0", "0", str(mux_2_to_1(Bit(0), Bit(1), Bit(0))))
    print_gate("MUX", "1", "0", "0", "1", str(mux_2_to_1(Bit(1), Bit(0), Bit(0))))
    print_gate("MUX", "1", "1", "0", "1", str(mux_2_to_1(Bit(1), Bit(1), Bit(0))))

    # Wenn sel=1, erwarte b
    print_gate("MUX", "0", "0", "1", "0", str(mux_2_to_1(Bit(0), Bit(0), Bit(1))))
    print_gate("MUX", "0", "1", "1", "1", str(mux_2_to_1(Bit(0), Bit(1), Bit(1))))
    print_gate("MUX", "1", "0", "1", "0", str(mux_2_to_1(Bit(1), Bit(0), Bit(1))))
    print_gate("MUX", "1", "1", "1", "1", str(mux_2_to_1(Bit(1), Bit(1), Bit(1))))

def print_gate(name: str, in_one: str, in_two: str, in_three: str, expected_out: str, actual_out: str):
    inputs = f"{in_one if in_one else ' '}{in_two if in_two else ' '}{in_three if in_three else ' '}"
    print(f"{name.ljust(4)} {inputs.ljust(4)} => {expected_out} = {actual_out}")

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

def mux_2_to_1(a: Bit, b: Bit, sel: Bit) -> Bit:
    not_sel = not_gate(sel)
    nand_a = nand_gate(a, not_sel)
    nand_b = nand_gate(b, sel)
    return nand_gate(nand_a, nand_b)






if __name__ == "__main__":
    main()