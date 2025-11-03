const GuestsPage = () => {
  return (
    <section className="space-y-4">
      <header className="flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h1 className="text-3xl font-semibold tracking-tight">Hóspedes</h1>
          <p className="text-muted-foreground text-sm">
            Registre novos hóspedes e acompanhe históricos de estadias.
          </p>
        </div>
        <button className="rounded-lg bg-primary px-4 py-2 text-sm font-medium text-primary-foreground">
          Adicionar hóspede
        </button>
      </header>
      <div className="rounded-xl border border-border bg-card">
        <div className="grid grid-cols-[2fr_1fr_1fr] gap-4 border-b border-border px-6 py-3 text-left text-sm font-medium text-muted-foreground">
          <span>Nome</span>
          <span>Telefone</span>
          <span>Última estadia</span>
        </div>
        <div className="px-6 py-4 text-sm text-muted-foreground">
          Nenhum hóspede cadastrado ainda.
        </div>
      </div>
    </section>
  )
}

export default GuestsPage
