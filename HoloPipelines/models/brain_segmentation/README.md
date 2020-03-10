# Load pre-trained weights
To run this model the pre-trained weights have to be placed into a directory called *saved_model*.
The weights can be found [here](https://github.com/miguel-dgist/mrbrains18).

# Uploading files
To use the server two directories for the prediction and uploaded files have to be created. The directories should be named *data* for uploads and *prediction* for the segmentation.

# Testing the flask server
Run the flask server:
```bash
python server.py
```

Once the server is up and running, the following command can be used to check if everything is working fine.
We post the three required input files against the server and save the output in a file called *segmentation.nii.gz*.
```bash
curl -F "files[]=@FLAIR.nii.gz" -F "files[]=@T1.nii.gz" -F "files[]=@IR.nii.gz" localhost:5000/model -o segmentation.nii.gz
```