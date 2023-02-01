from tkinter import *
import requests
import json

root=Tk()
root.title("Country API")
root.geometry("700x600")
root.configure(background = "blue")

lbl = Label(root, text = "Capital City Name", font = ("Helvetica", 18, "bold"), fg = "white", bg = "blue")
lbl.place(relx = 0.1, rely = 0.1, anchor = W)

entry = Entry(root)
entry.place(relx = 0.1, rely = 0.3, anchor = W)

btn = Button(root, text = "City Details", relief = FLAT, command = city_details, bg = "yellow", fg = "black")
btn.place(relx = 0.3, rely = 0.3, anchor = W)

country_lbl = Label(root, text = "Country:", bg = "blue", fg = "white", font = ("bold", 10))
country_lbl.place(relx = 0.1, rely = 0.5, anchor = W)

region_lbl = Label(root, text = "Region:", bg = "blue", fg = "white", font = ("bold", 10))
region_lbl.place(relx = 0.1, rely = 0.6, anchor = W)

language_lbl = Label(root, text = "Language:", bg = "blue", fg = "white", font = ("bold", 10))
language_lbl.place(relx = 0.1, rely = 0.7, anchor = W)

population_lbl = Label(root, text = "Population:", bg = "blue", fg = "white", font = ("bold", 10))
population_lbl.place(relx = 0.1, rely = 0.8, anchor = W)

area_lbl = Label(root, text = "Area:", bg = "blue", fg = "white", font = ("bold", 10))
area_lbl.place(relx = 0.1, rely = 0.9, anchor = W)

def city_details():
    api_request = requests.get("https://restcountries.com/v2/capital/" + entry.get())
    api_output_json = json.loads(api_request.content)
    
    country = api_output_json[0]["name"]
    print(country)
    
    region = api_output_json[0]["region"]
    print(region)
    
    language = api_output_json[0]["languages"]
    print(language)
    
    population = api_output_json[0]["population"]
    print(population)
    
    area = api_output_json[0]["area"]
    print(area)
    
    country_lbl["text"] = "Country : " + str(country)
    
    region_lbl["text"] = "Region : " + str(region)
    
    language_lbl["text"] = "Language : " + str(language)
    
    population_lbl["text"] = "Population : " + str(population)
    
    area_lbl["text"] = "Area : " + str(area)
    
root.mainloop()