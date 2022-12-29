# <u>Iris Flower Prediction through Web</u>

#### Deploying the Iris Flower Predicition Machine Learning Model using a RESTful Web application

##### How to run the program:

Run these commands first:

- `pip install -r requirements.txt` This command will install neccessary dependencies to tun the flask app and jupyter kernel

Note: Some or most of these packages may already be installed in your system. In that case just ignore the splash texts in the terminal that says "Requirements already met blah blah blah...". Its will then install the dependecies that are not in youre install system automatically. Just don't forget to run the command above.

After all packages have been installed `cd` into the `model` directory and:

- `jupyter notebook iris_flower_prediction.ipynb`

This will open up the notebook in jupyter. If you are just trying to test the app out, then just run all the cells once and your good to move on to the next step. Although, if you want to, you can play around with the notebook a little bit; try different models (I personally have used RandomForestClassifier), remove any unecessary cells like the classification report and stuff. But be sure of what you are doing and just don't make any changes to the rest of the code.

Next step is to run the different servers:

`cd ` into the `backend` directory and run:

- `flask run`

This will start up the backend server.

Next, `cd` into the `frontend` directory and run:

- `python3 -m http.server`

This will start up the server to display the web app.

Now go to `http://localhost:8000` to use the web app.

### <u>Note of Thanks</u>

Special thanks to [Raunak Joshi](https://www.linkedin.com/in/raunak-joshi-274a75133/) for this project tutorial.

#### Link to his [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/c/RaunakJoshi)