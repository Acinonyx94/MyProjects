// A Higher-or-Lower game played vs the program.

/* TODO: Fix input validations
 * More descriptive comments.
 */
import java.util.*;
import java.util.Scanner;

public class highorlow {
	int highScore = 0; //Sets highscore to 0 upon launch of program.
	Scanner sc = new Scanner(System.in);
	
	public void gameStart() {
		int score = 0;
		boolean gameOver = false;
		int num = (int)(Math.random()*12)+1; //initial pre-loop int set
		do {
			System.out.println(num + ": higher or lower?");
			int temp = num; // Stores previously generated number in a temporary variable
			System.out.println("Guess: higher or lower? (h/l)");// Prompts for guess
			char guess = sc.next().charAt(0);
			num = (int)(Math.random()*12)+1; //Generates comparison variable
			if ((guess == 'h') && (temp <= num)) {
				score++;
			} else if ((guess == 'l') && (temp >= num)) {
				score++;
			} else if ((guess == 'h') && (temp > num)) {
				System.out.println("Incorrect! Game Over!");
				System.out.println("Score: " + score); //Displays score from round
				if (score > highScore) {
					highScore = score; 
					System.out.println("New Highscore: " + highScore); //Sets new highscore
				} else {
					System.out.println("Highscore: " + highScore);
				}
				gameOver = true;
			} else if ((guess == 'l') && (temp < num)) {
				System.out.println("Incorrect! Game Over!");
				System.out.println("Score: " + score); //Displays score from round
				if (score > highScore) {
					highScore = score;
					System.out.println("New Highscore: " + highScore); //Sets new highscore
				} else {
					System.out.println("Highscore: " + highScore);
				}
				gameOver = true;
			} else {
				System.out.println("Input not recognised.");
				System.out.println("Guess: higher or lower? (h/l)");
				guess = sc.next().charAt(0);
			}
		} while (gameOver == false);
		System.out.println("Would you like to play again? y/n"); //Prompt to ask the user if they want to play the game.
		char playAgain = sc.next().charAt(0);
		if (playAgain == 'y') {
			gameStart(); //Restarts the game
		} else if (playAgain == 'n') {
			System.out.println("Goodbye!");
		} else {
			System.out.println("Input not recognised."); // Input validation
		}
	}
	
	
	public static void main (String[] args) {
		highorlow game = new highorlow();
		game.gameStart();
	}
}