
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


apikey = 'kfCgPMzqfXHOYCQDCC4cpQ--g5ajzGCFIEGPRIFuouFO'
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/8a6f0a7c-c01e-4697-b935-e5d8e0de840f'

authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)


with open('results.txt', 'r') as f:
    text = f.readlines()
    text = [line.replace('\n', '') for line in text]
    text = ''.join(str(line) for line in text)


with open('./audioFromResults.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
    audio_file.write(res.content)