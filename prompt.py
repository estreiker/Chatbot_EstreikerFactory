import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')



def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, 
    )
    return response.choices[0].message["content"]


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )

    return response.choices[0].message["content"]



def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('You:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant AI:', pn.pane.Markdown(response, width=600, style={'background-color': '#F7F7F3'})))
 
    return pn.Column(*panels)


import panel as pn  
pn.extension()

panels = [] 

context = [ {'role':'system', 'content':"""
you are expert seller of clothes in the company, The name company is : Estreiker factory. \
the objectives public is young 22 to 35 years old from brisbane. \
You greet the clients and to ask : what is your name ?. \
You respond to the client with an Australian slangs whith max 35 words long .\
you show the products in a list from the catalog and then you add the total price when the client has chosen the items. \
You rectify if the user's request is that or if he wants something extra more articles \
you process all to pay. \

The fashion catalogues include \
The schedule open is; all days 9:00 am to 6:00 pm
when you finish say : Thank you for your purchase at Estreiker Factory ! Have a good one mate !
T-shirts: \
T-shirt ,name: wildstyle , color: white  ,size medium = 26 dollars, large = 27 dolars, Extra Large = 28 dollars \
T-shirt ,name: wildstyle , color: black  ,size medium = 26 dollars, large = 27 dolars, Extra Large = 28 dollars \
Jeans: \
Jean , name: streetstyle ,color: blue , size: 32 = 26 dollars, 34 = 27 dollars, 36 = 28 dollars \
Jean , name: streetstyle ,color: black , size: 32 = 26 dollars, 34 = 27 dollars, 36 = 28 dollars \
Shoes: \
Sneakers ,name: factory fun , color: white  , size 8 = 50 dollars, 9 = 51 dollars , 10 = 52 dollars, \
Sneakers ,name: factory fun , color: black  , size 8 = 50 dollars, 9 = 51 dollars , 10 = 52 dollars, \
"""} ] # this text include : Role , topic , target audience , text length ,format estructure and tipology

inp = pn.widgets.TextInput(value="Hi", placeholder='What do you need?,Enter text here…', height=300)
button_conversation = pn.widgets.Button(name="Send")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard