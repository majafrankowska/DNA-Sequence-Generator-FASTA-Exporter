import random

def generate_dna_sequence(length):
    nucleotides = ['A', 'C', 'G', 'T']
    sequence = ''.join(random.choice(nucleotides) for _ in range(length))
    return sequence

def calculate_statistics(sequence):
    total = len(sequence)
    stats = {}
    for nucleotide in ['A', 'C', 'G', 'T']:
        stats[nucleotide] = round((sequence.count(nucleotide) / total) * 100, 1)
    cg_content = stats['C'] + stats['G']
    at_content = stats['A'] + stats['T']
    ratio = round((cg_content / at_content) * 100, 1) if at_content != 0 else 0
    return stats, ratio

length = int(input("Podaj długość sekwencji: "))
seq_id = input("Podaj ID sekwencji: ")
description = input("Podaj opis sekwencji: ")
name = input("Podaj imię: ")

dna_sequence = generate_dna_sequence(length)
insert_position = random.randint(0, len(dna_sequence))
sequence_with_name = dna_sequence[:insert_position] + name + dna_sequence[insert_position:]

filename = f"{seq_id}.fasta"
with open(filename, "w") as fasta_file:
    fasta_file.write(f">{seq_id} {description}\n")
    fasta_file.write(sequence_with_name + "\n")

print(f"Sekwencja została zapisana do pliku {filename}")

stats, cg_at_ratio = calculate_statistics(dna_sequence)

print("Statystyki sekwencji:")
for nucleotide, percent in stats.items():
    print(f"{nucleotide}: {percent}%")
print(f"%CG: {cg_at_ratio}")