// This function computes the factorial of a number N

func factorial(N: Int) -> (Int) {
  if N == 1 { // Recursive function stops when N = 1
    return 1
    }
  else {
    return(N * factorial(N - 1)) // Loops recursively until N = 1
  }
}
