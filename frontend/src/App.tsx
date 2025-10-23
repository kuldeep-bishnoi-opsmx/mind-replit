import { Routes, Route, Navigate } from 'react-router-dom'
//import { Toaster } from '@/components/ui/toaster'
import Dashboard from './pages/dashboard/Dashboard'
import Chat from './pages/chat/Chat'
import MoodTracker from './pages/mood/MoodTracker'
import Journal from './pages/journal/Journal'
import Settings from './pages/settings/Settings'
import Login from './pages/auth/Login'
import { useAuth } from './context/AuthContext'

function App() {
  const { currentUser } = useAuth()

  return (
    <div className="min-h-screen bg-background">
      <Routes>
        <Route path="/login" element={!currentUser ? <Login /> : <Navigate to="/" />} />
        <Route
          path="/"
          element={currentUser ? <Dashboard /> : <Navigate to="/login" />}
        />
        <Route
          path="/chat"
          element={currentUser ? <Chat /> : <Navigate to="/login" />}
        />
        <Route
          path="/mood"
          element={currentUser ? <MoodTracker /> : <Navigate to="/login" />}
        />
        <Route
          path="/journal"
          element={currentUser ? <Journal /> : <Navigate to="/login" />}
        />
        <Route
          path="/settings"
          element={currentUser ? <Settings /> : <Navigate to="/login" />}
        />
      </Routes>
      {/* <Toaster /> */}
    </div>
  )
}

export default App