# Flask Tutorials to Deploy Machine Learning Model
Launch machine learning models into production using flask.

# 1. Predict House Price

## Environment and tools
1. scikit-learn
2. pandas
3. numpy
4. flask

## Installation

`pip install scikit-learn pandas numpy flask`

`python model-houseprice.py`

`python app.py`

![Logo](product-img.jpg)

# 2. Predict Sales Price

Download the dataset from [here](https://www.kaggle.com/harithapliyal/house-sales-prices-in-king-county-usa).

## Environment and tools
1. scikit-learn
2. pandas
3. numpy
4. flask
5. docker

## Installation

`docker-compose up --build`

`curl -X POST -H "Content-Type: application/json" -d @to_predict_json.json http://localhost:8080/predict_price`

where `to_predict.json` contains:

`{"grade":5.0,"lat":47.200,"long":-122.600,"sqft_living":2000,"waterfront":1.0,"yr_built":2010.0}`

or

`curl -X POST -H "Content-Type: application/json" 
-d '{"grade":5.0,"lat":47.200,"long":-122.600,"sqft_living":2000,"waterfront":1.0,"yr_built":2010.0}' 
http://localhost:8080/predict_price`

Output:

```json
{
  "predict cost": 1,461,447.83
}
```

## Citing

If you find this code useful in your research, please consider citing the blog:

```
@misc{dasarpai-flask-mldeploy,
  Author = {Hari Thapliyal},
  Title = {How to Easily Deploy Machine Learning Models Using Flask},
  Year = {2021},
  Journal = {Kaggle},
}
```

## License

```
MIT License

Copyright (c) 2021 Hari Thapliyal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
