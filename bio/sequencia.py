
from bio.constantes import DNA_PARA_AMINOACIDO
from bio.constantes import DNA_STOP_CODONS


class Sequencia:
    def __init__(self, nome, sequencia):
        self.nome = nome
        self.sequencia = sequencia

    def __repr__(self):
        return f'Sequencia("{self.sequencia}")'

    def __iter__(self):
        return self.sequencia

    def __str__(self):
        return self.sequencia

    def __len__(self):
        return len(self.sequencia)

    def __eq__(self, outra_sequencia):
        return str(self) == str(outra_sequencia)

    def __getitem__(self, index):
        return self.sequencia.__getitem__(index)
    
    
    def sequencia_complementar(self):
            bases_dicionario = {
            "A": "T",
            "C": "G",
            "T": "A",
            "G": "C",
            }
            sequencia_complementar = ""
            for base in self.sequencia:
                if base in bases_dicionario:
                    sequencia_complementar += bases_dicionario[base]
            return sequencia_complementar
            
            
    def sequencia_complementar_reversa(self):
        sequencia_complementar = self.sequencia_complementar()
        sequencia_complementar_reversa = ""
        bases = len(sequencia_complementar)
        
        while(bases > 0):
            bases -= 1
            sequencia_complementar_reversa += sequencia_complementar[bases]
            print("ENTROU EM WHILE")
            
        #for base in range(tamanho, sequencia_complementar, 0):
            #print(sequencia_reversa[base])
            #sequencia_complementar_reversa += sequencia_complementar[base]
         
        return sequencia_complementar_reversa




    def calcular_percentual(self, bases):
            total_bases = len(self.sequencia)
            base_counts = {base: self.sequencia.count(base) for base in bases}
            percentuais = {base: (count / total_bases) * 100 for base, count in base_counts.items()}
            return percentuais

    def transcricao(self):
        sequencia_transcrita = ""
        
        for base in self.sequencia:
            if base == "T":
                sequencia_transcrita += "U" # Inserindo a Uracila no lugar da Timina
            else:
                sequencia_transcrita += base    
        return sequencia_transcrita

    def traducao(self, to_stop):
        sequencia_proteina = ""
        
        for i in range(0, len(self.sequencia), 3):
            trinca = self.sequencia[i: i+3]  
            
            if trinca in DNA_STOP_CODONS:
                if to_stop == False:
                    sequencia_proteina += "*"
                elif to_stop == True:
                    return sequencia_proteina
                    break
            else: 
                if trinca in DNA_PARA_AMINOACIDO: # Verificando se contém aquela trinca dentro de DNA_AMINOACIDO 
                    sequencia_proteina += DNA_PARA_AMINOACIDO[trinca]
                else: # SE a trinca NÃO está dentro de DNA_AMINOACIDO E STOP_CODON 
                    sequencia_proteina += "X"
        return sequencia_proteina