package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

type pattern struct {
	index    int
	leftEdge int
	topEdge  int
	width    int
	height   int
}

var (
	patterns []pattern
	grid     [1000][1000]int
)

func main() {

	f, err := os.Open("../input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	s := bufio.NewScanner(f)

	for s.Scan() {
		patterns = append(patterns, parseLine(s.Text()))
	}

	for _, p := range patterns {
		for y := p.topEdge; y < (p.topEdge + p.height); y++ {
			for x := p.leftEdge; x < (p.leftEdge + p.width); x++ {
				grid[x][y]++
			}
		}
	}

	// Create channels for goroutines
	nonOverlappingIndex := make(chan int)
	overlaps := make(chan int)

	go func() {
		// Range over the patterns again.
		// This time, if the space being increased is greater than 1,
		// then we know it overlapped before.
		// If it is only 1, then we know that only one claim used that space.
		for _, p := range patterns {
			overlapping := false
			for y := p.topEdge; y < (p.topEdge + p.height); y++ {
				for x := p.leftEdge; x < (p.leftEdge + p.width); x++ {
					if grid[x][y] > 1 {
						overlapping = true
					}
				}
			}
			if overlapping == false {
				nonOverlappingIndex <- p.index
			}
		}
	}()

	go func() {
		var o int
		for _, column := range grid {
			for _, val := range column {
				if val > 1 {
					o++
				}
			}
		}
		overlaps <- o
	}()

	fmt.Println("Non-overlapping index:", <-nonOverlappingIndex)
	fmt.Println("Number of overlaps:", <-overlaps)

}

func parseLine(s string) pattern {
	// #10 @ 936,278: 13x27
	regex, err := regexp.Compile(`#([0-9]*) @ ([0-9]*),([0-9]*): ([0-9]*)x([0-9]*)`)
	if err != nil {
		log.Fatal(err)
	}
	matches := regex.FindStringSubmatch(s)

	intConv := func(s string) int { x, _ := strconv.Atoi(s); return x }

	return pattern{
		index:    intConv(matches[1]),
		leftEdge: intConv(matches[2]),
		topEdge:  intConv(matches[3]),
		width:    intConv(matches[4]),
		height:   intConv(matches[5]),
	}
}
