FROM python:3-alpine

COPY TONEK_FILE TONEK_FILE
RUN pip install huggingface_hub
RUN cat TONEK_FILE | xargs huggingface-cli login --token

# 接收构建参数
ARG MODEL_NAME=THUDM/chatglm3-6b-32k
# 设置环境变量
ENV MODEL_NAME=$MODEL_NAME

COPY download.py .
RUN python download.py
RUN rm -f /root/.cache/huggingface/token && rm -f TONEK_FILE
