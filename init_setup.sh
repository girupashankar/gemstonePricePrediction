echo [$(data)]: "START"

echo [$(data)]: "Creating Environment with python 3.8 versuib."
conda create --prefix ./venv python=3.10 -y

echo [$(data)]: "Activating Environment"
source activate ./venv

echo [$(data)]: "Installing the requirements"
pip install -r requirements.txt

echo [$(data)]: "END"

