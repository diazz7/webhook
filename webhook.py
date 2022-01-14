import requests
import json

webhook_url = 'https://webhook.site/51cb2cf5-8b41-49df-9920-a02365adbc95'

data = { 'Version': 1,
         'TransformerName': 'ESIP_MediationEngine',
         'Agent': 'PROD',
         'EventSeverity': 5,
         'EventCategory': 4,
         'Timestamp': '2021.09.10 09:15:15',
         'Platform': 'SIPCore',
         'NodeName': '0123456789',
         'ProblemText': '',
         'ObjectName': '',
         'EventText': 'Pivot alert %title%',
         'CircuitId': '',
         'CircuitCode': '',
         'Url': '',
         'EventCat1': 'VoIP',
         'EventCat2': 'SIPCore',
         'EventCat3': 'ESIP',
         'EventLifeTime': '',
         'ObjectAddOn': '',
         'OnDuty': 'Please contact +41791111111'}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

