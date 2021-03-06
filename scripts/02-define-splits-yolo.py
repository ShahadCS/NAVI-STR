import os

labels_path = './PyTorch-YOLOv3/data/sevn/labels/'
path = "./data/sevn/images/"
custom_path = "./PyTorch-YOLOv3/data/sevn/"

total_frames = len(os.listdir(labels_path))
frames = [path.split('.')[0] for path in os.listdir(labels_path)]
train = frames[:int(total_frames * .8)]
test = frames[int(total_frames * .8):]

with open(f'{custom_path}train.txt', 'w') as f:
    for frame in train:
        f.write(f"{path}{frame}.png\n")
f.close()
with open(f'{custom_path}valid.txt', 'w') as f:
    for frame in test:
        f.write(f"{path}{frame}.png\n")

# from shutil import copyfile
# from tqdm import tqdm

# for frame in tqdm(test, desc='Copying test set:'):
#     copyfile(f"{path}{frame}.png", f"{custom_path}test/{frame}.png")

