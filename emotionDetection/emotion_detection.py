import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    try : 
        response = requests.post(URL, json = input_json, headers=header)
        formated_response = json.loads(response.text)

        response.raise_for_status() 
        # raise an HTTP error for bad responses(4xx and 5xx)

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

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except KeyError as key_err:
        print(f"Key error: {key_err}, response content: {response.text}")
    except json.JSONDecodeError as json_err:
        print(f"JSON decode error: {json_err}, response content: {response.text}")
    
    # Return a default structure in case of error
    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }


    