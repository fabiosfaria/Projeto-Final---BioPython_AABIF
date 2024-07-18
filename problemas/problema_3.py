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
    print()
    break
    #print(sequencias_sem_mutacao["sequencia"])

#print(sequencias_sem_mutacao)
print("Sequências SEM Mutação")        
