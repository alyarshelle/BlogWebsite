import os
import datetime
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient


def create_app():
    appp = Flask(__name__)
    try:

        client = MongoClient("mongodb+srv://alyaarshelle:L()kAAdri3nmb@blog-website.hw5zo.mongodb.net/")
        appp.db = client.bloggy

        @appp.route("/", methods=["GET", "POST"])
        def homePage():
            if request.method == "POST":
                entry_content = request.form.get("content")
                formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
                appp.db.entries.insert_one({"content": entry_content, "date": formatted_date})

                # Redirect to the homepage to prevent duplicate submissions on refresh
                return redirect(url_for('homePage'))

            entries_date = [
                (
                    entry["content"],
                    entry["date"],
                    datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
                )
                for entry in appp.db.entries.find({})
            ]

            return render_template("blogHome.html", entries=entries_date)

        return appp

    except Exception as ex:
        appp.logger.error(f"Error occurred: {ex}")
        return "An error occurred", 500


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
