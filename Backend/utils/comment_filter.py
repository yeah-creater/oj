import requests

API_URL = "https://api-inference.huggingface.co/models/thu-coai/roberta-base-cold"
headers = {"Authorization": "Bearer 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"}


def query(comment):
    try:
        response = requests.post(API_URL, headers=headers, json={'inputs':comment})
        if response.json()[0][0]['label'] == 'LABEL_0':
            return True
        return False
    except:
        return True


