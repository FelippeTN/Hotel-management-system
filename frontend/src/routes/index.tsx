import { createBrowserRouter } from 'react-router'

import ErrorPage from './error-page.tsx'
import DashboardPage from '@/pages/dashboard.tsx'
import RegisterPage from '@/pages/register.tsx'
import LoginPage from '@/pages/login.tsx'
import BookingsPage from '@/pages/bookings.tsx'
import GuestsPage from '@/pages/guests.tsx'
import RoomsPage from '@/pages/rooms.tsx'
import RequireAuth from '@/components/RequireAuth'

export const router = createBrowserRouter([
  {
    path: '/',
    element: (
      <RequireAuth>
        <DashboardPage />
      </RequireAuth>
    ),
    errorElement: <ErrorPage />,
  },
  {
    path: '/register',
    element: <RegisterPage />,
    errorElement: <ErrorPage />,
  },
  {
    path: '/login',
    element: <LoginPage />,
    errorElement: <ErrorPage />,
  },
  {
    path: '/bookings',
    element: (
      <RequireAuth>
        <BookingsPage />
      </RequireAuth>
    ),
    errorElement: <ErrorPage />,
  },
  {
    path: '/guests',
    element: (
      <RequireAuth>
        <GuestsPage />
      </RequireAuth>
    ),
    errorElement: <ErrorPage />,
  },
  {
    path: '/rooms',
    element: (
      <RequireAuth>
        <RoomsPage />
      </RequireAuth>
    ),
    errorElement: <ErrorPage />,
  },
])
