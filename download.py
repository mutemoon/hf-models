import os

# 从环境变量获取模型名称，如果没有设置则使用默认值
model_name = os.getenv('MODEL_NAME', 'THUDM/chatglm3-6b-32k')

# 下载模型
from huggingface_hub import snapshot_download
snapshot_download(model_name)

# Download from a dataset
# from huggingface_hub import snapshot_download
# snapshot_download(repo_id="bigcode/starcoderdata", repo_type="dataset", allow_patterns=["git-commits-cleaned/train-00000-of-00055.parquet", "github-issues-filtered-structured/train-00000-of-00059.parquet"])
# snapshot_download(repo_id="OpenAssistant/oasst1", repo_type="dataset")

# See more at https://huggingface.co/docs/huggingface_hub/en/guides/download