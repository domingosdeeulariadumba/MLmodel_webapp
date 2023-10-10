# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:35:41 2023

@author: domingosdeeulariadumba
"""

# Importing libraries

import gradio as gd
import joblib


# Creating a function by which Gradio will present the predicted price

def estimate(Brand, Product, ProcessorType, ProcessorCore,
                      ProcessorGen, RAM, Opsys, HDD_Storage,
                      SSD_Storage, Display, Warranty, Rating):
    
        model=joblib.load("LaptopPriceModel2.sav")

        outcome = model.predict([[Brand, Product, ProcessorType, ProcessorCore,
                              ProcessorGen, RAM, Opsys, HDD_Storage,
                              SSD_Storage, Display, Warranty, Rating]])
        return outcome



# Creating inputs for Gradio iterface

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


# Defining the output
Price = gd.Number()


# setting up the web app entries

webapp = gd.Interface(fn = estimate, inputs = [brand_input, product_input,
                                            processortype_input, 
                                            processorcore_input, 
                                            processorgen_input, ram_input, 
                                            opsys_input, hddstorage_input, 
                                            ssdstorage_input, display_input, 
                                            warranty_input, rating_input], outputs = Price)

# Deploying the model
webapp.launch(share = 'True')

________________________________________________________END____________________________________________________________________________

