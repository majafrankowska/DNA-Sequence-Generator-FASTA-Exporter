# DNA Sequence Generator & FASTA Exporter

Project developed as part of Bioinformatics / File Processing exercises for PBIO class at PJATK

---

## 🧬 Description

This Python script generates a random DNA sequence of user-defined length, inserts a user-provided name at a random location, and saves the sequence in [FASTA](https://en.wikipedia.org/wiki/FASTA_format) format. The name insertion does **not affect biological statistics** of the DNA (A/C/G/T ratio). After saving, the script also calculates and displays the nucleotide composition and CG/AT ratio.

The script was developed as part of a university bioinformatics exercise, but is built in a clean, reusable way and could be adapted for educational tools or synthetic DNA sequence testing.

---

## 🚀 Features

- User-defined DNA length
- Dynamic name insertion (for personalization or testing)
- FASTA export with correct formatting (60 characters per line)
- ID sanitization to create safe file names
- Nucleotide frequency statistics (A, C, G, T)
- CG vs AT ratio (%)
- Input validation and basic error handling

---

## 📂 Example Output

### Sample interaction:
- Podaj długość sekwencji: 30
- Podaj ID sekwencji: Test123
- Podaj opis sekwencji: Przykładowa sekwencja testowa
- Podaj imię: Maya

### Sample `.fasta` file:
Test123 Przykładowa sekwencja testowa
GTAATCCAATTCTTCMayaCGTTAGCCCACCGGG

### Console output:
Sekwencja została zapisana do pliku Test123.fasta
Statystyki sekwencji:
A: 20.0%
C: 33.3%
G: 20.0%
T: 26.7%
%CG: 114.1

---

## ▶️ How to Run

Make sure you have Python 3 installed. Follow the on-screen prompts.

Then run:

```bash
python s24331_2025.py
