// This function returns true if a string is a palindrome
// s is the original string
// reversedString mutable var stores s reversed using built-in function
// Compares and returns if original string and reverse string are equal

func is_palindrome(s: String) -> (Bool) {
let reversedString = String(s.characters.reverse())
    return(s == reversedString)
}
