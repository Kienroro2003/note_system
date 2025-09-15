import logging

from flask import Blueprint, jsonify, request

from .db_manager import get_db_connection

api = Blueprint("api", __name__)


@api.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json()
    if not data or "content" not in data:
        return jsonify({"error": "Missing content"}), 400

    content = data["content"]
    user_id = 1  # Giả sử đã xác thực người dùng

    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = "INSERT INTO `notes` (`content`, `user_id`) VALUES (%s, %s)"
            cursor.execute(sql, (content, user_id))
        conn.commit()

        note_id = conn.insert_id()
        logging.info(f"USER {user_id} CREATED note {note_id}")

        return jsonify({"id": note_id, "content": content}), 201

    except Exception as e:
        logging.error(f"Error creating note: {e}")
        return jsonify({"error": "Could not process request"}), 500
    finally:
        if conn:
            conn.close()
