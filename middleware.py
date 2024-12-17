from flask import Flask, request, jsonify, session, redirect
from functools import wraps

app = Flask(__name__)
app.secret_key = "secure_key"  # Replace with your secure key

# Dummy user database
users_db = {
    "admin_user": {"password": "admin_pass", "role": "admin"},
    "manager_user": {"password": "manager_pass", "role": "manager"},
    "viewer_user": {"password": "viewer_pass", "role": "viewer"}
}

# Role-permission mapping
role_permissions = {
    "admin": {"can_view": True, "can_edit": True, "can_delete": True},
    "manager": {"can_view": True, "can_edit": True, "can_delete": False},
    "viewer": {"can_view": True, "can_edit": False, "can_delete": False}
}

# Authentication Function
def authenticate(username, password):
    user = users_db.get(username)
    return user if user and user["password"] == password else None

# Authorization Decorator
def role_required(permission):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if 'user' not in session:
                return redirect("/login")
            role = session["user"]["role"]
            if not role_permissions[role].get(permission, False):
                return jsonify({"error": "Unauthorized access"}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator

# Routes
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = authenticate(data["username"], data["password"])
    if user:
        session["user"] = user
        return jsonify({"message": f"Welcome {user['role']}!"})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/dashboard/view")
@role_required("can_view")
def view_dashboard():
    return jsonify({"message": "Dashboard view access granted."})

@app.route("/dashboard/edit")
@role_required("can_edit")
def edit_dashboard():
    return jsonify({"message": "Dashboard edit access granted."})

@app.route("/dashboard/delete")
@role_required("can_delete")
def delete_dashboard():
    return jsonify({"message": "Dashboard delete access granted."})

if __name__ == "__main__":
    app.run(debug=True)
