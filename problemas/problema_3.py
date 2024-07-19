""" 
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bio.ler_fasta import ler_fasta

arquivo_fasta = 'arquivo/Flaviviridae-genomes.fasta'
sequencias = ler_fasta(arquivo_fasta)

sequencias_com_mutacao = sequencias_sem_mutacao = {
    "id": "",
    "nome": "",
    "sequencia": ""
}

for cada_sequencia in sequencias:
    if cada_sequencia.sequencia[999] == "G": 
        sequencias_com_mutacao["id"] += cada_sequencia.id
        sequencias_com_mutacao["nome"] += cada_sequencia.nome
        sequencias_com_mutacao["sequencia"] += cada_sequencia.sequencia
        
    else:
        sequencias_sem_mutacao["id"] += cada_sequencia.id
        sequencias_sem_mutacao["nome"] += cada_sequencia.nome
        sequencias_sem_mutacao["sequencia"] += cada_sequencia.sequencia

#gera_relatorio_de_mutacoes(sequencias_sem_mutacao)
#print("Sequências COM Mutação")

for i in sequencias_sem_mutacao:
    print(f'{i["id"] + " " + i["nome"]}')
    break
    #print(sequencias_sem_mutacao["sequencia"])

#print(sequencias_sem_mutacao)
print("Sequências SEM Mutação")        
 """
from Bio import SeqIO

def verificar_mutacao(sequencia, posicao, nucleotideo_original, nucleotideo_mutado):
    # Verifica se a mutação está presente na posição especificada
    return sequencia[posicao - 1] == nucleotideo_mutado

def gerar_relatorio(arquivo_fasta, posicao, nucleotideo_original, nucleotideo_mutado):
    with open("arquivos/Flaviviridae-genomes.fasta", "r") as handle:
        sequencias = list(SeqIO.parse(handle, "fasta"))
    
    relatorio = []
    for seq_record in sequencias:
        id_seq = seq_record.id
        sequencia = str(seq_record.seq)
        if verificar_mutacao(sequencia, posicao, nucleotideo_original, nucleotideo_mutado):
            relatorio.append(f"Sequência {id_seq}: Mutação presente")
        else:
            relatorio.append(f"Sequência {id_seq}: Mutação ausente")
    
    return relatorio

# Parâmetros
arquivo_fasta = "genomas_virais.fasta"
posicao = 1000
nucleotideo_original = "A"
nucleotideo_mutado = "G"

# Gerar relatório
relatorio = gerar_relatorio(arquivo_fasta, posicao, nucleotideo_original, nucleotideo_mutado)
for linha in relatorio:
    print(linha)