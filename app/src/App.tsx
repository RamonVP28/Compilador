import './App.css';
import { styled } from '@mui/material/styles';

import Button from '@mui/material/Button';
import SettingsOutlinedIcon from '@mui/icons-material/SettingsOutlined';
import IconButton from '@mui/material/IconButton';
import AttachFileIcon from '@mui/icons-material/AttachFile';
import Stack from '@mui/material/Stack';

import { useState } from 'react';

// Boton Upload
const Input = styled('input')({
  display: 'none',
});

var code: string = "";
  // Leemos el archivo
  function readFile(event: any) {
    code = event.target.result;
  }

  // Obtenemos el archivo
  function getfile(file: any) {
    let codes = file.target.files[0];
    const reader = new FileReader();
    reader.readAsText(codes);
    reader.addEventListener('load', readFile);
  }

function App() {
  const [Sintactico, setSintactico] = useState("");
  const [Lexico, setLexico] = useState("");
  const [Semantico, setSemantico] = useState("");

  //Boton ejecutar
  const handleClick = async (e: any) => {
    e.preventDefault();
    let output: any;
    output = await fetch("http://localhost:5000/Code", {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code })
    }).then(res => res.json());
    if (output['Lexico'] !== "" && output['Semantico'] !== "") {
      setLexico(Lexico + output['Lexico']);
      setSemantico(Semantico + output['Semantico']);
    }
    setSintactico(Sintactico + output['Sintactico']);
  }

  //clean textarea 
  const CleanTextArea = (e: any) => {
    e.preventDefault();
    setLexico("");
    setSintactico("");
    setSemantico("");
  }

  return (
    // Tabla de tokens= ID, Tipo, Nombre
    <div id="components">

      <div className="container">

        <div className="h1">
          <h1>
            Compilador
          </h1>
        </div>


        <div className="contenido">
          {/*Analizador Lexicoo */}
          <div className="subcontenido">

            <h1> Analizador Lexico</h1>
            <textarea readOnly className="text" value={Lexico} />

          </div>

          <div className="subcontenido">
            {/*Analizador Sintactico */}

            <h1> Analizador Sintactico</h1>
            <textarea readOnly className="text" value={Sintactico} />
            
          </div>

          <div className="subcontenido">
            {/*Analizador Semantico */}

            <h1> Analizador Semantico</h1>
            <textarea readOnly className="text" value={Semantico} />
          </div>
        </div>

        {/*Boton Upload */}
        <div className="button">

          <Stack direction="row" alignItems="center" spacing={2}>
            <label htmlFor="icon-button-file">
              <Input id="icon-button-file" type="file" onChange={getfile} />
              <IconButton size="large" color="primary" aria-label="upload picture" component="span">
                <AttachFileIcon fontSize="large" />
              </IconButton>
            </label>
          </Stack>

          {/*Boton Ejecutar */}

          <Stack direction="row" spacing={2}>
            <Button variant="contained" endIcon={<SettingsOutlinedIcon />} onClickCapture={CleanTextArea} onClick={handleClick}>
              Ejecutar
            </Button>
          </Stack>
        </div>


      </div>


    </div>
  );
}

export default App;
