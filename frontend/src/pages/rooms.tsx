const RoomsPage = () => {
  return (
    <section className="space-y-4">
      <header className="flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h1 className="text-3xl font-semibold tracking-tight">Quartos</h1>
          <p className="text-muted-foreground text-sm">
            Configure tipos de quarto, tarifas e disponibilidade.
          </p>
        </div>
        <button className="rounded-lg bg-primary px-4 py-2 text-sm font-medium text-primary-foreground">
          Novo quarto
        </button>
      </header>
      <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
        <div className="rounded-xl border border-border bg-card p-4">
          <h2 className="text-lg font-semibold">Suíte Master</h2>
          <p className="text-muted-foreground text-sm">
            Capacidade 4 hóspedes · R$ 780/noite
          </p>
        </div>
        <div className="rounded-xl border border-border bg-card p-4">
          <h2 className="text-lg font-semibold">Luxo</h2>
          <p className="text-muted-foreground text-sm">
            Capacidade 3 hóspedes · R$ 520/noite
          </p>
        </div>
        <div className="rounded-xl border border-border bg-card p-4">
          <h2 className="text-lg font-semibold">Standard</h2>
          <p className="text-muted-foreground text-sm">
            Capacidade 2 hóspedes · R$ 340/noite
          </p>
        </div>
      </div>
    </section>
  )
}

export default RoomsPage
