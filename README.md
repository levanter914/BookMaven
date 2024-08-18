# Project: ML Based Book Recommender System ! 


# BookMaven
![WhatsApp Image 2024-08-18 at 12 02 09 (3)](https://github.com/user-attachments/assets/2a36f188-f711-4f0f-9a4d-527d0e8156e8)

In the digital age, the sheer volume of available books can make it challenging for readers to discover titles that match their interests. A Book Recommendation System addresses this issue by leveraging machine learning techniques to analyze user preferences and suggest books that align with their tastes.

Our machine learning-based Book Recommendation System aims to provide personalized book suggestions by learning from user behavior, such as past ratings, reviews, and genre preferences. By utilizing advanced algorithms, this system not only enhances the reader's experience but also helps in uncovering hidden gems that might otherwise go unnoticed.


# Note:
If you want to understand this entire project overflow, please refer the jupyter notebook file inside notebook folder.

# Types of Recommendation System :

### 1 ) Content Based :

- Content-based systems, which use characteristic information and takes item attriubutes into consideration .

- Twitter , Youtube .

- Which music you are listening , what singer are you watching . Form embeddings for the features .
	
- User specific actions or similar items reccomendation .
	
- It will create a vector of it .
	
- These systems make recommendations using a user's item and profile features. They hypothesize that if a user was interested in an item in the past, they will once again be interested in it in the future
	
- One issue that arises is making obvious recommendations because of excessive specialization (user A is only interested in categories B, C, and D, and the system is not able to recommend items outside those categories, even though they could be interesting to them).
  

### 2 ) Hybrid Based :
	
- Hybrid systems, which combine both types of information with the aim of avoiding problems that are generated when working with just one kind.

- Combination of both and used now a days .

- Uses : word2vec , embedding .           

# About this project:

This is a collaborative filtering based books recommender system & a streamlit web application that can recommend various kinds of similar books based on an user interest.



# Demo:

https://github.com/user-attachments/assets/6b15e930-feb7-42bb-9473-58fe68d5c847



# Dataset has been used:

* [Dataset link](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset/data)
  ![WhatsApp Image 2024-08-18 at 12 02 09](https://github.com/user-attachments/assets/5a945076-d627-40ad-810d-1cbd00babe6e)

# Built With
1. streamlit
2. Machine learning
3. sklearn

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/ML-Based-Book-Recommender-System.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n books python=3.7.10 -y
```

```bash
conda activate books
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


Now run,
```bash
streamlit run app.py
```

```bash
Note: Before clicking on show recommendations first of all click on Train Recommender System for generating models
```

# How to run in Docker?

#### Build a Docker image
The docker build command builds an image from a Dockerfile . Run the following command from the app/ directory on your server to build the image:


```bash
docker build -t streamlit .
```

The -t flag is used to tag the image. Here, we have tagged the image streamlit. If you run:

```bash
docker images
```
You should see a streamlit image under the REPOSITORY column. For example:

```bash
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
streamlit    latest    70b0759a094d   About a minute ago   1.02GB
```

#### Run the Docker container
Now that you have built the image, you can run the container by executing:

```bash
docker run -p 8501:8501 streamlit
```

The -p flag publishes the container’s port 8501 to your server’s 8501 port.

If all went well, you should see an output similar to the following:

```bash
$ docker run -p 8501:8501 streamlit

  You can now view your Streamlit app in your browser.

  URL: http://127.0.0.1:8501/
```

To view your app, users can browse to http://0.0.0.0:8501 or http://127.0.0.1:8501/




