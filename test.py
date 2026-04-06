import streamlit as st
last_college = ""
 
def response_chatbot(user):
    global last_college 

    if "amity"in user:
        last_college="amity"
    elif "sharda" in user:
        last_college="sharda"
    elif "galgotias" in user:
        last_college="galgotias"
    

    if fees_words = {"cost","price","fees"} :
        if last_college ="amity":
           return "the fees of amity university: 1-2 lakh"
        elif last_college = "sharda":
           return " the fees of sharda university 1-1.2 lakh"
        elif last_college ="galgotias":
         return "the fees og galgotias 1-1.5 "
    
        else :
         return"ask me about amity, galgotias,sharda"
      

    elif placements_words = {"pakage","job","placements"} :
        if last_college ="amity":
           return "the placements of amity university: 3-4 LPA"
        elif last_college = "sharda":
           return " the placements of sharda university 2-5 LPA"
        elif last_college ="galgotias":
           return "the placements galgotias 2-3LPA "
    
        else :
         return"ask me about amity, galgotias,sharda"
      
    elif  "hi" in user or "hello" in user:
       return "ask me about colleges:"

    elif "bye" in user:
       return "goodbye!"  

      
      