package main

import (
	"crypto/sha256"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

func main() {
	weblocation := os.Args[1]
	resp, err := http.Get(weblocation)
	if err != nil {
		log.Fatalln(err)
	}
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}
	h := sha256.Sum256(body)
	fmt.Printf("%x", h)
}
