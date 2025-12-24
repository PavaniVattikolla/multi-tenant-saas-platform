import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(!!localStorage.getItem('token'));

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      setIsAuthenticated(true);
    }
  }, []);

  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/" element={isAuthenticated ? <Navigate to="/dashboard" /> : <Navigate to="/login" />} />
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/projects" element={<ProjectsPage />} />
        <Route path="/projects/:projectId" element={<ProjectDetailsPage />} />
        <Route path="/users" element={<UsersPage />} />
      </Routes>
    </Router>
  );
}

function LoginPage() {
  return <div style={{padding: '40px'}}>Login Page</div>;
}

function RegisterPage() {
  return <div style={{padding: '40px'}}>Register Page</div>;
}

function DashboardPage() {
  return <div style={{padding: '40px'}}>Dashboard Page</div>;
}

function ProjectsPage() {
  return <div style={{padding: '40px'}}>Projects Page</div>;
}

function ProjectDetailsPage() {
  return <div style={{padding: '40px'}}>Project Details Page</div>;
}

function UsersPage() {
  return <div style={{padding: '40px'}}>Users Page</div>;
}

export default App;
