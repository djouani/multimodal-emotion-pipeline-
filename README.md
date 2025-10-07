# multimodal-emotion-pipeline-
--- README.md ---
Multimodal Emotion Recognition Pipeline

This repository implements a modular pipeline for multimodal emotion recognition (audio, video, text) with decision-level fusion and uncertainty-aware gating. Primary dataset: IEMOCAP. Optional: MSP-IMPROV, CREMA-D, MELD.

Quick start

Create environment: conda env create -f conda.yml conda activate multimodal-emotion
Place datasets under data/ as described in data/README_datasets.md
Preprocess: python src/preprocessing/audio_preprocess.py --root data/iemocap/wav --out data/feats/audio --manifest data/manifests/iemocap_audio.json python src/preprocessing/video_preprocess.py ...
Train: bash examples/run_audio.sh bash examples/run_video.sh bash examples/run_text.sh
Extract posteriors and train fusion: python src/inference/extract_posteriors.py --cfg configs/default_audio.yaml ... bash examples/run_fusion.sh
