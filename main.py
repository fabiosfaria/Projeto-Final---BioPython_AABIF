from Bio import SeqIO, Seq
from bio.ler_fasta import ler_fasta
from bio.constantes import DNA_PARA_AMINOACIDO
from bio.constantes import DNA_STOP_CODONS
from bio.sequencia import Sequencia


arquivo_fasta = 'arquivos/Flaviviridae-genomes.fasta'
sequencias = ler_fasta(arquivo_fasta) 

seq_unica = sequencias[1].sequencia
#print(seq_unica)

# Testando PROBLEMA-2
sequencia_classe = Sequencia(sequencias[1].nome, seq_unica) 
#resultado_classe = sequencia_classe.traducao(stop_codon=False)
#print(resultado_classe)

# Testando Metodo TRANSCRICAO 
resultado_classe = sequencia_classe.transcricao()
#print(resultado_classe)


