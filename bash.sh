echo "Building the project..."
python3.9 -m pip3 install Django=4.2.2 

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear

