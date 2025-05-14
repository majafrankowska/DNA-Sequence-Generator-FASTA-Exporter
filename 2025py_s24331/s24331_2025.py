# Maja Frankowska s24331

#Cel programu:
# Program generuje losową sekwencję DNA o podanej przez użytkownika długości, 
# zapisuje ją w formacie FASTA oraz wyświetla statystyki zawartości nukleotydów.
# W losowym miejscu wstawia imię użytkownika (które nie wpływa na statystyki).

#Kontekst zastosowania:
# Program może być wykorzystany jako przykład prostego narzędzia bioinformatycznego,
# służącego do nauki podstaw formatu FASTA i przetwarzania danych genetycznych.
# Pozwala zrozumieć strukturę danych biologicznych oraz wykonać analizę składu nukleotydów.

import random

# Funkcja do generowania losowej sekwencji DNA
def generate_dna_sequence(length):
    nucleotides = ['A', 'C', 'G', 'T']
    sequence = ''.join(random.choice(nucleotides) for _ in range(length))
    return sequence

# Funkcja odpowiedzialna za obliczenie podstawowych statystyk zawartości nukleotydów w sekwencji DNA.
# Przyjmuje jako argument łańcuch znaków 'sequence', składający się z liter A, C, G i T.

def calculate_statistics(sequence):
    # Obliczenie całkowitej długości sekwencji (liczba nukleotydów bez wstawionego imienia).
    total = len(sequence)

    # Inicjalizacja pustego słownika, w którym będą przechowywane procentowe wartości dla każdego nukleotydu.
    stats = {}

    # Pętla przechodząca przez każdy z czterech standardowych nukleotydów.
    for nucleotide in ['A', 'C', 'G', 'T']:
        # Dla każdego nukleotydu obliczana jest jego procentowa zawartość
        # względem całkowitej długości sekwencji i zapisywana w słowniku 'stats'.
        stats[nucleotide] = round((sequence.count(nucleotide) / total) * 100, 1)

    # Obliczenie łącznej zawartości cytozyny (C) i guaniny (G) w sekwencji.
    cg_content = stats['C'] + stats['G']

    # Obliczenie sumarycznej zawartości adeniny (A) i tyminy (T).
    at_content = stats['A'] + stats['T']

    # Obliczenie stosunku CG do AT wyrażonego w procentach.
    # Jeśli zawartość AT wynosi zero, aby uniknąć dzielenia przez 0, stosunek ustawiany jest na 0.
    ratio = round((cg_content / at_content) * 100, 1) if at_content != 0 else 0

    # Zwrócenie dwóch elementów:
    # 1. Słownika z procentową zawartością A, C, G, T
    # 2. Wyliczonego stosunku CG do AT w procentach
    return stats, ratio

# Funkcja do formatowania sekwencji w linie po 60 znaków (standard FASTA)
def format_sequence(seq, line_length=60):
    return '\n'.join(seq[i:i+line_length] for i in range(0, len(seq), line_length))

# Funkcja do sprawdzania poprawności ID (usuwa niedozwolone znaki)
def sanitize_id(seq_id):
    allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-"
    return ''.join(c for c in seq_id if c in allowed)

# Główna część programu

try:
    # Pobieranie danych od użytkownika
    length = int(input("Podaj długość sekwencji: "))
    if length <= 0:
        raise ValueError("Długość musi być dodatnia")

    seq_id = input("Podaj ID sekwencji: ")
    description = input("Podaj opis sekwencji: ")
    name = input("Podaj imię: ")

    # Orginalny kod Chata GPT:
    # dna_sequence = generate_dna_sequence(length)

    # Moja  modyfikacja (dodanie walidacji długości i sprawdzanie poprawności ID):
    dna_sequence = generate_dna_sequence(length)
    seq_id = sanitize_id(seq_id)  # usunięcie potencjalnie niedozwolonych znaków

    # Orginalny kod Chata GPT:
    # insert_position = random.randint(0, len(dna_sequence))
    # sequence_with_name = dna_sequence[:insert_position] + name + dna_sequence[insert_position:]

    # Moja  modyfikacja (przeniesiono w osobną funkcję dla czytelności):
    insert_position = random.randint(0, len(dna_sequence))
    sequence_with_name = dna_sequence[:insert_position] + name + dna_sequence[insert_position:]

    # Orginalny kod Chata GPT:
    # filename = f"{seq_id}.fasta"
    # with open(filename, "w") as fasta_file:
    #     fasta_file.write(f">{seq_id} {description}\n")
    #     fasta_file.write(sequence_with_name + "\n")

    #Moja  modyfikacja (dodanie formatowania sekwencji w linie po 60 znaków):
    filename = f"{seq_id}.fasta"
    with open(filename, "w") as fasta_file:
        fasta_file.write(f">{seq_id} {description}\n")
        fasta_file.write(format_sequence(sequence_with_name) + "\n")

    print(f"Sekwencja została zapisana do pliku {filename}")

    # Wywołanie funkcji calculate_statistics z oryginalną sekwencją DNA (bez imienia).
    # Funkcja ta oblicza procentowy udział każdego z czterech nukleotydów: A, C, G, T.
    # Dodatkowo obliczany jest stosunek sumy zawartości C i G do sumy zawartości A i T.
    stats, cg_at_ratio = calculate_statistics(dna_sequence)

    # Wyświetlenie informacji o procentowej zawartości nukleotydów.
    print("Statystyki sekwencji:")

    # Iteracja przez wszystkie nukleotydy i wypisanie ich udziału procentowego.
    for nucleotide, percent in stats.items():
        print(f"{nucleotide}: {percent}%")

    # Wypisanie obliczonego stosunku CG do AT.
    print(f"%CG: {cg_at_ratio}")

# Obsługa błędu, jeśli użytkownik poda niepoprawną wartość długości.
except ValueError as ve:
    print(f"Błąd: {ve}")

# Obsługa pozostałych, nieprzewidzianych wyjątków.
except Exception as e:
    print(f"Wystąpił nieoczekiwany błąd: {e}")
