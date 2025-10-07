--- Dockerfile ---
FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-runtime
RUN apt-get update && apt-get install -y ffmpeg libsndfile1
WORKDIR /workspace
COPY . /workspace
RUN pip install -r <(python - <<'PY'
print("\n".join([
"transformers",
"librosa",
"numpy",
"scipy",
"pandas",
"scikit-learn",
"matplotlib",
"seaborn",
"opencv-python",
"tensorboard",
"wandb",
"soundfile",
"tqdm",
"dlib",
"face-alignment"
]))
PY)
