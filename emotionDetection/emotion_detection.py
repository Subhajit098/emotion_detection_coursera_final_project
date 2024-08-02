import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = input_json, headers=header)
    formated_response = json.loads(response.text)

    if response.status_code == 200:
        # return formated_response
        extracted_emotion=formated_response['emotionPredictions'][0]['emotion']
        # return extracted_emotion

        dominant_emotion_value=0
        dominant_emotion='nothing'


        for key,value in extracted_emotion.items():
            if value > dominant_emotion_value : 
                dominant_emotion_value=value
                dominant_emotion=key


        extracted_emotion['dominant_emotion']=dominant_emotion

        return extracted_emotion

    elif response.status_code == 400:
        formated_response = {
                            'anger': None,
                            'disgust': None, 
                            'fear': None, 
                            'joy': None, 
                            'sadness': None, 
                            'dominant_emotion': None}
        return formated_response
