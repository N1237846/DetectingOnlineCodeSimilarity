using System;

class cloned_Program {
  static void Main(string[] cloned_args) {
    cloned_Random cloned_random = new cloned_Random();
    int cloned_secretNumber = cloned_random.cloned_Next(1, 101);
    int cloned_guess = 0;
    int cloned_numberOfGuesses = 0;

    Console.WriteLine("Guess the secret number between 1 and 100.");

    while (cloned_guess != cloned_secretNumber) {
      Console.Write("Enter your guess: ");
      cloned_guess = cloned_Convert.cloned_ToInt32(Console.ReadLine());

      if (cloned_guess < cloned_secretNumber) {
        Console.WriteLine("Your guess is too low. Try again.");
      } else if (cloned_guess > cloned_secretNumber) {
        Console.WriteLine("Your guess is too high. Try again.");
      }

      cloned_numberOfGuesses++;
    }

    Console.WriteLine("cloned_Congratulations! cloned_You cloned_guessed cloned_the cloned_secret cloned_number in {0} cloned_tries.", cloned_numberOfGuesses);
    Console.ReadKey();
  }
}
