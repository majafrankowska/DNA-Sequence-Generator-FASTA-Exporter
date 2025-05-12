# Maja Frankowska s24331

# Program generuje losową sekwencję DNA o podanej przez użytkownika długości, 
# zapisuje ją w formacie FASTA oraz wyświetla statystyki zawartości nukleotydów.
# W losowym miejscu wstawia imię użytkownika (które nie wpływa na statystyki).

import random

# Funkcja do generowania losowej sekwencji DNA
def generate_dna_sequence(length):
    nucleotides = ['A', 'C', 'G', 'T']
    sequence = ''.join(random.choice(nucleotides) for _ in range(length))
    return sequence

# Funkcja do obliczania statystyk nukleotydowych
def calculate_statistics(sequence):
    total = len(sequence)
    stats = {}
    for nucleotide in ['A', 'C', 'G', 'T']:
        stats[nucleotide] = round((sequence.count(nucleotide) / total) * 100, 1)
    cg_content = stats['C'] + stats['G']
    at_content = stats['A'] + stats['T']
    ratio = round((cg_content / at_content) * 100, 1) if at_content != 0 else 0
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

    # Obliczanie i wyświetlanie statystyk (bez wstawionego imienia)
    stats, cg_at_ratio = calculate_statistics(dna_sequence)

    print("Statystyki sekwencji:")
    for nucleotide, percent in stats.items():
        print(f"{nucleotide}: {percent}%")
    print(f"%CG: {cg_at_ratio}")

except ValueError as ve:
    print(f"Błąd: {ve}")
except Exception as e:
    print(f"Wystąpił nieoczekiwany błąd: {e}")
