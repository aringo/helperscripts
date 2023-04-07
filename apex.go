package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var domains []string

	// read domain names from standard input or a file
	scanner := bufio.NewScanner(os.Stdin)
	if len(os.Args) > 1 {
		file, err := os.Open(os.Args[1])
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error opening file: %v\n", err)
			os.Exit(1)
		}
		defer file.Close()
		scanner = bufio.NewScanner(file)
	}
	for scanner.Scan() {
		domains = append(domains, scanner.Text())
	}

	// extract unique apex domains
	apexDomains := make(map[string]bool)
	for _, domain := range domains {
		parts := strings.Split(domain, ".")
		for i := len(parts) - 2; i >= 0; i-- {
			apexDomain := strings.Join(parts[i:], ".")
			if len(apexDomain) > 0 && apexDomain[0] != '-' {
				apexDomains[apexDomain] = true
				break
			}
		}
	}

	// print the unique apex domains
	for apexDomain := range apexDomains {
		fmt.Println(apexDomain)
	}
}
