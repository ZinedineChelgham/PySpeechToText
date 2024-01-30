from google.cloud import speech 

client = speech.SpeechClient.from_service_account_file('transcription-google-key.json')

file_name = "audio.mp3"

with open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    
audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.MP3,
    sample_rate_hertz=16000,
    language_code="en-US",
)

response = client.recognize(config=config, audio=audio)


print("Transcript: {}".format(response.results[0].alternatives[0].transcript))
