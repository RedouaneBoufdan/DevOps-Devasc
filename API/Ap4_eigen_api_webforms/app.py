from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_RANDOM = "https://api.chucknorris.io/jokes/random"
API_CATEGORIES = "https://api.chucknorris.io/jokes/categories"
API_BY_CATEGORY = "https://api.chucknorris.io/jokes/random?category="

def fetch_categories():
    try:
        r = requests.get(API_CATEGORIES, timeout=10)
        if r.status_code == 200:
            return r.json()
    except requests.RequestException:
        pass
    return []

def fetch_joke(category=None):
    try:
        if category and category != "random":
            url = API_BY_CATEGORY + category
        else:
            url = API_RANDOM

        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return None, f"API error (status {r.status_code})"

        data = r.json()
        return data, None
    except requests.exceptions.Timeout:
        return None, "Timeout: API did not respond in time."
    except requests.RequestException as e:
        return None, f"Request error: {e}"
    except ValueError:
        return None, "Error: response is not valid JSON."

@app.route("/", methods=["GET", "POST"])
def index():
    categories = fetch_categories()
    selected = "random"
    joke_text = None
    joke_id = None
    error = None

    if request.method == "POST":
        selected = request.form.get("category", "random")
        data, error = fetch_joke(selected)
        if data:
            joke_text = data.get("value")
            joke_id = data.get("id")

    return render_template(
        "index.html",
        categories=categories,
        selected=selected,
        joke_text=joke_text,
        joke_id=joke_id,
        error=error
    )

if __name__ == "__main__":
    # host=0.0.0.0 lets it run in VM / container easily
    app.run(host="0.0.0.0", port=5000, debug=True)
