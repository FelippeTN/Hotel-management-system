const apiUrl = "http://localhost:8000/api/v1"

interface NewUser {
    name: string
    email: string
    password: string
}

export async function registerUser(userData: NewUser): Promise<any> {
  const response = await fetch(`${apiUrl}/auth/register`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(userData),
  })
  if (!response.ok) {
    throw new Error("Failed to create user")
  }
  return response.json()
}