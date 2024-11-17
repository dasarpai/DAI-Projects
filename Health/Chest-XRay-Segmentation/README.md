# Readme by Hari Thapliyal

## About Project & Dataset
- Segmentation of patch on x-ray. Segment neet to identify the effusion area.

**Montgomery County Chest X-ray Database (USA)**

Originates from the Montgomery County, Maryland Tuberculosis screening program. 
- Contains 58 TB-positive and 80 normal X-ray images.
- Shenzhen Chest X-ray Database (China)

Collected from out-patient clinics in Shenzhen, Guangdong Province.   
Includes 336 TB-positive and 326 normal X-ray images.

## Technology Used 
- U-Net Architecutre, Tensorlfow, Kaggle Dataset downloader, pandas,  matplotli, seaborn, scikit-learn, 
- 20 ephoc 
- Trainable params: 7,701,825

```
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy',dice_coefficient,jaccard_index])
			  
checkpoint = ModelCheckpoint(
    'best_model.keras',            # Path to save the model
    monitor='val_dice_coefficient',         # Metric to monitor
    verbose=1,                  # Print messages when saving the model
    save_best_only=True,        # Save only the best model (with highest metric)
    mode='max',                 # 'max' means the model with the highest metric score will be saved
    save_weights_only=False,     # Save the entire model (not just weights)
)


policy = tf.keras.mixed_precision.Policy('mixed_float16')
tf.keras.mixed_precision.set_global_policy(policy)

with tf.device('/GPU:0'): # Use the first GPU, if available.  Change to /GPU:1 etc. for other GPUs.
    history = model.fit(
        train_data,
        validation_data=val_data,
        epochs=20,
        batch_size=4,
        callbacks=[checkpoint],
        # workers=4, # Number of worker processes for data loading
        # use_multiprocessing=True # Enable multiprocessing for data loading
    )
```

## Results 
	- accuracy: 0.9824 
	- dice_coefficient: 0.9497 
	- jaccard_index: 0.9044 
	- loss: 0.0451 
	- val_accuracy: 0.9324 
	- val_dice_coefficient: 0.8319 
	- val_jaccard_index: 0.7186 
	
## Steps to train to this model on Colab using local GPU machine

- WSL
- jupyter-notebook --no-browser --port=8888 --ip=0.0.0.0
	- It will create one url along with token
- Create a new notebook in colab OR Use this notebook available at github in colab
- Notebook: Lungs_Segmentation_using_U_Net_Architecture.ipynb
- Use the earlier generated url and token to connect as local server
-  watch -n 1 nvidia-smi (check whether GPU is being used)