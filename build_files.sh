echo "Building the project..."
python3.9 -m pip install -r r.txt
pip install --root-user-action=ignore

echo "Make Migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear