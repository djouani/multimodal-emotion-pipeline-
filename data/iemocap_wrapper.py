--- data/iemocap_wrapper.py ---
--- (Parses IEMOCAP to manifests; simplified)
import os, json
from pathlib import Path

def build_iemocap_manifest(root, out_manifest, label_map=None):
    root = Path(root)
    items=[]
    # naive scan: look for wav files under Session*/sentences/wav or dialog
    for wav in root.rglob('*.wav'):
        # infer session and utterance id; user should customize mapping
        # expects accompanying label mapping file per dataset
        rel = wav.relative_to(root)
        items.append({'wav': str(wav), 'feat': '', 'label': 0})
    with open(out_manifest,'w') as f:
        json.dump(items, f, indent=2)

if __name__ == '__main__':
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument('--root', required=True)
    p.add_argument('--out', required=True)
    args=p.parse_args()
    build_iemocap_manifest(args.root, args.out)
