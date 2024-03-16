import json,os
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from variable import VERSION, URL, API_KEY,COLLECTION_ID, ENVIRONMENT_ID
authenticator = IAMAuthenticator(API_KEY)
discovery = DiscoveryV1(
    version=VERSION,
    authenticator=authenticator
)
#user_input1 = input("please enter crypto currency\n")
#user_input2 = input("please enter how many doc you want to see\n")
discovery.set_service_url(URL)
Query = discovery.query(
        ENVIRONMENT_ID,
        COLLECTION_ID,
        passages = True, 
        deduplicate= False,
        highlight= True,
        #passages_count= 5,
        #aggregation = f"filter(enriched_text.entities.text:{user_input1}).term(enriched_text.relevence.document.label,count:{user_input2})"
       natural_language_query = '10 most relevant document about bitcoin'


)
#print(json.dumps(Query.result, indent=2)[1])
#print(len(json.dumps(Query.result, indent=2)))
print((Query.result["results"][1]))
