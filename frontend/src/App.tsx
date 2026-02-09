import type { ReactNode } from "react"
import { Navigate, Route, Routes } from "react-router-dom"

import Login from "./pages/Login"
import Signup from "./pages/Signup"
import Tasks from "./pages/Tasks"

function isAuthenticated(): boolean {
  return !!localStorage.getItem("access_token")
}

function PrivateRoute({ children }: { children: ReactNode }) {
  if (!isAuthenticated()) {
    return <Navigate to="/login" replace />
  }

  return children
}

export default function App() {
  return (
    <Routes>
      {/* PUBLIC */}
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<Signup />} />

      {/* PRIVATE */}
      <Route
        path="/tasks"
        element={
          <PrivateRoute>
            <Tasks />
          </PrivateRoute>
        }
      />

      {/* FALLBACK */}
      <Route
        path="*"
        element={
          <Navigate
            to={isAuthenticated() ? "/tasks" : "/login"}
            replace
          />
        }
      />
    </Routes>
  )
}
