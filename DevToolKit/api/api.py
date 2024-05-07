# import jwt
import httpx

import os
from dotenv import load_dotenv


load_dotenv()

PUBLIC_KEY: str = os.environ["SUPABASE_KEY"]


async def user_login_endpoint(email:str, password: str):
    url = "https://wvwdqwltnkkhfmmxfwpa.supabase.co/auth/v1/token?grant_type=password"
    headers = {
        "apikey": PUBLIC_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "email": email,
        "password": password
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        data = response.json()
        access_token = data.get("access_token")  # Usamos .get() para evitar KeyError
        expires_in = data.get("expires_in")
        user_id = None
        user_email = None
        if "user" in data:
            user_data = data["user"]
            user_id = user_data.get("id")  # Usamos .get() para evitar KeyError
            user_email = user_data.get("email")  # Usamos .get() para evitar KeyError

        return access_token, expires_in, user_id, user_email
    
async def username_registration_endpoint(user_id: int, username: str):
    url = "https://wvwdqwltnkkhfmmxfwpa.supabase.co/rest/v1/users"
    headers = {
        "apikey": PUBLIC_KEY,
        "Authorization": f"Bearer {PUBLIC_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "id": user_id,
        "username": username
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        return response.status_code

async def is_username_taken(username: str):
    url = "https://wvwdqwltnkkhfmmxfwpa.supabase.co/rest/v1/users?select=*"
    headers = {
        "apikey": PUBLIC_KEY,
        "Authorization": f"Bearer {PUBLIC_KEY}"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        users = response.json()
        print("is_username_taken -> log para ver los users",users)
        return any(user.get("username") == username for user in users)


async def user_registration_endpoint(username: str, email: str, password: str):
    url = "https://wvwdqwltnkkhfmmxfwpa.supabase.co/auth/v1/signup"
    headers = {
        "apikey": PUBLIC_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "email": email,
        "password": password,
        "username": username
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=data)
            print("user_registration_endpoint -> response status code:", response.status_code)
            print("user_registration_endpoint -> response body:", response.text)

            if response.status_code == 400:
                error_msg = response.json().get("error_description", "")
                if "email" in error_msg and "already exists" in error_msg:
                    print("El correo electrónico ya está registrado.")
                    return "El correo electrónico ya está registrado."
                elif "username" in error_msg and "already exists" in error_msg:
                    print("El nombre de usuario ya está en uso.")
                    return "El nombre de usuario ya está en uso."
                else:
                    print("Error desconocido al registrar el usuario")
                    return f"Error desconocido al registrar el usuario: {error_msg}"

            if response.status_code == 200:
                data = response.json()
                user_id = data.get("id")
                if user_id:
                    await username_registration_endpoint(user_id, username)
                    return True
                else:
                    return "Error al procesar la respuesta del servidor."

            return ("Error desconocido al registrar el usuario.", data)
    except Exception as e:
        print("Excepción en user_registration_endpoint:", e)
        return f"Excepción al registrar el usuario: {str(e)}"