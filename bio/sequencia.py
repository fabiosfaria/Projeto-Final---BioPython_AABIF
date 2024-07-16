
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

    def transcricao(self):
        sequencia_transcrita = ""
        
        for base in self.sequencia:
            if base == "T":
                sequencia_transcrita += "U" # Inserindo a Uracila no lugar da Timina
            else:
                sequencia_transcrita += base    
        return sequencia_transcrita

    def traducao(self, stop_codon):
        sequencia_proteina = ""
        
        for i in range(0, len(self.sequencia), 3):
            trinca = self.sequencia[i: i+3]  
            
            if trinca in DNA_STOP_CODONS:
                if stop_codon == False:
                    sequencia_proteina += "*"
                elif stop_codon == True:
                    return sequencia_proteina
                    break
            
            if trinca in DNA_PARA_AMINOACIDO: # verificando se contem aquela trinca dentro de DNA_AMINOACIDO 
                sequencia_proteina += DNA_PARA_AMINOACIDO[trinca]
            elif trinca not in DNA_PARA_AMINOACIDO: # verificando se a trinca nao está dentro de DNA_AMINOACIDO  
                sequencia_proteina += "X"
        return sequencia_proteina