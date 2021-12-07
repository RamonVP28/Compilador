package Connection

import (
	"fmt"
	"io"
	"log"
	"os/exec"
)

type pipes interface {
	ExecPythonErrPipe() string
	ExecPythonStdinPipe() string
}

type StructCode struct {
	Code string
}

//Revisamos si existe un error en el archivo Query.py
func (this StructCode) ExecPythonErrPipe() string {
	cmd := exec.Command("python", "./main.py", this.Code)

	stderr, err := cmd.StderrPipe()
	if err != nil {
		log.Fatal(err)
	}

	if err := cmd.Start(); err != nil {
		log.Fatal(err)
	}

	slurp, _ := io.ReadAll(stderr)

	if err := cmd.Wait(); err != nil {
		log.Fatal(err)
	}

	return string(slurp)
}

//Enviamos datos al rachivo Query.py y recolectamos la respuesta
func (this StructCode) ExecPythonStdinPipe() string {
	cmd := exec.Command("python", "./main.py", this.Code)

	stdin, err := cmd.StdinPipe()
	if err != nil {
		log.Fatal(err)
	}

	go func() {
		defer stdin.Close()
		io.WriteString(stdin, "values written to stdin are passed to cmd's standard input")
	}()

	out, err := cmd.CombinedOutput()
	if err != nil {
		log.Fatal(err)
	}

	return string(out)
}

func ExecuteCode(execPython pipes) string {
	//Ejecutamos el archivo main.py
	fmt.Printf(execPython.ExecPythonErrPipe())
	result := execPython.ExecPythonStdinPipe()
	return result

	/*//Retornamos la respuesta del archivo Query.py
	if strings.Contains(result, "") {
		return false
	} else {
		return true
	}*/
}
