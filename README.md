Plasmid Design with ORI Detection

Objective
To design a plasmid that functions in an unknown organism by first detecting
the organism-specific origin of replication (ORI) from the input DNA sequence.

Methodology
1. The input genome sequence is provided in FASTA format.
2. The ORI is predicted using GC skew analysis, as taught in class.
3. This newly identified ORI is used as the replication backbone of the plasmid.
4. A design file specifies restriction sites to remove and markers to include.
5. Marker sequences are loaded from markers.tab.
6. The final plasmid sequence is written in FASTA format.

Marker Handling
Only markers present in markers.tab are incorporated.
If a marker is not found, the program skips it without crashing.

Testing
The implementation is tested using pUC19.fa and Design_pUC19.txt.
The test confirms removal of the EcoRI site from the output plasmid.

Files
Input.fa              : Unknown organism DNA sequence  
Design.txt            : Plasmid design specification  
markers.tab           : Marker sequence dictionary  
plasmid_builder.py    : Main pipeline  
ori_finder.py         : ORI detection logic  
tests/                : Mandatory test cases  
Output.fa             : Generated plasmid DNA  

Execution
python plasmid_builder.py Input.fa Design.txt markers.tab Output.fa
