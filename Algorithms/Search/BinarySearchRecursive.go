package main

import (
	"fmt"
)

func RecursiveBinarySearch(arr []int, start int, end int, target int) int {
	if start > end {
		return -1
	}

	mid := start + (end - start)/2

	if arr[mid] == target {
		return mid
	}
	if arr[mid]>target {
		return RecursiveBinarySearch(arr, start, mid-1, target)
	}
	return RecursiveBinarySearch(arr, mid+1, end, target)
}

func main(){
	var arr = []int{1,2,3,4,5,6,7,8}
	target := 10
	var result = RecursiveBinarySearch(arr, 0, len(arr)-1, target)
	if result > -1{
		fmt.Printf("Target %d found at index %d", target, result);
	} else
	{
		fmt.Printf("Target %d is not found", target)
	}

}