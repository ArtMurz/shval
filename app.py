from flask import Flask, request, redirect
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    user_agent = request.headers.get("User-Agent")
    print("IP:", ip)

    with open("clicks.log", "a", encoding="utf-8") as f:
        f.write(f"Время - {datetime.now()} | IP - [{user_ip} | Еще что-то {user_agent}\n")
    return redirect("https://www.deepseek.com/en/")  # ← сюда меняешь ссылку

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
