from fastapi import HTTPException
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="user_db"
    )

# ---------- SIGNUP ----------
async def signup_user(username: str, password: str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT id FROM users WHERE username = %s",
            (username,)
        )
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="User already exists")

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password)
        )
        conn.commit()

        return {"success": True, "message": "Signup successful"}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()


# ---------- LOGIN ----------
async def login_user(username: str, password: str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT username, password FROM users WHERE username = %s",
            (username,)
        )
        user = cursor.fetchone()

        if not user or user["password"] != password:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        return {
            "success": True,
            "message": "Login successful",
            "username": user["username"]
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()
