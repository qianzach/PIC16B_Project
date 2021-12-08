from dash_package import app

# To run the app locally, locate the directory, activate conda environment, and finally type python run.py in terminal
import dash

app._favicon = 'favicon.ico'
#app.title = "Network Recommendation Engine: Visualization"
if __name__ == "__main__":
    app.run_server(debug=True)