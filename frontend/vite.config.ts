import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, '.', '')
  const frappeUrl = env.VITE_FRAPPE_URL || 'http://localhost:8000'

  return {
    plugins: [react()],
    server: {
      port: 5173,
      // Forward API calls to the Frappe bench so cookies/session auth work in dev.
      proxy: {
        '/api': { target: frappeUrl, changeOrigin: true },
        '/assets': { target: frappeUrl, changeOrigin: true },
        '/files': { target: frappeUrl, changeOrigin: true },
      },
    },
  }
})
