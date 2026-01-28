import sys
from ori_finder import find_ori

def read_fasta(file):
    seq = ""
    with open(file) as f:
        for line in f:
            if not line.startswith(">"):
                seq += line.strip().upper()
    return seq

def read_design(file):
    mcs = []
    markers = []
    with open(file) as f:
        for line in f:
            if "," not in line:
                continue
            key, value = line.strip().split(",", 1)
            key = key.lower()
            value = value.strip()
            if "site" in key:
                mcs.append(value)
            else:
                markers.append(value)
    return mcs, markers

def read_markers(file):
    marker_dict = {}
    with open(file) as f:
        for line in f:
            if line.strip():
                k, v = line.strip().split("\t")
                marker_dict[k] = v
    return marker_dict

RESTRICTION_SITES = {
    "EcoRI": "GAATTC",
    "BamHI": "GGATCC",
    "HindIII": "AAGCTT",
    "PstI": "CTGCAG",
    "SmaI": "CCCGGG",
    "SalI": "GTCGAC",
    "XbaI": "TCTAGA",
    "KpnI": "GGTACC",
    "SacI": "GAGCTC",
    "SphI": "GCATGC"
}

def build_plasmid(input_fa, design_txt, markers_tab, output_fa):
    genome = read_fasta(input_fa)

    # Finding organism-specific ORI
    ori = find_ori(genome)

    # Reading design and marker dictionary
    mcs_list, marker_list = read_design(design_txt)
    marker_db = read_markers(markers_tab)

    plasmid = ori

    # Adding markers safely
    for marker in marker_list:
        if marker in marker_db:
            plasmid += marker_db[marker]

    # Removing restriction sites as per design
    for enzyme in mcs_list:
        if enzyme in RESTRICTION_SITES:
            plasmid = plasmid.replace(RESTRICTION_SITES[enzyme], "")

    # Writing output FASTA
    with open(output_fa, "w") as f:
        f.write(">Designed_Plasmid\n")
        for i in range(0, len(plasmid), 60):
            f.write(plasmid[i:i+60] + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python plasmid_builder.py Input.fa Design.txt markers.tab Output.fa")
        sys.exit(1)

    build_plasmid(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
