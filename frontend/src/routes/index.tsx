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
    errorElement: <ErrorPage />,
    children: [
      { index: true, element: <DashboardPage /> },
      { path: 'auth', element: <AuthPage /> },
      { path: 'bookings', element: <BookingsPage /> },
      { path: 'guests', element: <GuestsPage /> },
      { path: 'rooms', element: <RoomsPage /> },
    ],
  },
])
