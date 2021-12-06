import './App.css';
import * as React from 'react';
import { styled } from '@mui/material/styles';


import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';



import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import SettingsOutlinedIcon from '@mui/icons-material/SettingsOutlined';
import IconButton from '@mui/material/IconButton';
import AttachFileIcon from '@mui/icons-material/AttachFile';
import Stack from '@mui/material/Stack';



// Tabla 
const StyledTableCell = styled(TableCell)(({ theme }) => ({
  [`&.${tableCellClasses.head}`]: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
  },
  [`&.${tableCellClasses.body}`]: {
    fontSize: 14,
  },
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
  '&:nth-of-type(odd)': {
    backgroundColor: theme.palette.action.hover,
  },
  // hide last border
  '&:last-child td, &:last-child th': {
    border: 0,
  },
}));

function createData(
  id: number,
  tipo: string,
  nombre: string,
) {
  return { id, tipo, nombre };
}

const rows = [
  createData(159, 'gg', 'gg'),
  createData(159, 'gg', 'gg'),
  createData(159, 'gg', 'gg'),
  createData(159, 'gg', 'gg'),
  createData(159, 'gg', 'gg'),
  createData(159, 'gg', 'gg'),
  createData(159, 'gg', 'gg'),
  createData(159, 'gg', 'gg'),
  createData(159, 'gg', 'gg'),
  createData(159, 'gg', 'gg'),
  createData(159, 'gg', 'gg'),
  createData(159, 'gg', 'gg'),
  createData(159, 'gg', 'gg'),
  createData(159, 'gg', 'gg'),
  createData(159, 'gg', 'gg'),
  createData(159, 'gg', 'gg'),
  createData(159, 'gg', 'gg')
];

// Boton Upload

const Input = styled('input')({
  display: 'none',
});

var file: string;
const getfile = (input: any) => {
  file = input.target.files[0].url;
  console.log(file);
}

function App() {

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

            <div className="table">
              <TableContainer component={Paper}>
                <Table sx={{ minWidth: 700 }} aria-label="customized table">
                  <TableHead>
                    <TableRow>
                      <StyledTableCell align="center">ID</StyledTableCell>
                      <StyledTableCell align="right">Tipo</StyledTableCell>
                      <StyledTableCell align="right">Nombre</StyledTableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {rows.map((row) => (
                      <StyledTableRow key={row.id}>
                        <StyledTableCell component="th" scope="row">
                          {row.id}
                        </StyledTableCell>
                        <StyledTableCell align="right">{row.tipo}</StyledTableCell>
                        <StyledTableCell align="right">{row.nombre}</StyledTableCell>
                      </StyledTableRow>
                    ))}
                  </TableBody>
                </Table>
              </TableContainer>

            </div>

          </div>

          <div className="subcontenido">
            {/*Analizador Sintactico */}

            <h1> Analizador Sintactico</h1>

            <textarea readOnly className="text" />
          </div>


          <div className="subcontenido">
            {/*Analizador Semantico */}

            <h1> Analizador Semantico</h1>

            <textarea readOnly className="text" />
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
            <Button variant="contained" endIcon={<SettingsOutlinedIcon />}>
              Ejecutar
            </Button>
          </Stack>
        </div>




      </div>





    </div>



  );
}

export default App;
