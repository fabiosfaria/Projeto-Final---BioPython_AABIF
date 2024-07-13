from Bio import SeqIO, Seq
from bio.ler_fasta import ler_fasta
from bio.constantes import DNA_PARA_AMINOACIDO
from bio.constantes import DNA_STOP_CODONS
from bio.sequencia import Sequencia


arquivo_fasta = 'arquivos/Flaviviridae-genomes.fasta'
sequencias = ler_fasta(arquivo_fasta) 

#print(sequencias)

# LE TODO O ARQUIVO COM TODAS AS SEQUENCIAS 
#for seq in sequencias:
    #print(f"Sequencia: {seq.nome}")
    #print(f"ID Sequencia: {seq.sequencia}") #pegando cada sequencia 

seq_unica = sequencias[1].sequencia

sequencia_classe = Sequencia(sequencias[1].nome, seq_unica) 
resultado_classe = sequencia_classe.traducao(stop_codon=False)
print(resultado_classe)