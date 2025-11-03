import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'

const AuthPage = () => {
  return (
    <div className="flex min-h-[60vh] items-center justify-center px-4">
      <Card className="w-full max-w-md">
        <CardHeader>
          <CardTitle className="text-2xl">Acesse sua conta</CardTitle>
          <CardDescription>Faça login para gerenciar o hotel.</CardDescription>
        </CardHeader>
        <CardContent className="flex flex-col gap-4">
          <label className="flex flex-col gap-1 text-sm">
            <span className="font-medium">Email</span>
            <input
              type="email"
              placeholder="voce@hotel.com"
              className="rounded-lg border border-border bg-background px-3 py-2 text-base"
            />
          </label>
          <label className="flex flex-col gap-1 text-sm">
            <span className="font-medium">Senha</span>
            <input
              type="password"
              placeholder="••••••••"
              className="rounded-lg border border-border bg-background px-3 py-2 text-base"
            />
          </label>
          <button className="rounded-lg bg-primary px-4 py-2 text-sm font-medium text-primary-foreground">
            Entrar
          </button>
        </CardContent>
        <CardFooter className="text-sm text-muted-foreground">
          Ainda não tem acesso? Entre em contato com o administrador.
        </CardFooter>
      </Card>
    </div>
  )
}

export default AuthPage