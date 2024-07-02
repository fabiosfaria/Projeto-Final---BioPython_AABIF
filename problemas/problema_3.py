from Bio import SeqIO
import pandas as pd

def verificar_mutacao(sequencia, posicao_da_mutacao, nucleotideo_original, nucleotideo_mutado):
    if len(sequencia) > posicao_da_mutacao:
        if sequencia[posicao_da_mutacao] == nucleotideo_mutado:
            return True
        elif sequencia[posicao_da_mutacao] == nucleotideo_original:
            return False
    return False

def analisar_mutacoes(arquivo_fasta, posicao_da_mutacao, nucleotideo_original, nucleotideo_mutado):
    resultados = []

    for record in SeqIO.parse(arquivo_fasta, "fasta"):
        id_sequencia = record.id
        sequencia = str(record.seq)
        
        possui_mutacao = verificar_mutacao(sequencia, posicao_da_mutacao, nucleotideo_original, nucleotideo_mutado)
        
        resultados.append({
            "ID Sequência": id_sequencia,
            "Possui Mutação": possui_mutacao
        })
    
  
    df_resultados = pd.DataFrame(resultados)
    df_resultados.to_csv("relatorio_mutacoes.csv", index=False)
    print(df_resultados)

