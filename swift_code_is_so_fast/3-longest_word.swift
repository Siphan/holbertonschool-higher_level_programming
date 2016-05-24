// Function that returns the longest word in a string

func longest_word(text: String) -> (String) {
    let textArr = text.characters.split{$0 == " "}.map(String.init) // Splits the string (sentence) into array of strings (words)
        var longest:String = "" // Declares our 'max' var which will form the basis for comparison
        for word in textArr { // Loops through array of strings
                let longLen:Int = longest.characters.count // Counts the number of char of our basis (max) for comparison
                let len:Int = word.characters.count // Counts the new word to compare max to
                if len > longLen { // If a word is longer than the previous longest word (max), this word becomes the new max
                        longest = word
                }
        }
        return longest
}
