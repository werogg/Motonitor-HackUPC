<h1 align="center">
  Motonitor - HackUPC 2022
</h1>

<p align="center">This is a web user fronted software that lets the user calculate an estimated price of their motorbikes from home, letting them have a preview before starting contact with any agent, or selling it for a worse price. <br><br>This project makes the calculation based on a <b>Machine Learning System</b> that takes data from different motorbikes (previously extracted from second-hand motorbike online shops with our tool <a href="https://github.com/KuroHaka/motonitor-deep-scrapper">Motonitor-Deep-Scrapper</a>) and uses it to make a learning model that will predict with a pretty good accuracy (82% scored) an estimated price for the motorcycle.</p>

## ⚡️ Quick start

First, we need to [download](https://www.python.org/downloads/) python `3.9.2` or higher is required, and preferably a python3-venv enviroment to install all the required packages.  

> If you are using venv you can easily create a new enviroment with "python3 -m venv venv" (Inside project's folder). <br>
> Activate the python3-venv with "source venv/bin/activate"

Once you have your enviroment setted up and ready to work with python you need to install the requirements:

```bash
pip install -r requirements.txt
```

Now that we have already installed all the required packages we are going to start it:
```bash
./manage.py runserver
```

Now you can acces the user friendly website using this url http://127.0.0.1:8000/ (or the specified port).

## ⚙️ File Structure

### `/mainpage`

Just the user friendly front-end.

### `/predictor`

The backend, where the magic happens.

### `/predictor/learner.py`

The machine learning model with the preprocess, train and split, learn and predict functions that makes our software a reality.

### `/predictor/data`

The scrapped data used to train the ML-ModelS.

### `/predictor/views.py`

A little API to connect with our front-end.

### `Motonitor_ML.ipynb`

A Jupyter Notebook used for internal purposes on calculating the best scores for our Machine Learning Models and analyzing them with graphics.

## 📝 ML-Model Analysis and Scores
In the development of our software we did some analysis of the data that we were getting from our Machine Learning Models.

Our score calculation results:<br><br>
![motonitor-score](https://user-images.githubusercontent.com/6135390/166442345-5eaa0bdd-e122-4874-a0c6-4fad30d3efd9.png)

Motonitor's linear regression line:<br><br>
![motonitor-linear-regression-line](https://i.imgur.com/0QCTkpz.png)


## ⭐️ Screenshot
![motonitor-screenshot](https://i.imgur.com/2W8yzeK.png)

## ⚠️ License

`Motonitor` is free and open-source software non-licensed. Official Motonitor was created by [Jorge Vinagre Triguero](https://github.com/jorgec444), [Zhensheng Chen](https://github.com/kurohaka), [Roberto Lupu](https://github.com/Robertolupu) and [Joel Otero Martín](https://github.com/werogg) for the [HackUPC 2022 BarcelonaTech student Hackathon](https://hackupc-2022.devpost.com) in 36h in a non-stop and non-sleeping rush submitted [here](https://devpost.com/software/motinator?ref_content=my-projects-tab&ref_feature=my_projects).

