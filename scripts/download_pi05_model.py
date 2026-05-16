from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="lerobot/pi05_libero_base",
    repo_type="model",
    local_dir=r"E:\Robotics\Lerobot\models\pi05_libero_base",
)

print("Downloaded pi05_libero_base")
