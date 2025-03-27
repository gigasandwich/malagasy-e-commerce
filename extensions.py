# Module created to get rid of circular import
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Folders for training
raw_data_folder = 'data/raw-data'
trained_models_folder = 'data/trained-models'