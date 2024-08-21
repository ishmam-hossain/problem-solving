func longestConsecutive(nums []int) int {
    if len(nums) == 0 {
        return 0
    }

    set := make(map[int]bool)
    for _, num := range nums {
        set[num] = true
    }


    largest := 0

    for _, num := range nums {
        if !set[num-1] {
            length := 0
            for set[num + length]{
                length ++
            }
            largest = max(largest, length)
        }
    }
    return largest
}
