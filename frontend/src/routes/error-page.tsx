import { isRouteErrorResponse, Link, useRouteError } from 'react-router'

const ErrorPage = () => {
  const error = useRouteError()

  const status = isRouteErrorResponse(error) ? error.status : 500
  const statusText = isRouteErrorResponse(error)
    ? error.statusText
    : 'Erro interno'
  const message = isRouteErrorResponse(error)
    ? error.data?.message ?? 'Não foi possível carregar esta rota.'
    : (error as Error | undefined)?.message ?? 'Algo inesperado aconteceu.'

  return (
    <div className="flex min-h-[60vh] flex-col items-center justify-center gap-4 text-center">
      <div className="space-y-1">
        <p className="text-sm font-medium text-muted-foreground">{status}</p>
        <h1 className="text-3xl font-semibold tracking-tight">{statusText}</h1>
        <p className="text-muted-foreground text-sm">{message}</p>
      </div>
      <Link
        to="/"
        className="rounded-lg bg-primary px-4 py-2 text-sm font-medium text-primary-foreground"
      >
        Voltar para o painel
      </Link>
    </div>
  )
}

export default ErrorPage
