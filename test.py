import torch
from timesformer.models.vit import TimeSformer
from tools.train_net import train

model = TimeSformer(img_size=224, num_classes=400, num_frames=8, attention_type='divided_space_time',  pretrained_model='TimeSformer_divST_8x32_224_K400.pyth')

dummy_video = torch.randn(2, 3, 8, 224, 224) # (batch x channels x frames x height x width)

pred = model(dummy_video,) # (2, 400)

print(pred.shape)

#from timesformer.dataset.kinetics import Kinetics


