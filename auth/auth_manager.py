import os, json, secrets, hashlib, re

DATA_DIR = "userdata_01e4.dat"
USERS_FILE = os.path.join(DATA_DIR, "users.json")
SESSION_FILE = os.path.join(DATA_DIR, "user_session.json")


def hash_password(password: str, salt: str = None) -> str:
    if salt is None:
        salt = secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode(), salt.encode(), 100_000
    )
    return f"{salt}${digest.hex()}"


def verify_password(stored_hash: str, password: str) -> bool:
    try:
        salt, digest = stored_hash.split("$", 1)
        new_digest = hashlib.pbkdf2_hmac(
            "sha256", password.encode(), salt.encode(), 100_000
        ).hex()
        return secrets.compare_digest(digest, new_digest)
    except Exception:
        return False


def validate_email(email: str) -> bool:
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email))


def validate_password(password: str) -> bool:
    return bool(re.match(
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!#%*?&^]).{8,}$',
        password
    ))


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(users: dict):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


def register_user(email: str, password: str):
    users = load_users()
    if email in users:
        return False, "Email already registered"

    users[email] = {"password": hash_password(password)}
    save_users(users)
    return True, "Account created"


def login_user(email: str, password: str):
    users = load_users()
    if email not in users:
        return False, "User not found"

    if not verify_password(users[email]["password"], password):
        return False, "Invalid password"

    token = secrets.token_hex(32)
    with open(SESSION_FILE, "w") as f:
        json.dump({"user": email, "token": token}, f)

    return True, email
