from tkinter import *
import random
root = Tk()
root.geometry("500x500")
root.configure(background = 'cyan')
root.title("Country Capitals")

#inputs
country_name = Entry(root)
country_name.place(relx = 0.5, rely = 0.2, anchor = CENTER)


city_name = Entry(root)
city_name.place(relx = 0.5, rely = 0.3, anchor = CENTER)

#labels
country_list_label = Label(root)
country_list_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

random_country = Label(root)
random_country.place(relx = 0.5, rely = 0.8, anchor = CENTER)


city_list_label = Label(root)
city_list_label.place(relx = 0.5, rely = 0.6, anchor = CENTER)

random_city = Label(root)
random_city.place(relx = 0.5, rely = 0.9, anchor = CENTER)

country_list = []
city_list = []

def show_name():
    # country
    country = country_name.get()
    country_list.append(country)
    country_list_label["text"] = "Country Name: " + str(country_list)
    
    
    #city 
    city = city_name.get()
    city_list.append(city)
    city_list_label["text"] = "City Name: " + str(city_list)
    
    
def random_show_name():    
    #country
    length_country = len(country_list)
    random_no_country = random.randint(1, length_country)
    generated_no_country = country_list[random_no_country - 1]
    random_country["text"] = "Random Country is: " + str(generated_no_country)
    
    #city
    length_city = len(city_list)
    random_no_city = random.randint(1, length_city)
    generated_no_city = city_list[random_no_city - 1]
    random_city["text"] = "Random City is: " + str(generated_no_city)

btn1 = Button(root, text = "Display Country and City Name", command = show_name, bg = 'gold')
btn1.place(relx = 0.5, rely = 0.4, anchor = CENTER)

btn2 = Button(root, text = "Display Country and City Name Randomly", command = random_show_name, bg = 'gold')
btn2.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()

