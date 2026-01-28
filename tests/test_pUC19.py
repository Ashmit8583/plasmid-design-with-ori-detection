import subprocess

def test_puc19():
    subprocess.run([
        "python",
        "plasmid_builder.py",
        "tests/pUC19.fa",
        "tests/Design_pUC19.txt",
        "markers.tab",
        "Output.fa"
    ], check=True)

    with open("Output.fa") as f:
        data = f.read()
        assert "GAATTC" not in data
