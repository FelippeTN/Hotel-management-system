const BookingsPage = () => {
  return (
    <section className="space-y-4">
      <header className="flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h1 className="text-3xl font-semibold tracking-tight">Reservas</h1>
          <p className="text-muted-foreground text-sm">
            Gerencie reservas ativas e futuras.
          </p>
        </div>
        <button className="rounded-lg bg-primary px-4 py-2 text-sm font-medium text-primary-foreground">
          Nova reserva
        </button>
      </header>
      <div className="rounded-xl border border-border bg-card">
        <div className="grid grid-cols-5 gap-4 border-b border-border px-6 py-3 text-left text-sm font-medium text-muted-foreground">
          <span>Hóspede</span>
          <span>Quarto</span>
          <span>Check-in</span>
          <span>Check-out</span>
          <span>Status</span>
        </div>
        <div className="px-6 py-4 text-sm text-muted-foreground">
          Nenhuma reserva encontrada. Comece adicionando uma nova reserva.
        </div>
      </div>
    </section>
  )
}

export default BookingsPage
