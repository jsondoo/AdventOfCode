package main

import(
	"fmt"
	"os"
	"log"
	"bufio"
	"strconv"
	// "math"
)

func getFuel(mass int) int {
	var fuel int = mass / 3 - 2
	if fuel < 0 {
		return 0
	}
	return fuel + getFuel(fuel)
}

func main() {
	fmt.Println("hello, 정수")
	file, err := os.Open("day01.txt")
	if err != nil {
		log.Fatal(err)
  	}
  	defer file.Close() 

  	var total int = 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		n, er := strconv.Atoi(scanner.Text())

		if er != nil {
			log.Fatal(er)
		}

		fmt.Println(n)
		total += getFuel(n)
	}

	fmt.Println("Part 2: ", total)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}


}