package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

var (
	i        int
	pastVals map[int]int
)

func main() {
	f, err := os.Open("changes.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	pastVals = make(map[int]int)

	for {
		readFile(f)
		f.Seek(0, 0)
	}
}

func readFile(f *os.File) {
	s := bufio.NewScanner(f)
	for s.Scan() {
		val, err := strconv.Atoi(s.Text()[1:])
		if err != nil {
			log.Fatal(err)
		}

		switch string(s.Text()[0]) {
		case "+":
			i = i + val
		case "-":
			i = i - val
		default:
			log.Fatal("no matching sign")
		}

		if pastVals[i] == 0 {
			pastVals[i]++
		} else {
			log.Fatalf("Value '%v' repeated.", i)
		}
	}
}
