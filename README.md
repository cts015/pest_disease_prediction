# pest_disease_prediction
A machine learning app to predict the number of codling moths (Cydia pomonella), which are a major pest of apple and pear trees, based on vegetative and meteorlogical data.

This model was trained on vegetation and weather data for the Bucknell University Farm in Lewisburg, PA.

Explanation of terms: the previous month's data (lag1) is considered, as well as the current month's data (lag0). NDVI (normalized difference vegetation index) is a number that measures the density and health of vegetation in the area.

Process to clean up data and choose best ML model:
First compile sample data into csv file.
Read sample data from xls or csv file.
Then, perform exploratory data analysis (EDA) of sample data.
EDA includes removing duplicates, filling missing values with the mean for the column, and normalization/standardization if necessary.
The app will then categorize the data into targets and features.
Multiple regression models are trained and tested and RMSE is calculated to assess performance.
Once the best model is selected based on the lowest RMSE, push the best_model.pkl to GitHub repo for Streamlit app.

Streamlit app:
https://pestdiseaseprediction-oembzg9k4hcbzxzyopvyy8.streamlit.app/

Google colab to find best model:
https://colab.research.google.com/drive/1jhCJz-efppGe3UBYape4shSyKU-kwLbi?usp=sharing
