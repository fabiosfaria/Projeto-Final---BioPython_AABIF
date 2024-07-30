from bio.ler_fasta import ler_fasta
from bio.sequencia import Sequencia
from problemas.problema_3 import sequencias_mutadas


arquivo_fasta = 'arquivos/Flaviviridae-genomes.fasta'
sequencias = ler_fasta(arquivo_fasta) 

seq_unica = sequencias[1].sequencia
#print(seq_unica)

# Testando PROBLEMA-2 => 
sequencia_classe = Sequencia(seq_unica) 
resultado_Problema_2_F = sequencia_classe.traducao(to_stop=False)
resultado_Problema_2_T = sequencia_classe.traducao(to_stop=True)
#print(f'\nResultado do PROBLEMA-2 com o atributo To_Stop FALSE =>\n\n{resultado_Problema_2_F}')
#print(f'\nResultado do PROBLEMA-2 com o atributo To_Stop TRUE =>\n\n{resultado_Problema_2_T}')

# ---------------------------------------------------------------

pequena_sequencia = Sequencia("ACTGAAGCT")

# Testando Método TRANSCRICAO() => 
resultado_Metodo_Transcricao = seq_unica.transcricao()
#print(f'\nResultado do Método transcricao() =>\n{resultado_Metodo_Transcricao}')
print(f'\nResultado do Método transcricao() na Sequencia Pequena [ACTGAAGCT] =>\n{pequena_sequencia.transcricao()}')

# Testando Método SEQUENCIA_COMPLEMENTAR() => 
resultado_Metodo_SequenciaComplementar = seq_unica.sequencia_complementar()
#print(f'\nResultado do Método sequencia_complementar() =>\n{resultado_Metodo_SequenciaComplementar}')
print(f'\nResultado do Método sequencia_complementar() na Sequencia Pequena [ACTGAAGCT] =>\n{pequena_sequencia.sequencia_complementar()}')


# Testando Método SEQUENCIA_COMPLEMENTAR_REVERSA() => 
resultado_Metodo_SequenciaComplementarReversa = seq_unica.sequencia_complementar_reversa()
#print(f'\nResultado do Método sequencia_complementar_reversa() =>\n{resultado_Metodo_SequenciaComplementarReversa}')
print(f'\nResultado do Método sequencia_complementar_reversa() na Sequencia Pequena [ACTGAAGCT] =>\n{pequena_sequencia.sequencia_complementar_reversa()}')


# ---------------------------------------------------------------

# Testando PROBLEMA-3 => 
sequencias_mutadas(sequencias)


