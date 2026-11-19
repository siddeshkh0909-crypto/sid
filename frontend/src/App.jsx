import { useEffect } from 'react'

function App() {
  useEffect(() => {
    // If running in Vite dev, redirect to the full KIT application
    window.location.replace('/kit.html')
  }, [])

  return (
    <div style={{ width: '100vw', height: '100vh', margin: 0, padding: 0, overflow: 'hidden' }}>
      <iframe
        src="/kit.html"
        title="KIT SMART - Karavali Institution of Technology"
        style={{ width: '100%', height: '100%', border: 'none' }}
      />
    </div>
  )
}

export default App
