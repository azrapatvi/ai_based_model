# 🤖 ChatGPT Terminal Assistant using boltiotai

This is a simple Python-based chatbot that allows users to interact with OpenAI’s ChatGPT (gpt-3.5-turbo) model through the terminal. The script uses the `boltiotai` module to indirectly access the OpenAI API via an API key stored in a separate file.

---

## 📁 Project Structure
```
project-folder/
├── apikey.py # Contains the API key
├── simple_ai+model.py # Main chatbot script
```


---

## 🔐 Storing Your API Key

Create a file named `apikey.py` and store your OpenAI key in it like this:

```python
# apikey.py
OPENAI_API_KEY = "your_openai_api_key_here"

