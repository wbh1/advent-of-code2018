package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

var (
	twoRepeats    int
	threeRepeats  int
	commonLetters []byte
	lines         []string
)

func main() {
	f, err := os.Open("../input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	s := bufio.NewScanner(f)

	for s.Scan() {
		parseLine(s.Text())
	}
	fmt.Printf("Twos: %d\nThrees: %d\nChecksum: %d\n", twoRepeats, threeRepeats, twoRepeats*threeRepeats)
}

func parseLine(input string) {
	var (
		twoCounts   bool
		threeCounts bool
	)
	// Map of letter to its frequency
	letters := make(map[byte]int)

	for i := 0; i < len(input); i++ {
		letters[input[i]]++
	}
	// Each line can only count once for repeating twos and repeating threes
	// To avoid counting it multiple times, set a boolean of whether or not it should be counted
	for _, v := range letters {
		switch v {
		case 2:
			twoCounts = true
		case 3:
			threeCounts = true
		}
	}

	if twoCounts == true {
		twoRepeats++
	}

	if threeCounts == true {
		threeRepeats++
	}
}
