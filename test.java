/*vivek anand*/
/* java*/


import java.util.Scanner;

public class RockPaperScissors{
	
	/*program use to paly Rock paper and Scissors */
	
	public static void main(String args[]){
		
		Scanner input = new Scanner(System.in);
		int playerWins=0;
		int compWins =0;
		int gamesPlayed=0;
		
		while(true){
			System.out.println("Its time to play Rock paper scissors ans with (Y/N):" );
			System.out.println("Do you want to play Rock Paper Scissors (yes/no): ");
        String play = input.nextLine();

        // user terminates game and program prints number of wins, losses and percentage of wins.
        if (play.equals("no")) {

            System.out.println("You played a total of " + gamesPlayed + " matches against the computer");
            System.out.println("The computer won " + compWins + " matches");
            System.out.println("You won " + playerWins + " matches");

            // 0% wins when no games are played.
            if (gamesPlayed == 0) { 
                System.out.println("You won 0% of the time!");
                break;

            } else if (gamesPlayed > 0) {
                double totalWins = (int)(playerWins *100) /gamesPlayed;
                System.out.println("You won " + totalWins + "% of the time!");
                break;
            }

        } else if ((!play.equals("no")) && (!play.equals("yes"))) {
            System.out.println("Invalid entry");
        } else {

            System.out.println("Welcome to Rock, Paper and Scissors!");
            System.out.print("Select \"Paper\", \"Rock\" or \"Scissors\": ");
            String decision = input.nextLine();
            System.out.println("Your selection: " + decision);

            // random number generator producing integer values between 1 to 3 for computer's choices.
            // 1 is for Rock, 2 is for Paper and 3 is for Scissors.
            int num = (int)(Math.random() *  (3-0) + 1);

            switch (num) {

                // Computer picks Rock
                case 1:
                    if (decision.equals("Rock")) {
                    System.out.println("Tie, you and the computer selected rock");
                    gamesPlayed++;
                } else if (decision.equals("Paper")) {
                    System.out.println("You win, paper beats rock!");
                    gamesPlayed++;
                    playerWins++;
                } else if (decision.equals("Scissors")) {
                    System.out.println("Computer wins, rock beats scissors!");
                    gamesPlayed++;
                    compWins++;
                } else {
                    System.out.println(decision + " is not a valid input");
                }
                break;
                case 2:
                    // computer picks Paper
                    if (decision.equals("Rock")) {
                    System.out.println("Computer wins, rock beats paper!");
                    gamesPlayed++;
                    compWins++;
                } else if (decision.equals("Paper")) {
                    System.out.println("Tie, you and the computer selected paper");
                    gamesPlayed++;
                } else if (decision.equals("Scissors")) {
                    System.out.println("You win, scissors beats paper");
                    gamesPlayed++;
                    playerWins++;
                } else {
                    System.out.println(decision + " is not a valid input");
                }
                break;
                case 3:
                    // computer picks Scissors
                    if (decision.equals("Rock")) {
                    System.out.println("You win, rock beats scissors");
                    gamesPlayed++;
                    playerWins++;
                } else if (decision.equals("Paper")) {
                    System.out.println("Computer wins, scissors beats paper");
                    gamesPlayed++;
                    compWins++;
                } else if (decision.equals("Scissors")) {
                    System.out.println("Tie, you and the computer selected scissors");
                    gamesPlayed++;
                } else {
                    System.out.println(decision + " is not a valid input");
				 	}
                }
                break;

            } 
        }

    }

}