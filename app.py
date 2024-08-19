import os
import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient


def create_app():
    appp = Flask(__name__)
    client = MongoClient(MONGODB_URI)
    appp.db = client.bloggy

    @appp.route("/", methods=["GET", "POST"])
    def homePage():
        print([e for e in appp.db.entries.find({})])
        if request.method == "POST":
            entry_content = request.form.get("content")  # content is the name of the field
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            appp.db.entries.insert_one({"content": entry_content, "date": formatted_date})

        entries_date = [
            (
                entry["content"],
                entry["date"],
                datetime.datetime.today().strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
            )

            for entry in appp.db.entries.find({})
        ]

        return render_template("blogHome.html", entries=entries_date)

    return appp


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
