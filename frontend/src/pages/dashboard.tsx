const DashboardPage = () => {
  return (
    <section className="space-y-4">
      <header>
        <h1 className="text-3xl font-semibold tracking-tight">Painel</h1>
        <p className="text-muted-foreground text-sm">
          Visão geral rápida das métricas do hotel.
        </p>
      </header>
      <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        <div className="rounded-xl border border-border bg-card p-4">
          <h2 className="text-sm font-medium text-muted-foreground">Ocupação</h2>
          <p className="text-2xl font-semibold">72%</p>
        </div>
        <div className="rounded-xl border border-border bg-card p-4">
          <h2 className="text-sm font-medium text-muted-foreground">Receita diária</h2>
          <p className="text-2xl font-semibold">R$ 18.450</p>
        </div>
        <div className="rounded-xl border border-border bg-card p-4">
          <h2 className="text-sm font-medium text-muted-foreground">Check-ins hoje</h2>
          <p className="text-2xl font-semibold">12</p>
        </div>
        <div className="rounded-xl border border-border bg-card p-4">
          <h2 className="text-sm font-medium text-muted-foreground">Check-outs hoje</h2>
          <p className="text-2xl font-semibold">9</p>
        </div>
      </div>
    </section>
  )
}

export default DashboardPage
