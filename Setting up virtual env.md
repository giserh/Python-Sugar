[Virtualenv Basics](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
[More advanced](https://realpython.com/blog/python/python-virtual-environments-a-primer/)

more resources: [blog](http://docs.python-guide.org/en/latest/dev/virtualenvs/)


```shell
# libraries you need
pip install virtualenv # install virtualenv your system's python2.
pip install virtualenvwrapper # helps you manage virtual environments.

# setting up easy commands in terminal
# add this to your ~/.zshrc file and run source ~/.zshrc
export WORKON_HOME=$HOME/.virtualenvs   # optional
export PROJECT_HOME=$HOME/projects      # optional
# path you get from which virtualenvwrapper.sh
source /Library/Frameworks/Python.framework/Versions/2.7/bin/virtualenvwrapper.sh

cd my_project_folder # go to wherever you want to start your project, or whereever your project is located.

# setup your env
mkvirtualenv my_project # create a virtualenv for the project.
virtualenv -p $(which python3) blog_virtualenv # use python2.7 interpreter.
virtualenv -p /usr/bin/python2.7 my_project # use python2.7 interpreter, same as above
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2.7 # or you can set it in your ~/.zshrc.

# start your env/download your libraries.
source my_project/bin/activate # activate your virtual env.
pip install requests # install requests in your virtual env.

# others
mkvirtualenv my_project # create env.
workon                  # lists all your envs.
workon my_project       # activate the env.
deactivate              # deactivate your env.
rmvirtualenv my_project # remove env.
```
