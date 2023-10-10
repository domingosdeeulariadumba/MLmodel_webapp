# Deploying a ML model using Gradio
  This project aims to present an alternative to deploy a ML model using Gradio

# What is Gradio?
  According to their officioal webpage, "Gradio is the fastest way to demo your machine learning model with a friendly web interface so that anyone can use it, anywhere!"

# Prerequisites
  1. Knowledge about how to train, fit and save a model
  2. Set your python environment
     
# How to deploy a model using Gradio?
  1. Install Gradio
  ![image](https://github.com/domingosdeeulariadumba/MLmodel_webapp/assets/110714056/61adbf4e-bf54-4e94-bbd1-b978bee9f99b)
  
  2. Import the required libraries (assuming you have already saved your model using Joblib)
  ![image](https://github.com/domingosdeeulariadumba/MLmodel_webapp/assets/110714056/8f42227e-af0b-4b85-bb9b-1aba5cc751b3)
    
  3. Creating a function by which Gradio will present the predicted price
  ![image](https://github.com/domingosdeeulariadumba/MLmodel_webapp/assets/110714056/95b963ac-6fd7-4db3-a582-32161871a43e)
  
  You can find this model here: https://github.com/domingosdeeulariadumba/LaptopPriceAnalysis
  
  4. Setting up the entries
  ![image](https://github.com/domingosdeeulariadumba/MLmodel_webapp/assets/110714056/27b9c876-60b0-4dfb-88fc-6ac1a74d618d)
  
  The term 'label' represents the component or the message that will be displayed. We set 'Number' for numeric entries and 'Textbox' to pass non numeric inputs

  5. Defining the output
  ![image](https://github.com/domingosdeeulariadumba/MLmodel_webapp/assets/110714056/c73c4139-292b-43e9-ad77-cf42d47bcb04)
  
  As the goal of this project was to predict laptop prices, we set the price as the outcome.

  6. Defining the interface entries
   ![image](https://github.com/domingosdeeulariadumba/MLmodel_webapp/assets/110714056/d92aa844-3545-4a41-9f26-d1b6384d70a4)
  
  The 'fn' is a function of the Interface class used "to wrap an interface around. Often a machine learning model's prediction function. Each parameter of the function corresponds to      one input component, and      the function should return a single value or a tuple of values, with each element in the tuple corresponding to one output component." We then iclude
  the inputs and the output defined in the steps 4 and 5.

  7. Deploying the model
  ![image](https://github.com/domingosdeeulariadumba/MLmodel_webapp/assets/110714056/1f050ab2-0027-49e3-8729-6a0999ce5d9f)
  
  And finally we launch the model. At this point, all we can do is copy the url and check how it looks like.

# References
  1. How to Deploy a Machine Learning Model as a Web App Using Gradio. Ibrahim Abayomi Ogunbiyi. https://www.freecodecamp.org/news/how-to-deploy-your-machine-learning-model-as-a-web-app-using-gradio/

  2. Build & Share Delightful Machine Learning Apps. Gradio. https://www.gradio.app/docs/interface


