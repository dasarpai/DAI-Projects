This model was run into colab using wsl/docker using image tensorflow/tensorflow:latest-gpu-jupyter

# How to run the jupyter server from docker image?
docker run --gpus all -d -it -p 8888:8888 -v /mnt/d/github/2-Solutions/Buransh:/home/project my-tf-jupyter jupyter notebook --ip=0.0.0.0 --allow-root

# where kaggle related files are save?
Actually this kernel was orgianlly available on kaggle. when I saved and run into colab. It created temp files during image download into 54a8b1ca9c7f:/input. Earlier part is container id.

# To copy from a docker container onto host machine's wsl env.
docker cp 54a8b1ca9c7f:/input/chest-xray-pneumonia/chest_xray/train/NORMAL/NORMAL2-IM-0966-0001.jpeg /mnt/d/github/2-Solutions/

# Process followed
- To train the model data is downloaded from kaggle datasets
- torchvision, scikit-image, torch, libraries were installed on docker image tensorflow/tensorflow:latest-gpu-jupyter. For this we need to download the docker image, run the container with volume attached, jupyter notebook attached, port attached, etc. After jupyter server is created then within the jupyter notebook cells I downloaed these packages.
- vgg16 model architecture was model_pre = models.vgg16(). from torchvision import datasets, models, transforms
- Pre_trained weights were loaded: model_pre.load_state_dict(torch.load("../input/pytorch-pretrained-models/vgg16-397923af.pth"))
- Model moved to gpu : model_pre = model_pre.to(device)
- parameters need to model training: 
    - criterion = nn.CrossEntropyLoss()
    - optimizer = optim.SGD(model_pre.parameters(), lr=0.001, momentum=0.9, weight_decay=0.01)
    - # Decay LR by a factor of 0.1 every 10 epochs
    - exp_lr_scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)
- training function was created: train_model(model, criterion, optimizer, scheduler, num_epochs=25)
    - this function logs metrics, to plot later.
    - saves the best model using callback. Used model accuracy to evalute the model
    - Test accuracy is 80%
    - Recall: 0.9974358974358974
    - Precision: 0.759765625
    - F1: 0.8625277161862528
- Confusion Metrix:

```
from sklearn import metrics
metrics.confusion_matrix(true_labels1,pred_labels1)

array([[111, 123],
       [  1, 389]])

```