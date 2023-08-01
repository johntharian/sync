# sync

# Getting Started 

Clone the repository 
### git clone https://github.com/johntharian/sync.git

## Setting up backend

#### cd sync
#### cd server
### git clone https://github.com/Rudrabha/Wav2Lip.git


#### wget "https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth" -O "Wav2Lip/face_detection/detection/sfd/s3fd.pth"

Create a virtual env using conda with python version==3.6

### conda create -n sync python=3.6

### conda activate sync

## Install the required libraries in the conda env


#### pip install librosa==0.7.0

#### pip install numpy==1.17.1

#### pip install opencv-contrib-python==4.2.0.34

#### pip install opencv-python==4.1.0.25

#### pip install torch===1.1.0 -f https://download.pytorch.org/whl/torch_stable.html

#### pip install torchvision==0.3.0

#### pip install tqdm==4.45.0

#### pip install numba==0.48

#### pip install resampy==0.3.1

These are required for running Wav2lip

### pip install -r requirements.txt

Replace [upload_dir](https://github.com/johntharian/sync/blob/ff6fb085aa2595bda3f65cffe6d0d8668a05abec/server/main.py#L58C32-L58C32) with the path to the directory you want to use for uploading files


Download the weights from [weights](https://iiitaphyd-my.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fradrabha%5Fm%5Fresearch%5Fiiit%5Fac%5Fin%2FDocuments%2FWav2Lip%5FModels%2Fwav2lip%2Epth&parent=%2Fpersonal%2Fradrabha%5Fm%5Fresearch%5Fiiit%5Fac%5Fin%2FDocuments%2FWav2Lip%5FModels&ga=1) and paste in the server directory

Modify the [command = f'cd /app/Wav2Lip && python inference.py --checkpoint_path "{checkpoint_path}" --face "{videof_path}" --audio "{audiof_path}"'](https://github.com/johntharian/sync/blob/ff6fb085aa2595bda3f65cffe6d0d8668a05abec/server/main.py#L91C8-L91C8) with the correct path to Wav2Lip 


The result will be stored at Wav2Lip/results/result_voice.mp4', so need to update [res_path](https://github.com/johntharian/sync/blob/ff6fb085aa2595bda3f65cffe6d0d8668a05abec/server/main.py#L98) with the correct path.
To start the server RUN ### uvicorn main:app --reload

## Setting up frontend

### cd client
### npm i

To start the app
### npm start
