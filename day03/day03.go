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

func Abs(x int) int { // golang doesnt have built-in Abs for int64
    if x < 0 {
        return -x
    }
    return x
}

func Min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

type Key struct {
    X, Y int
}

func main() {
    file, err := os.Open("input.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close() 
    
    reader := bufio.NewReader(file)

    seen := map[Key]int{} // Key to minimum steps it took to get there

    path1, _ := reader.ReadString('\n') 
    path1 = strings.TrimSpace(path1)
    commands := strings.Split(path1, ",")

    r, c, dr, dc, length := 0, 0, 0, 0, 0
    for _, d := range commands {
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
            length += 1

            // if this hasnt been visited
            if _, ok := seen[Key{r,c}]; !ok {
                seen[Key{r,c}] = length
            }
        }
    }

    path2, _ := reader.ReadString('\n') 
    path2 = strings.TrimSpace(path2)
    commands = strings.Split(path2, ",")

    min_distance := math.MaxInt64
    r, c, dr, dc, length = 0, 0, 0, 0, 0
    for _, d := range commands {
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
            length += 1

            if _, ok := seen[Key{r,c}]; ok {
                min_distance = Min(min_distance, length + seen[Key{r,c}])
            }
        }
    }

    fmt.Println(min_distance)
}