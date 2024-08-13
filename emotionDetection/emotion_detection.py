import requests
import json

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    input_json = { "raw_document": { "text": text_to_analyze } } 

    response = requests.post(url,json=input_json,headers=Headers)

    formatted_response = response.text

    # from text to json/dictionary
    json_response = json.loads(formatted_response)

    req_emotions = json_response['emotionPredictions'][0]['emotion']

    # logic for finding the dominant emotion
    dominant_emotion=''
    dominant_value=0

    for (key,value) in req_emotions.items() : 
        if value > dominant_value:
            dominant_value=value
            dominant_emotion=key

    # print(dominant_value,dominant_emotion)
    req_emotions['dominant_emotion'] = dominant_emotion
    return (req_emotions)




# emotion_detector("I hate you")


