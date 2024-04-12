echo "Building the project..."
python3.8 -m pip install -r requirements.txt

echo "Collect Static..."
python3.8 manage.py collectstatic --noinput --clear

