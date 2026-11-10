// Minimal Frappe REST client. Requests go to /api/* which Vite proxies
// to the Frappe bench in development (see vite.config.ts).

export class FrappeError extends Error {
  status: number
  constructor(message: string, status: number) {
    super(message)
    this.status = status
  }
}

async function request<T>(path: string, init: RequestInit = {}): Promise<T> {
  const res = await fetch(path, {
    credentials: 'include',
    ...init,
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
      ...(init.headers ?? {}),
    },
  })
  const body = await res.json().catch(() => ({}))
  if (!res.ok) {
    throw new FrappeError(body?.exception ?? body?.message ?? res.statusText, res.status)
  }
  return (body.message ?? body.data ?? body) as T
}

/** Call a whitelisted server method, e.g. `genysis_pos.api.ping`. */
export function call<T = unknown>(method: string, args: Record<string, unknown> = {}) {
  return request<T>(`/api/method/${method}`, { method: 'POST', body: JSON.stringify(args) })
}

/** List documents of a DocType. */
export function getList<T = Record<string, unknown>>(
  doctype: string,
  params: { fields?: string[]; filters?: unknown[]; limit?: number } = {},
) {
  const q = new URLSearchParams()
  if (params.fields) q.set('fields', JSON.stringify(params.fields))
  if (params.filters) q.set('filters', JSON.stringify(params.filters))
  if (params.limit) q.set('limit_page_length', String(params.limit))
  return request<T[]>(`/api/resource/${encodeURIComponent(doctype)}?${q}`)
}

export function login(usr: string, pwd: string) {
  return request('/api/method/login', { method: 'POST', body: JSON.stringify({ usr, pwd }) })
}

export function logout() {
  return request('/api/method/logout', { method: 'POST' })
}
