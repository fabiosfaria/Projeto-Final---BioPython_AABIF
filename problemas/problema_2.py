import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bio.ler_fasta import ler_fasta
from bio.sequencia import Sequencia 


arquivo_fasta = 'arquivos/Flaviviridae-genomes.fasta'
sequencias = ler_fasta(arquivo_fasta)
sequencia_classe = "" 
proteina_organismo = "" 

for sequencia_organismo in sequencias:
    print(f"ORGANISMO: {sequencia_organismo.nome}, PROTEINA => ")
    sequencia_classe = Sequencia(sequencia_organismo.nome, sequencia_organismo.sequencia)
    proteina_organismo = sequencia_classe.traducao(stop_codon=True)
    print(proteina_organismo + "\n")
    
    sequencia_classe = "" # zerando os valores 
    proteina_organismo = ""

    