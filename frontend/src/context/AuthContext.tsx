import { createContext, useContext, ReactNode, useState, useEffect } from 'react'

type User = {
  id: string
  email: string
  name: string
}

type AuthContextType = {
  currentUser: User | null
  login: (email: string, password: string) => Promise<void>
  register: (email: string, password: string, name: string) => Promise<void>
  logout: () => Promise<void>
}

const AuthContext = createContext<AuthContextType | null>(null)

export function useAuth() {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider')
  }
  return context
}

export function AuthProvider({ children }: { children: ReactNode }) {
  const [currentUser, setCurrentUser] = useState<User | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Check if user is logged in
    const user = localStorage.getItem('user')
    if (user) {
      setCurrentUser(JSON.parse(user))
    }
    setLoading(false)
  }, [])

  const login = async (email: string, password: string) => {
    // TODO: Implement actual login logic
    const user = { id: '1', email, name: 'Test User' }
    localStorage.setItem('user', JSON.stringify(user))
    setCurrentUser(user)
  }

  const register = async (email: string, password: string, name: string) => {
    // TODO: Implement actual registration logic
    const user = { id: '1', email, name }
    localStorage.setItem('user', JSON.stringify(user))
    setCurrentUser(user)
  }

  const logout = async () => {
    localStorage.removeItem('user')
    setCurrentUser(null)
  }

  const value = {
    currentUser,
    login,
    register,
    logout,
  }

  return <AuthContext.Provider value={value}>{!loading && children}</AuthContext.Provider>
}