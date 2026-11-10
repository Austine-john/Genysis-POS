import { useEffect, useState } from 'react'
import { call } from '../api/frappe'

type Ping = { app: string; status: string; etims_enabled: boolean }

export default function PosHome() {
  const [ping, setPing] = useState<Ping | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    call<Ping>('genysis_pos.api.ping')
      .then(setPing)
      .catch((e: Error) => setError(e.message))
  }, [])

  return (
    <main className="pos-home">
      <h1>Genysis POS</h1>
      <p>React frontend for the Frappe / ERPNext backend with KRA e-TIMS integration.</p>
      <section className="status">
        <h2>Backend status</h2>
        {error && <p className="error">Could not reach backend: {error}</p>}
        {!error && !ping && <p>Connecting…</p>}
        {ping && (
          <ul>
            <li>App: {ping.app}</li>
            <li>Status: {ping.status}</li>
            <li>e-TIMS: {ping.etims_enabled ? 'enabled' : 'not configured'}</li>
          </ul>
        )}
      </section>
    </main>
  )
}
