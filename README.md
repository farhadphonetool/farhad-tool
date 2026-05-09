pkg update -y
pkg install python git -y

git clone https://github.com/farhadphonetool/farhad-tool.git

cd farhad-tool

pip install -r requirements.txt

python run.py
