echo "Building the project..."
python3.9 pip install django

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear

