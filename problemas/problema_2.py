from bio.ler_fasta import ler_fasta



arquivo_fasta = 'arquivos/Flaviviridae-genomes.fasta'
sequencias = ler_fasta(arquivo_fasta)

print("HELLO")
print(sequencias)