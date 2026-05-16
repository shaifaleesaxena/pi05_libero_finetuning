from lerobot.datasets.lerobot_dataset import LeRobotDataset

ds = LeRobotDataset("HuggingFaceVLA/libero")

print("Dataset loaded")
print("Frames:", len(ds))
print("Features:")
print(ds.meta.features)

sample = ds[0]
print("Sample keys:", sample.keys())
print("State:", sample["observation.state"].shape)
print("Action:", sample["action"].shape)
print("Image:", sample["observation.images.image"].shape)
print("Image2:", sample["observation.images.image2"].shape)
