#git clone https://github.com/erichamk/nurseapp
#cd nurseapp
#sudo apt-get -y install python3-venv python3-pip
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata initialdata.json

python manage.py runserver 0.0.0.0:8000
