from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load models
models = {
    "Linear Regression": pickle.load(open('models/linear.pkl', 'rb')),
    "Decision Tree": pickle.load(open('models/decision_tree.pkl', 'rb')),
    "Random Forest": pickle.load(open('models/random_forest.pkl', 'rb')),
    "XGBoost": pickle.load(open('models/xgboost.pkl', 'rb'))
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get input values
            age = float(request.form['HouseAge'])
            rooms = float(request.form['AveRooms'])
            bedrms = float(request.form['AveBedrms'])

            features = np.array([[age, rooms, bedrms]])

            # Predict with all models
            results = {}
            for name, model in models.items():
                results[name] = model.predict(features)[0]

            return render_template('index.html', results=results, values=request.form)

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template('index.html', results=None)

if __name__ == '__main__':
    app.run(debug=True)
