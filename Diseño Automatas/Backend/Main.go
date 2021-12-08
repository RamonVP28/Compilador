package main

import (
	"net/http"
	"strings"
	"time"

	"RestApi.com/packages/Connection"
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()

	router.Use(cors.New(cors.Config{
		AllowOrigins:     []string{"http://localhost:3000"},
		AllowMethods:     []string{"GET", "POST"},
		AllowHeaders:     []string{"Content-Type"},
		ExposeHeaders:    []string{"Content-Length"},
		AllowCredentials: true,
		AllowOriginFunc: func(origin string) bool {
			return origin == "http://localhost:5000"
		},
		MaxAge: 12 * time.Hour,
	}))

	router.POST("/Code", sendData)

	router.Run("localhost:8080") // listen and serve on 0.0.0.0:8080

}

type StructCode struct {
	Code string `json:"code"`
}

func sendData(c *gin.Context) {
	var sCode StructCode
	c.BindJSON(&sCode)
	Code := sCode.Code
	StrucCode := Connection.StructCode{Code}
	funcCode := Connection.ExecuteCode(StrucCode)
	if strings.Contains(funcCode, "Error") {
		c.JSON(http.StatusOK, gin.H{
			"Sintactico": funcCode,
			"Lexico":     "",
			"Semantico":  "",
		})
	} else {
		c.JSON(http.StatusOK, gin.H{
			"Sintactico": funcCode[:strings.Index(funcCode, "[")-1],
			"Lexico":     funcCode[strings.Index(funcCode, "[")+1 : strings.Index(funcCode, "]]")+1],
			"Semantico":  funcCode[strings.Index(funcCode, "<inicio>"):strings.Index(funcCode, "<fin>")],
		})
	}
}
