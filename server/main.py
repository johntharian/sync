from fastapi import FastAPI,File,UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os 
import subprocess
from moviepy.editor import VideoFileClip
import wave


app=FastAPI()

origins=[
    "https://main.d1o0lycmm6b9m1.amplifyapp.com",
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# class VideoFile(BaseModel):
#     filename: str
#     content_type: str
#     file: bytes

def  get_video_duration(video_path):
    video_c=VideoFileClip(video_path)
    return video_c.duration

def get_audio_duration(audio_path):
    with wave.open(audio_path,"rb") as audio_file:
        audio_frames= audio_file.getnframes()
        frame_rate=audio_file.getframerate()
        audio_duration=  audio_frames / float(frame_rate)
        return audio_duration
    
def duration_equal(video_duration,audio_duration):
    return int(video_duration) == int(audio_duration)

@app.get('/health')
async def check_health():
    return {"health":"200"}
 
@app.post('/')
async def upload_file(videof : UploadFile=File(...),audiof : UploadFile=File(...)):
    print(videof.content_type,audiof.content_type)
    if videof.content_type !=  'video/mp4' or audiof.content_type != 'audio/wave':
        return "Video or audio not supported"
    
    

    print(videof.filename, audiof.filename)
    print('received successfully')
    upload_dir = '/app/uploads'
    os.makedirs(upload_dir, exist_ok=True)
    # dir=os.getcwd()+ '\\' + upload_dir

    videof_path = os.path.join(upload_dir, videof.filename)
    audiof_path = os.path.join(upload_dir, audiof.filename)

    with open(videof_path, "wb") as f:
        f.write(await videof.read())

    with open(audiof_path, "wb") as f:
        f.write(await audiof.read())

    video_duration=get_video_duration(videof_path)
    audio_duration = get_audio_duration(audiof_path)

    print(video_duration, audio_duration)
    if not duration_equal(video_duration,audio_duration) :
        print("Durations do not match")
        return {"Durations":"Durations do not match"}

    else :
        

        # test
        # res_path = r"E:\sync\server\Wav2Lip\results\result_voice.mp4"
        # print('test')
        # return FileResponse(res_path)
        
    

        checkpoint_path = '/app/wav2lip.pth'

        command = f'cd /app/Wav2Lip && python inference.py --checkpoint_path "{checkpoint_path}" --face "{videof_path}" --audio "{audiof_path}"'

        try:
            # Run the shell command
            subprocess.run(command, shell=True, check=True)
            print("Wav2Lip inference completed successfully!")

            res_path = '/app/Wav2Lip/results/result_voice.mp4'

            if os.path.exists(res_path):
                print("sucess")
                # return video results
                return FileResponse(res_path)
                
        except subprocess.CalledProcessError as e:
            print(f"Error while running Wav2Lip inference: {e}")

        
        return {videof.filename, audiof.content_type}