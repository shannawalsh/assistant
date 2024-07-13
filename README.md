# Setting up to run scripts using the openai API with Python.

The script will be run in a virtual environment. Start by creating a virtual environment:  

On a Mac: <code>python3 -m venv openai-env</code>

On Windows: <code>python -m venv openai-env</code>


After creating the virtual environment, you need to activate it:  
On a Mac: <code>source openai-env/bin/activate</code>

On Windows: <code>openai-env\Scripts\activate</code>


Once the virtual environment is activated, the beginning of your terminal prompt should display **(openai-env)**.
Install the OpenAI API library by running (in both a Mac and Windows):  
<code>pip install --upgrade openai</code>

You'll see an openai-env folder has been added to the directory with all of the installed dependencies.


To run your code, in the command line run (change the file name if necessary):  
On a Mac: <code>python3 assistant.py</code>

On Windows: <code>python assistant.py</code>


When finished, close the virtual environment by running:  
<code>deactivate</code>

