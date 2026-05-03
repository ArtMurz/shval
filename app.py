from datetime import datetime
from flask import Flask, redirect, request
app = Flask(__name__)

TARGET = "https://cloud.mail.ru/public/C3Nj/"

@app.route("/")
def go():
    # тут ты ловишь факт перехода
    user_ip = request.remote_addr
    user_agent = request.headers.get("User-Agent")

    print("Переход по ссылке!")
    print("IP:", user_ip)
    print("UA:", user_agent)

    # редирект на нужную страницу
    with open("clicks.log", "a", encoding="utf-8") as f:
        f.write(f"Время - {datetime.now()} | IP - [{user_ip} | Еще что-то {user_agent}\n")
    return redirect("https://cloud.mail.ru/public/C3Nj/8JYTes8G9")

if __name__ == "__main__":
    app.run(debug=True)
