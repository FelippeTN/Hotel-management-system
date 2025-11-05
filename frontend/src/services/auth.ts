const apiUrl = "http://localhost:8000/api/v1"

interface NewUser {
  name: string
  email: string
  password: string
}

interface UserRead {
  id: number
  name: string
  email: string
  is_active: boolean
  last_login_at: string | null
}

interface LoginResponse {
  access_token: string
  token_type: string
  user: UserRead
}

export async function registerUser(userData: NewUser): Promise<UserRead> {
  const response = await fetch(`${apiUrl}/auth/register`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(userData),
  })
  
  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}))
    throw new Error(errorData.detail || "Falha ao criar usuário")
  }
  
  return response.json()
}

export async function loginUser(email: string, password: string): Promise<LoginResponse> {
  const response = await fetch(`${apiUrl}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  })
  
  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}))
    throw new Error(errorData.detail || "Falha ao fazer login")
  }
  
  return response.json()
}
