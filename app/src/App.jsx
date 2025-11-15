import axios from "axios"
import { useState } from "react"

function App() {
  const [code, setCode] = useState({ text: '' });
  const [output, setOutput] = useState('');
  const [loading, setLoding] = useState(false);

  const handleChange = (e) => {
    setCode({
      ...code,
      [e.target.id]: e.target.value
    });
  };

  const headleSubmit = async () => {
    setLoding(true);
    setOutput(''); // limpiar salida anterior 

    try {
      const req = await axios.post('https://compilador-ide.onrender.com/api/code', code);
      setOutput(req.data.output);
    } catch (error) {
      console.error("error al enviar el codigo:", error);
      setOutput("error al procesar la solicitud:");
    } finally {
      setLoding(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#1e1e1e] text-gray-200 p-6 font-mono">
      <div className="max-w-4xl mx-auto space-y-4">
        <h1 className="text-xl font-semibold text-[#d4d4d4]">MiniLang</h1>

        {/* textarea de entrada */}
        <textarea
          id="text"
          onChange={handleChange}
          className="w-full h-48 bg-[#1e1e1e] text-[#d4d4d4] border border-[#3c3c3c]
          rounded-md p-3 focus:outline-none focus:border-[#007acc]
          placeholder-gray-500 resize-none shadow-inner"
          placeholder="Escribe algo aqui..."
        ></textarea>

        {/* textarea de salida */}
        <textarea
          value={output}
          readOnly
          className="w-full h-48 bg-[#1e1e1e] text-[#9cdcfe] border border-[#3c3c3c]
          rounded-md p-3 focus:outline-none resize-none shadow-inner"
        ></textarea>

        {/* botón */}
        <button
          onClick={headleSubmit}
          disabled={loading}
          className={`px-4 py-2 rounded-md font-semibold transition
          ${
            loading
              ? `bg-[#0e639c] opacity-60 cursor-not-allowed`
              : `bg-[#0e639c] hover:bg-[#1177bb]`
          }`}
        >
          {loading ? 'enviando...' : 'Enviar'}
        </button>
      </div>
    </div>
  );
}

export default App;
