### Steps to run

```
python -m pip install fastapi uvicorn[standard]
```

```
pip install spacy

python -m spacy download en_core_web_lg
```

```
uvicorn main:app --reload
```

Visit:

http://localhost:8000/docs

#### Notes: If pylance error comes up please follow below instruction

In VSCode, prese ctrl+shift+p
Select python interpreter
Enter the path of python executable from virtual environment (eg: C:\workspace\venv\Scripts\python.exe)
