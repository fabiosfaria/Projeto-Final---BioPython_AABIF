
from bio.organismo_fasta import OrganismoFasta

def ler_fasta(caminho_do_arquivo):
    sequencias = []
    
    with open(caminho_do_arquivo, 'r') as f:
        id, nome, sequencia = '', '', ''
        for line in f:
            if line.startswith('>'):
                if sequencia:
                    sequencias.append(OrganismoFasta(id, nome, sequencia))
                    sequencia = ''
                header_parts = line[1:].strip().split(' ', 1)
                id = header_parts[0]
                nome = header_parts[1] if len(header_parts) > 1 else ''
            else:
                sequencia += line.strip()
        if sequencia:
            sequencias.append(OrganismoFasta(id, nome, sequencia))
    return sequencias
