import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bio.sequencia import Sequencia 
from bio.ler_fasta import ler_fasta 


arquivo_fasta = 'arquivos/Flaviviridae-genomes.fasta'
bases_nucleotideos = ['A', 'T', 'C', 'G']

sequencias = ler_fasta(arquivo_fasta)
for seq in sequencias:
    percentuais = seq.calcular_percentual(bases_nucleotideos)
    print(f"Sequência: {seq.nome}")
    for base, percentual in percentuais.items():
        print(f"{base}: {percentual:.2f}%")
    gc_content = percentuais['G'] + percentuais['C']
    print(f"Conteúdo GC: {gc_content:.2f}%")
    print()
