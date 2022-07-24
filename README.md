# Object State Change Classification

This is the imlementation of submission called ``TarHeels" for the [Ego4D: Object State Change Classification Challenge](https://ego4d-data.org/docs/challenge/) at [1st Ego4D Workshop, CVPR 2022](https://sites.google.com/view/cvpr2022w-ego4d-epic/). We use a transformer-based video recognition model and leverage the [Divided Space-Time Attention mechanism](https://arxiv.org/abs/2102.05095) for classifying object state change in egocentric videos. Our submission achieves the second-best performance in the challenge.

# Steps to run the codebase

- Follow the instruction from [timeSformer](https://github.com/facebookresearch/TimeSformer) for setup and installation.
- Run `create_fho_clips.py` for processing and creating video clips.
- Run `create_fho_dataset.py` for creating the dataset.
- Use following command to run the train the model.
 ```python
 python tools/run_net.py \
  --cfg configs/Ego4dFho/TimeSformer_divST_8x32_224.yaml \
  DATA.PATH_TO_DATA_DIR path_to_your_dataset \
  NUM_GPUS 8 \
  TRAIN.BATCH_SIZE 8 \
 ```
 - Finally, run `generate_submission.py` to generate submission file for the challenge.

