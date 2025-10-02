
// The process builder library allows us to run operating system commands in java. It is akin to the "os" module in python 
import java.lang.ProcessBuilder;




// creating a test class
// Note that I will need a separate python script to handle the ML side, such as predictions and so forth 
// Java will handle the back-end side. 


public class newsApp {



	static void train_model(String script) {
		System.out.println("Training the model..."); 
		// The script is called "news_model.py" 
		//
		ProcessBuilder run_script = new ProcessBuilder("python", script).redirectErrorStream(true).start(); 

	}


	public static void main(String[] args) {

		System.out.println("Welcome to my news app");

		/*
		 * This script will run Python scripts for the ML-side
		 * Java will handle all of the backend-side 
		 *
		 *
		 */

		System.out.println("Training the model..."); 
		try {
			train_model("news_model.py");
		        System.out.println("Successfully trained the model"); 	

		} catch (Exception e) {

			System.out.println("There was an error: " + e); 
		} finally {

			System.out.println("Finished!"); 

		}
	       	

	}
	


}
