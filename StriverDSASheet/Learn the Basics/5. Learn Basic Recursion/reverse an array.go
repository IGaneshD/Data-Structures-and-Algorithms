package main

import (
	"fmt"
)


func reverseArray(arr []int, i int, j int){
	if (i>=j){
		return 
	}

	var temp int = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

	reverseArray(arr, i+1, j-1)
}


func main(){

	// create an array of type int
	arr := []int{1,2,3,4,4}

	// array before reversing

	reverseArray(arr, 0, len(arr)-1)

	// array after reversing
	fmt.Print(arr)
}