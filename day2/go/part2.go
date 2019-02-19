package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

var (
	lines []string
)

func main() {
	f, err := os.Open("../input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	s := bufio.NewScanner(f)

	for s.Scan() {
		curLine := s.Text()

		for _, line := range lines {
			result := compare(curLine, line)
			if len(result) == len(curLine)-1 {
				fmt.Printf("Result is: %v", result)
			}
		}
		lines = append(lines, curLine)
	}
}

func compare(line1, line2 string) (result string) {
	for i := 0; i < len(line1); i++ {
		if line1[i] == line2[i] {
			result += string(line1[i])
		}
	}
	return
}
