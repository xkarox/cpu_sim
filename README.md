
## Roadmap: Vom Gatter zur CPU

### Meilenstein 1: Die "Atome" der Logik (Boolesche Algebra) 💡

**Lernziel:** Verstehen, dass *jede* Operation in einer CPU (von `+` bis `if`) am Ende auf simplen logischen Gattern basiert.

* **1.1. Die Gatter-Bibliothek:**
    * Beginne *nicht* mit der `Bit`-Klasse, sondern mit simplen Python-Funktionen, die `bool`-Werte nehmen und zurückgeben.
    * Implementiere `nand_gate(a: bool, b: bool) -> bool`.
    * **Übung:** Baue *nur* mit deiner `nand_gate`-Funktion alle anderen Gatter:
        * `not_gate(a)` (Tipp: `nand_gate(a, a)`)
        * `and_gate(a, b)`
        * `or_gate(a, b)`
        * `xor_gate(a, b)`
* **1.2. Die `Bit`-Klasse (Refactoring):**
    * Jetzt führst du deine `Bit`-Klasse ein. Sie ist ein "Wrapper" um `bool`, der hauptsächlich das `__str__` (für "1" / "0") schöner macht.
    * Passe deine Gatter-Funktionen an, sodass sie `Bit`-Objekte akzeptieren und zurückgeben.
* **1.3. Der Multiplexer (MUX):**
    * Implementiere `mux_2_to_1(a: Bit, b: Bit, sel: Bit) -> Bit`.
    * Ein MUX ist ein "Daten-Schalter". Wenn `sel` 0 ist, kommt `a` raus. Wenn `sel` 1 ist, kommt `b` raus.
    * **Erkenntnis:** "So funktioniert eine `if`-Abfrage in Hardware!"

---

### Meilenstein 2: Kombinatorische Logik (Das Rechenwerk) ➕

**Lernziel:** Verstehen, wie man aus Gattern Schaltnetze baut, die *rechnen* können. Der Output hängt *nur* vom aktuellen Input ab (kein Gedächtnis).

* **2.1. Der Halbaddierer (Half-Adder):**
    * Schreibe eine Funktion `half_adder(a: Bit, b: Bit) -> (Bit, Bit)`.
    * Der Rückgabewert ist `(sum_bit, carry_out_bit)`.
    * Baue ihn *explizit* aus deinen Gatter-Funktionen (z.B. `sum = xor_gate(a, b)`).
* **2.2. Der Volladdierer (Full-Adder):**
    * Schreibe `full_adder(a: Bit, b: Bit, carry_in: Bit) -> (Bit, Bit)`.
    * **Übung:** Baue ihn *explizit* aus zwei `half_adder`-Funktionen und einem `or_gate`. 
* **2.3. Die `Byte`-Klasse & das Addierwerk:**
    * Implementiere deine `Byte`-Klasse (mit `list[Bit]`).
    * Implementiere `__add__(self, other: 'Byte')`.
    * **WICHTIG:** Implementiere `__add__` *nicht* mit Python-Magie, sondern durch eine 8-fache Schleife, die deine `full_adder`-Funktion aufruft. Der `carry_out` der einen Stufe wird zum `carry_in` der nächsten. Das ist das **Ripple-Carry-Addierwerk**.
* **2.4. Die Arithmetic Logic Unit (ALU):**
    * Beweise die Macht des Zweierkomplements: Implementiere `__sub__` als `A + (~B) + 1`.
    * Implementiere `__and__`, `__or__` (diese sind einfach, da sie bitweise arbeiten).
    * **Bonus-Meisterstück:** Baue eine `ALU`-Klasse.
        * `ALU.execute(op_code: str, a: Byte, b: Byte) -> Byte`
        * Der `op_code` (z.B. `"add"`, `"sub"`, `"and"`) steuert, welches Ergebnis zurückgegeben wird. (Tipp: Ein 8-Bit-MUX ist hier nützlich!)

---

### Meilenstein 3: Sequentielle Logik (Das Gedächtnis) 🧠

**Lernziel:** Den *wichtigsten Sprung* verstehen: Wie entsteht "Zustand" (Gedächtnis)? Der Output hängt vom Input *und* dem gespeicherten Zustand ab.

* **3.1. Das D-Flip-Flop (D-FF):**
    * Das ist die 1-Bit-Speicherzelle. Alle Register basieren darauf.
    * Implementiere eine `class D_Flip_Flop`.
    * Attribute: `q: Bit` (der gespeicherte Zustand).
    * Methode: `clock_tick(data_in: Bit, load_enable: Bit)`.
    * *Logik:* `if load_enable.state == True: self.q = data_in`.
    * **Erkenntnis:** Der Zustand ändert sich *nur*, wenn der Takt "tickt" *und* das `load_enable`-Signal an ist.
* **3.2. Das 8-Bit-Register:**
    * Implementiere eine `class Register`.
    * Intern besteht sie einfach aus `list[D_Flip_Flop]` (8 Stück).
    * Methoden:
        * `read() -> Byte`: Gibt ein `Byte`-Objekt zurück, das aus den 8 `q`-Zuständen der Flip-Flops besteht.
        * `write(data_in: Byte, load_enable: Bit, clock: Bit)`: Ruft `clock_tick` für jedes der 8 Flip-Flops auf.

---

### Meilenstein 4: Die Von-Neumann-Architektur (Das System) 🏛️

**Lernziel:** Die Hauptkomponenten (Speicher, Register) zu einem System verbinden.

* **4.1. Der Hauptspeicher (RAM):**
    * Implementiere eine `class RAM`.
    * Intern ist das (vereinfacht) eine `list[Byte]` fester Größe (z.B. 256).
    * Methoden: `read(address: Byte) -> Byte` und `write(address: Byte, data: Byte)`. (Du musst `address` für den Listen-Index in `int` umwandeln).
* **4.2. Der Register-Satz (Register File):**
    * Eine simple Klasse, die deine Arbeitsregister bündelt.
    * `R0 = Register()`, `R1 = Register()`, `IR = Register()` (Instruction Register).
* **4.3. Der Program Counter (PC):**
    * Das ist ein spezielles Register (erbt von `Register`).
    * Er hat eine zusätzliche Methode: `increment(clock: Bit)`.
    * *Logik:* Er liest seinen eigenen Wert, ruft dein Addierwerk (`full_adder`...) auf, um `+1` zu rechnen, und schreibt das Ergebnis bei `clock_tick` in sich selbst zurück.

---

### Meilenstein 5: Das Steuerwerk (Der Dirigent) 🎶

**Lernziel:** Den "Fetch-Decode-Execute"-Zyklus verstehen, der alles orchestriert.

* **5.1. Der Befehlssatz (ISA):**
    * Definiere simple Opcodes (z.B. `0x01` = `LOAD R0, [Adresse]`, `0x10` = `ADD R0, R1`, `0xFF` = `HALT`).
* **5.2. Das "ROM" / Programm:**
    * Lade dein Programm, indem du dein `RAM`-Objekt händisch füllst:
        * `ram.write(Byte(num=0), Byte(num=0x01))` // Befehl LOAD an Adresse 0
        * `ram.write(Byte(num=1), Byte(num=0x10))` // Adresse 16 (für LOAD)
        * ...
* **5.3. Die `CPU`-Hauptschleife (Fetch-Decode-Execute):**
    * Implementiere eine `CPU`-Klasse, die `RAM`, `PC`, `ALU`, Register usw. besitzt.
    * Implementiere die `run()`-Methode, eine große `while True:`-Schleife:
        1.  **Takt-Signal:** Simuliere einen Takt (z.B. `clock_tick()`).
        2.  **Fetch:** Lade den Befehl, auf den der `PC` zeigt, aus dem `RAM` in das `Instruction Register (IR)`. `ir.write(ram.read(pc.read()), ...)`
        3.  **Increment:** Sage dem `PC`, er soll sich erhöhen. `pc.increment(...)`
        4.  **Decode:** Ein großes `match/case` (oder `if/elif`) auf dem `IR.read()`.
        5.  **Execute:**
            * *Beispiel `ADD R0, R1`*: Rufe `alu_result = alu.execute("add", R0.read(), R1.read())` auf.
            * Schreibe das Ergebnis zurück: `R0.write(alu_result, load_enable=Bit(True), ...)`
            * *Beispiel `LOAD`*: Lade die Adresse (Folge-Byte) aus dem RAM, lies *von dort* die Daten und schreibe sie in `R0`.
            * *Beispiel `HALT`*: `break` aus der Schleife.
