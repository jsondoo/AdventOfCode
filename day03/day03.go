package main

import(
	"fmt"
	"os"
	"log"
	"bufio"
	"strconv"
	"strings"
	"math"
)

func Abs(x int) int { // golang doesnt have built-in ab for int64
	if x < 0 {
		return -x
	}
	return x
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
  	}
  	defer file.Close() 

  	type Key struct {
  		X, Y int
  	}
	// seen := map[Key]bool{} // golang doesnt have a set (???)
	seen := map[Key]int{} // Key to minimum steps it took to get there

  	min_distance := math.MaxInt64
  	first := true

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		if first {
			line := scanner.Text() // path from central thing
			fmt.Println("first lne")
			fmt.Println(line)
			if err != nil {
				log.Fatal(err)
			}

			counter := 0
			r, c, dr, dc := 0, 0, 0, 0
			dir := strings.Split(line, ",")
			for _, d := range dir {
				if d[0] == 'L' {
					dr, dc = 0, -1
				} else if d[0] == 'R' {
					dr, dc = 0, 1
				} else if d[0] == 'U' {
					dr, dc = 1, 0
				} else if d[0] == 'D' {
					dr, dc = -1, 0 
				}

				steps, err := strconv.Atoi(d[1:])
				if err != nil {
					log.Fatal(err)
				}

				for i := 0; i < steps; i++ {
					r += dr
					c += dc
					counter += 1

					// if this hasnt been visited
					if _, ok := seen[Key{r,c}]; !ok {
						seen[Key{r,c}] = counter
					}
					fmt.Println(Key{r,c})
				}

			}
			fmt.Println(seen)
			first = false
		} else {
			// second line 
			line := scanner.Text()
			
			counter := 0
			r, c, dr, dc := 0, 0, 0, 0
			fmt.Println(line)
			dir := strings.Split(line, ",")
			for _, d := range dir {
				if d[0] == 'L' {
					dr, dc = 0, -1
				} else if d[0] == 'R' {
					dr, dc = 0, 1
				} else if d[0] == 'U' {
					dr, dc = 1, 0
				} else if d[0] == 'D' {
					dr, dc = -1, 0 
				}

				steps, err := strconv.Atoi(d[1:])
				if err != nil {
					log.Fatal(err)
				}
				

				for i := 0; i < steps; i++ {
					r += dr
					c += dc
					counter += 1

					// fmt.Println(Key{r,c})
					if val, ok := seen[Key{r,c}]; ok {
						// manhattan_distance := Abs(r) + Abs(c)
						sum_distance := val + counter
						min_distance = min(sum_distance, min_distance)
					}
				}

			}
		}
	}

	fmt.Println(min_distance)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}