# Mall Customer Segmentation

This project is a modularized version of the Week 11 Unsupervised Clustering notebook for the CST2216 Individual Term Project.

The application uses K-Means clustering to segment mall customers based on age, annual income, and spending score. Streamlit provides an interactive interface for exploring cluster quality, visualizing customer groups, reviewing cluster profiles, and assigning new customers to a segment.

## Features

- Loads the Week 11 `mall_customers.csv` dataset
- Validates required customer data
- Converts clustering features to numeric values
- Standardizes features using `StandardScaler`
- Evaluates multiple possible cluster counts
- Uses silhouette score to recommend an appropriate value of `k`
- Trains a K-Means clustering model
- Uses reproducible K-Means initialization
- Displays an interactive income-versus-spending scatter plot
- Displays average customer characteristics for each cluster
- Allows users to change the number of clusters
- Assigns new customers to an existing cluster
- Supports uploading another compatible CSV dataset
- Includes logging and user-friendly error handling
- Includes automated model tests

## Project Structure

```text
customer-segmentation-app/
│
├── data/
│   └── mall_customers.csv
│
├── src/
│   ├── __init__.py
│   ├── data.py
│   └── model.py
│
├── tests/
│   └── test_model.py
│
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

## Dataset

The application uses the Week 11 `mall_customers.csv` dataset.

The clustering model uses the following features:

- `Age`
- `Annual_Income`
- `Spending_Score`

The dataset may also contain additional customer information, but the three features above are used for K-Means clustering.

The dataset is stored at:

```text
data/mall_customers.csv
```

A compatible CSV file can also be uploaded through the Streamlit application.

## Model

The application uses the K-Means clustering algorithm from scikit-learn.

Because K-Means is distance-based, the clustering features are standardized using:

```text
StandardScaler
```

The application evaluates several possible values of `k` and calculates the silhouette score for each option.

The silhouette score measures how well customers fit within their assigned clusters compared with other clusters.

The application uses the highest silhouette score to suggest an appropriate number of clusters.

The K-Means model uses:

- K-Means++ initialization
- Multiple initialization attempts
- A fixed random state for reproducibility

The trained model is also used to assign new customers to one of the generated clusters.

## Cluster Evaluation

The application evaluates different values of `k` using:

- Silhouette Score
- Model inertia

The Streamlit interface displays:

- Current silhouette score
- Suggested value of `k`
- Interactive customer-cluster visualization
- Average characteristics of each cluster

Users can also manually change the number of clusters using the Streamlit slider.

## Installation

Follow these steps from the `customer-segmentation-app` folder.

### 1. Open the project in VS Code

Open the `customer-segmentation-app` folder in Visual Studio Code.

### 2. Open a terminal

In VS Code, select:

**Terminal → New Terminal**

Check the current directory with:

```powershell
Get-Location
```

The path should end with:

```text
customer-segmentation-app
```

If necessary, move into the project folder:

```powershell
cd .\customer-segmentation-app
```

### 3. Create a virtual environment

Run:

```powershell
python -m venv .venv
```

This creates an isolated Python environment for the project.

### 4. Activate the virtual environment

On Windows PowerShell, run:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, the terminal should look similar to:

```text
(.venv) PS C:\...\customer-segmentation-app>
```

### 5. Install the required packages

Run:

```powershell
python -m pip install -r requirements.txt
```

The required packages include:

- Streamlit
- pandas
- scikit-learn
- Plotly
- pytest

## Run the Tests

The project contains automated tests for clustering and customer-segment assignment.

From the `customer-segmentation-app` folder, run:

```powershell
python -m pytest -v
```

A successful test run should display:

```text
PASSED
```

The automated tests verify that:

- The real dataset can be loaded
- Cluster evaluation produces results
- K-Means can create the requested number of clusters
- The silhouette score is within a valid range
- A new customer can be assigned to a valid cluster

## Run the Application

Make sure the dataset exists at:

```text
data/mall_customers.csv
```

Then start the Streamlit application:

```powershell
python -m streamlit run app.py
```

Streamlit will start a local web server.

The application will normally open automatically at:

```text
http://localhost:8501
```

If the browser does not open automatically, copy the local URL displayed in the terminal and open it manually.

To stop the application, return to the terminal and press:

```text
Ctrl + C
```

## How to Use

1. Start the Streamlit application.
2. The bundled Week 11 `mall_customers.csv` dataset loads automatically.
3. The application evaluates different cluster counts.
4. Review the displayed:
   - Silhouette score
   - Suggested number of clusters
5. Use the **Number of clusters** slider to change `k` if desired.
6. Review the interactive scatter plot showing:
   - Annual income
   - Spending score
   - Customer cluster
7. Review the **Cluster Profiles** table to compare average:
   - Age
   - Annual income
   - Spending score
8. Scroll to the customer-assignment section.
9. Enter:
   - Age
   - Annual income
   - Spending score
10. Click **Assign Segment**.
11. The application displays the cluster assigned to the new customer.

A different compatible `mall_customers.csv` dataset can also be uploaded using the CSV uploader.

## Visualization

The application uses Plotly to create an interactive scatter plot.

The chart displays:

- Annual Income on the x-axis
- Spending Score on the y-axis
- Cluster membership using separate groups
- Customer Age as additional hover information

This makes it easier to visually compare the customer segments identified by K-Means.

## Error Handling

The application validates the dataset before clustering.

Validation includes:

- Checking for required columns
- Ensuring age, income, and spending score are numeric
- Checking for missing required values
- Requiring a minimum number of customer records
- Rejecting invalid age values
- Rejecting negative annual income
- Ensuring spending score remains between 1 and 100
- Ensuring the requested number of clusters is valid

If invalid data is provided, the application displays a user-friendly error message rather than terminating unexpectedly.

Errors are also recorded using Python logging.

## Deployment

This project is designed to be deployed using Streamlit Community Cloud.

To deploy the application:

1. Publish this project to a GitHub repository.
2. Make sure the repository contains:
   - `app.py`
   - `requirements.txt`
   - `data/mall_customers.csv`
   - `src/`
   - `tests/`
   - `README.md`
3. Open Streamlit Community Cloud.
4. Connect your GitHub account.
5. Select the GitHub repository for this project.
6. Select the `main` branch.
7. Use the following file as the Streamlit application entry point:

```text
app.py
```

8. Deploy the application.
9. Open the public Streamlit URL.
10. Test the application in a signed-out or private browser window to confirm that it is publicly accessible and working correctly.

## Educational Use

This project was developed for the CST2216 Individual Term Project.

The customer segments produced by the clustering model are intended as a machine-learning demonstration and should be interpreted as exploratory groupings rather than definitive descriptions of individual customers.
