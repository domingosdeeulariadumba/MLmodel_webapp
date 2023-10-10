# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:35:41 2023

@author: domingosdeeulariadumba
"""

import gradio as gd
import joblib


def greet_user(name):
	return "Hello " + name + " Welcome to Gradio!😎"


webapp =  gd.Interface(fn = greet_user, inputs = "text", outputs = 'number')
webapp.launch(share = True)


def estimate(Brand, Product, ProcessorType, ProcessorCore,
                      ProcessorGen, RAM, Opsys, HDD_Storage,
                      SSD_Storage, Display, Warranty, Rating):
    
        model=joblib.load("LaptopPriceModel2.sav")

        outcome = model.predict([[Brand, Product, ProcessorType, ProcessorCore,
                              ProcessorGen, RAM, Opsys, HDD_Storage,
                              SSD_Storage, Display, Warranty, Rating]])
        return outcome



#Create the input component for Gradio since we are expecting 4 inputs

brand_input = gd.Textbox(label = "Enter the brand of the laptop")
product_input = gd.Textbox(label = "Enter the product type")
processortype_input = gd.Textbox(label = "Enter the processor type")
processorcore_input = gd.Textbox(label = "Enter the processor core")
processorgen_input = gd.Textbox(label = "Enter the processor generation")
ram_input = gd.Number(label = "Enter the RAM")
opsys_input = gd.Textbox(label = "Enter the Operating System")
hddstorage_input = gd.Number(label = "Enter the HDD Storage")
ssdstorage_input = gd.Number(label = "Enter the SSD Storage")
display_input = gd.Textbox(label = "Enter the SSD Storage")
warranty_input = gd.Textbox(label = "Enter the Warranty")
rating_input = gd.Number(label = "Enter the Rating")




# We create the output
Price = gd.Number()


webapp = gd.Interface(fn = estimate, inputs = [brand_input, product_input,
                                            processortype_input, 
                                            processorcore_input, 
                                            processorgen_input, ram_input, 
                                            opsys_input, hddstorage_input, 
                                            ssdstorage_input, display_input, 
                                            warranty_input, rating_input], outputs = Price)

webapp.launch(share = 'True')

