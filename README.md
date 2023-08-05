# Project Information
- Github URL: https://github.com/laurent4ml/build-ml-pipeline-for-short-term-rental-prices
- WANDB URL: https://wandb.ai/laurent4ml/nyc_airbnb/

# Goal 
Build a ML Pipeline for Short-Term Rental Prices in NYC to estimate the typical price for a given property based on the price of similar properties. 
New data is received in bulk every week. 
The model needs to be retrained with the same cadence.

## Steps
- Exploratory Data Analysis (EDA)
- Data cleaning
- Data testing
- Data splitting
- Train Random Forest
- Optimize hyperparameters
- Select the best model
- Test
- Visualize the pipeline
- Release ML pipeline

# Configuration
The parameters controlling the pipeline are defined in the config.yaml file.
We will use Hydra to manage this configuration file.

# Run the full pipeline
```
> mlflow run .
```

# Run only some steps
here only the download and basic_cleaning steps are run
```
> mlflow run . -P steps=download,basic_cleaning
```

# Overwrite some configuration parameters
```
> mlflow run . \
  -P steps=download,basic_cleaning \
  -P hydra_options="modeling.random_forest.n_estimators=10 etl.min_price=50"
```