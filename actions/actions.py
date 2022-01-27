# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List, Laws
# from matplotlib.pyplot import text
# import requests
# import xml.etree.ElementTree as ET
# import csv
from rasa_sdk.events import EventType
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Esta ley regula el regimen de responsabilidad aplicable en los casos de robo")

        return []

# class AskLaws1(Action):
#     def name(seft) -> Text:
#         return "action_ask_laws"
    
#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         if tracker.get_slot("Articulo1"):
#             dispatcher.utter_message(
#                 text=f"Esta ley regula el régimen de responsabilidad aplicable en los casos de extravío, hurto, robo o fraude de tarjetas de crédito, tarjetas de débito, tarjetas de pago con provisión de fondos, o cualquier otro sistema similar"
#             )
#         return []


# # 

# class actionasklaws(Action):
#     def name(self) -> Text:
#         return "action_ask_laws"

#     def run(self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]
#         ) -> List[Dict[Text, Any]]:
#         # get the location slot
#         ley = tracker.get_slot('ley')
#         # read the CSV file
#         with open('Profesor/articulos', 'r', encoding = "utf-8") as file:
#             reader = csv.DictReader(file)
#             # get a list of universities in the desired location
#             output = [row for row in reader if row['Articulo'] == ley]
#         if output: 
#             reply  = f"Descripcion del articulo {ley}:"
#             reply += "".join([item['Descripcion'] for item in output])
            
#             dispatcher.utter_message(reply)
#         else: 
#             dispatcher.utter_message(f"No se encontró el articulo {ley}")



# class ActionLaws(Action):

#     def name(self) -> Text:
#         return "action_ask_laws" 

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         la=tracker.latest_message('ley')
#         norma= int(Laws(la)['norma'])
#         dispatcher.utter_tamplate("utter_laws",tracker, norma=norma)
#         return []

#     def Laws(ley): 
#         api_address='https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma='

#         url = api_address + ley 
#         print(url.content)
#         xmlDict = {}
#         root = ET.fromstring(url.content)
#         for child in root.iter('*'):
#             print(child.tag)
#         for sitemap in root:
#             children = sitemap.getchildren()
#             xmlDict[children[0].text] = children[1].text
#         print(xmlDict)
#         return xmlDict

    

    
