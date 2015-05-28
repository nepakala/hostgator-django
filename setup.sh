tar -xvzf virtualenv-12.0.7.tar.gz 
cd virtualenv-12.0.7
/usr/local/bin/python2.7 setup.py install --user
cd ..
../../.local/bin/virtualenv pyenv --python=python2.7
rm -r virtualenv-12.0.7
. pyenv/bin/activate
pip install pip --upgrade
pip install django flup unirest ipython
