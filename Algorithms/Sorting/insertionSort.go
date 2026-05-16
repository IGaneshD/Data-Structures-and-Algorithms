package main

import (
	"fmt"
)

func main(){
	var arr = []int{10, 1, 5, 11, 2, 13}
	fmt.Print("Array Before sorting ", arr)

	var j int

	var temp int

	for i:= 0; i<len(arr); i++{
		temp = arr[i]
		j = i

		for j>0 && temp < arr[j-1]{
			arr[j] = arr[j-1]
			j--
		}

		arr[j] = temp

	}

	fmt.Print("\nArray after Sorting ", arr)
}

