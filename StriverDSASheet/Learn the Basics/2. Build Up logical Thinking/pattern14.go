package main

import (
	"fmt"
)


func main(){
	var endCharacter int;
	fmt.Print("Enter the end Character:")

	fmt.Scanf("%c", &endCharacter)

	for  i  := 0; i<= int(endCharacter) - 65; i++ {
		for j := 65; j<=65+i; j++{
			fmt.Printf("%c", j)
		}
		fmt.Println()
	}
	
}