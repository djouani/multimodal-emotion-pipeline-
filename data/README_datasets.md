--- data/README_datasets.md ---
Datasets and placement
IEMOCAP (requires registration): https://sail.usc.edu/iemocap/
Place extracted IEMOCAP under: data/iemocap/
Structure expected:
data/iemocap/Session1/sentences/wav/...
data/iemocap/Session1/dialog/EmoEvaluation/...
See data/iemocap_wrapper.py for parser.

MSP-IMPROV: https://www.eecs.qmul.ac.uk/~mdr/MPData/
CREMA-D: https://github.com/CheyneyComputerScience/CREMA-D
MELD: https://github.com/declare-lab/MELD
Place each corpus under data// with raw files. Wrapper scripts produce manifests.
