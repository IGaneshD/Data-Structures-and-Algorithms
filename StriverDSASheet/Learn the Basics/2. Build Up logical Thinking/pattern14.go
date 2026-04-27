package main

import (
	"fmt"
)


func main(){
	var endCharacter int;
	fmt.Print("Enter the end Character:")

	fmt.Scanf("%c", &endCharacter)

	for  i  := 65; i<= int(endCharacter); i++ {
		for j := 65; j<=i; j++{
			fmt.Printf("%c", j)
		}
		fmt.Println()
	}
	
}