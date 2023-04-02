# This is a tkinter app to connect to gpt-4
Connect to gpt4 from your local computer
## Using virtual env
```
python -m virtualenv chagpt4env
```
Activate the environment

```
source chatgptenv/bin/activate

```

then install the required packages in requirements.txt

```
python -m pip install -r requirements.txt

```
export your openai API key

```
export OPENAI_API_KEY=sk-yourKeytoken

```
then run the app

```
python -m chatgpt.py

```
## For more infos visit openai API docs
<a href="https://platform.openai.com/docs/introduction">OPENAI_DOCS</a>