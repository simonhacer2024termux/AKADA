pkg update -y && pkg upgrade -y
pkg install python
pkg install pip
pip install colour,requests,dadata,pystyle,colorama
pkg install git
git clone https://github.com/simonhacer2024termux/AKADA
cd ARKADA
python main.py
