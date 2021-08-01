#                                                                HydroSafe Project 
------------------
## Contents

- [Hydrosafe](#Hydrosafe)
  - [Contents](#contents)
  - [Short description](#short-description)
    - [The Problem](#The-Problem)
    - [How can technology help?](#How-can-technology-helps-in-solving-this-problem?)
    - [The idea](##The-Idea)
    - [General Objective](##General-Objective)
    - [Specific Objectives](##Specific-Objectives)
  - [Demo video](##Demo-video)
  - [The Project Architecture](##Project-Architecture)
  - [Long description](#long-description)
  
  - [Getting started](##Getting-started)
  - [Live demo](#Live-Demo)
  - [Built with](#built-with)
  
  - [Authors](#authors)
# The Problem
There has been an increase in deaths  every year due to unsafe water consumption. Globally, in efforts to address the clean water and sanitation problem, various governments and NGOs have initiated various strategies to curb the deaths that result from consumption of unsafe water. According to the World Health Organization (WHO) contaminated drinking-water is estimated to cause 502000 diarrhoeal deaths each year (Water, n.d.-b). With the rapid growth in population and increased human activities on land globally, which leads to water pollution,. Studies have shown that by 2025, half of the world's population will not have clean water and have poor sanitation. To bridge this gap, we propose a ‘Hydrosafe’ project to solve the issue of microorganisms and dirt in water by identifying the specific contaminant and giving specific solutions to the problem identified. This may not eradicate the problem fully but it will help reduce consumption of unsafe water and hence reduce death rates too.


# How can technology helps in solving this problem?
Using Deep Learning Techniques of Computer Vision to solve water safety problems.

## The Idea
We propose a ‘Hydrosafe’ project to solve the issue of microorganisms and dirt in water by identifying the specific contaminant and giving specific solutions to the problem identified. Cameras of Smartphones are used to take photos of water and the proposed idea detects whether the water is safe for drinking. This may not eradicate the problem fully but it will help reduce consumption of unsafe water and hence reduce death rates too.


## General Objective
To develop an AI-based Application that will be used to detect impurities in water.


## Specific Objectives
1. Detecting harmful bacterias in water.
2. Determine contaminants in water.
3. Analyze the level of contaminants in water  based on exploratory methods.
4. To build a real world mobile-based application that predicts the level of bacteria and water contamination. 

## Demo video

[![Watch the video](https://user-images.githubusercontent.com/55980747/127390084-3e92e0ca-f270-4edc-838c-bcd88e4ac96a.jpeg)](https://youtu.be/TcLq8W20Aho)
<!-------------<img src="https://user-images.githubusercontent.com/55980747/127390084-3e92e0ca-f270-4edc-838c-bcd88e4ac96a.jpeg" width=300 style="border-radius:50%" /> ---------------->


## Project Architecture

<img src="https://user-images.githubusercontent.com/41194018/127502511-d4f8ee6d-2e7f-405b-94d4-4d186833d66f.png" width=850 style="border-radius:50%" />

##### Data
We collected prinary kenyan data images named (kenyan_data)for our model and also Secondary Data Named (turbid) in call-for-code repository


## Long Description 


[link](https://docs.google.com/document/d/1Oq-cgygnQshRx_rxzZh7A2tjQ6XSDTwbWCza21_zOr0/edit?usp=sharing)
## Getting started
### This is the way to execute the code
#### Method 1. Using Python 3.8.5 on Terminal
------
- Clone the project i.e. 
```
git clone https://github.com/The-HydroSafers/Call-for-code
```
- Navigate to the directory "Call-for-code".
- Run the following commands in a systematic manner.
- Step 1
```
python load_data.py
```
- Step 2
```
python data_preprocess.py
```
- Step 3
```
python model.py
```
- Step 4
```
python train.py
```
- Step 5
```
python predict.py
```
- Step 6
```
python evaluate.py
```

#### Method 2. Navigate to IBM site
------
Click this [link](https://dataplatform.cloud.ibm.com/analytics/notebooks/v2/46a6f195-79e3-47b3-ac01-53cfb12b5126/view?projectid=7119d3cc-4cea-4fe7-b2bb-7a5601d7bccc&context=cpdaas) and run the code online. 

#### Method 3. Using Google Colaboratory
-------
Download the data from the repository and save it to your google drive.

Go to this [link](https://colab.research.google.com/drive/1WUw4zE4iixV_P_BDIK9poit6sD3nKTts?usp=sharing) and run the code.

# Live Demo


## Built with

- [IBM Watson Studio](https://www.ibm.com/cloud/watson-studio) -Ibm Watson Cloud pack for Data
- [Flask](https://flask.palletsprojects.com) -Flask Web Framework

- [Flutter](https://www.flutter.com/) -Flutter for App Development
- [Web Development](https://www./) -Follow the LInk to view the website

## Source Code

[Source Code-Ibm Cloud](https://dataplatform.cloud.ibm.com/analytics/notebooks/v2/46a6f195-79e3-47b3-ac01-53cfb12b5126/view?projectid=7119d3cc-4cea-4fe7-b2bb-7a5601d7bccc&context=cpdaas).


[Source Code-Google Colaboratory](https://colab.research.google.com/drive/1WUw4zE4iixV_P_BDIK9poit6sD3nKTts?usp=sharing).



## Flutter Appication 
About Flutter application is still underdevelopment ,we will be updating our repository to cater the missing flutter code.We decided to use  Web Application first to depoly our model.

## Web Application
 #### Frontend
we built our web application using Hyper Text Markup Language (HTML 5) , Cascading Style sheet (CSS) ,Javascript and Bootstrap FrameWork.
#### Backened 
 We used Python language where made use of Python Framework Flask.So far we are only classifying if the water is clean or not.
 we highly recommend use of high quality image to test the model.But in future we will make use lenses in our Flutter Application.
Here is the link [Link to preview the Website](https://the-hydrosafers.github.io/Web-Application/templates/index.html)
 
## Running the web application
- Clone the project i.e. 
```
git clone https://github.com/The-HydroSafers/Web-Application
```
- Navigate to the directory "Web-Application".
- Run the following commands in a systematic manner.
- Step 1
```
python model.py
 to generate model to be used in  the appliication
 ```
- Step 2
```
python index.py
 This is used to run our application
 ```



## Future of our Project
If our solution will be deployed it will help alot of people in knowing the water to drink and hence reduce  diseases which are water borne.This might help reduce the fatalities caused by drinking unsafe water.




## Authors

<a href="https://github.com/The-HydroSafers/Call-for-code/graphs/contributors">
 <img src="https://avatars.githubusercontent.com/u/55980747?v=4" width=100 style="border-radius:50%"/>
  <img src="https://avatars.githubusercontent.com/u/60429026?v=4" width=100 style="border-radius:50%"/>
  <img src="https://avatars.githubusercontent.com/u/41194018?v=4" width=100 style="border-radius:50%"/>
 <img src="https://avatars.githubusercontent.com/u/87578910?v=4" width=100 style="border-radius:50%"/>
  <img src="https://avatars.githubusercontent.com/u/87808828?v=4" width=100 style="border-radius:50%"/>
</a>

