## Create env
conda create -p venv_name python==3.13

## Activate env
conda activate location_of_env_folder

## Deactivate 
conda deactivate

## Install dependencies
pip install -r requirements.txt

## Run the app
uvicorn app.main:app --reload

## Accessible via below link in local
http://127.0.0.1:8000/