import { createBrowserRouter } from 'react-router'

import ErrorPage from './error-page.tsx'
import DashboardPage from '@/pages/dashboard.tsx'
import AuthPage from '@/pages/auth.tsx'
import BookingsPage from '@/pages/bookings.tsx'
import GuestsPage from '@/pages/guests.tsx'
import RoomsPage from '@/pages/rooms.tsx'

export const router = createBrowserRouter([
  {
    path: '/',
    element: <DashboardPage />,
    errorElement: <ErrorPage />,
  },
  {
    path: '/auth',
    element: <AuthPage />,
    errorElement: <ErrorPage />,
  },
  {
    path: '/bookings',
    element: <BookingsPage />,
    errorElement: <ErrorPage />,
  },
  {
    path: '/guests',
    element: <GuestsPage />,
    errorElement: <ErrorPage />,
  },
  {
    path: '/rooms',
    element: <RoomsPage />,
    errorElement: <ErrorPage />,
  },
])
