ID = []

def fasta_downloader(ID):
    """
    Función creada para cargar id_coati.txt en id_coatiy.py, de manera que se va a
    descargar en formato genbank la información correspondiente a los identificadores 
    de accesión usando el ENTREZ de Biopython para guardar en coati y en coati.gb
    """
    with open("data/coati.txt","r") as coati:
        for seq_record in coati:
            Entrez.email = "andres.benalcazar@est.ikiam.edu.ec"
            with Entrez.efetch( db="nucleotide", rettype="gb", retmode="text", id= coati) as handle:
                seq_record = SeqIO.read(coati, "gb"):
                seq_record.append(coati, "gb")
        
       
    return
 
def alignment():
    """
    Función creada para que el algoritmo extraiga solamente    
    las secuencias de la variable coati y realice un alineamiento usando clustalW. 
    El resultado debe ser coati.aln y coati.dnd que deben guardarse en su carpeta de trabajo
    """
    
    
    return

def tree(): 
    """
    Sirve creada para que realice el cálculo de las distancias 
    utilizando coati.aln y finalmente que imprima en la pantalla el 
    árbol filogenético y guarde en su carpeta de trabajo el arbol como coati_phylotree.pdf
    """

    return