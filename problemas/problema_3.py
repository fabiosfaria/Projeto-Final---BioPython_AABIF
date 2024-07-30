
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bio.ler_fasta import ler_fasta

def sequencias_mutadas(sequencias):
    for cada_sequencia in sequencias:
        if cada_sequencia.sequencia[999] == "G": 
            print("Esta Sequência POSSUI a mutação => ")
            print(f'ID => {cada_sequencia.id}')
            print(f'NOME => {cada_sequencia.nome}')
            print("\n")
            
        else:
            print("Esta Sequência NÃO possui a mutação => ")
            print(f'ID => {cada_sequencia.id}')
            print(f'NOME => {cada_sequencia.nome}')
            print("\n")

arquivo_fasta = 'arquivos/Flaviviridae-genomes.fasta'
sequencias = ler_fasta(arquivo_fasta)
sequencias_mutadas(sequencias)