from flask import Blueprint, render_template, request, jsonify
from app.functions.newsLoader import loadNews

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return render_template("index.html")

@main_bp.route("/news", methods=["GET"])
def load_news():
    """Return news as JSON (for AJAX requests)."""
    return jsonify(loadNews())
    



