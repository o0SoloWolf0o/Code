package CSS224;


import java.io.IOException;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Random;

public class TSP {

    public static void main(String[] args) throws IOException {
        int[][] distances = {{0, 2, 9, 10}, {1, 0, 6, 8}, {15, 7, 0, 3}, {6, 8, 12, 0}};
        int[] solution = simulatedAnnealing(distances);
        ServerSocket serverSocket = new ServerSocket(8000);
        while (true) {
            Socket socket = serverSocket.accept();
            ObjectOutputStream out = new ObjectOutputStream(socket.getOutputStream());
            out.writeObject(solution);
            out.flush();
            socket.close();
        }
        // try (ServerSocket serverSocket = new ServerSocket(8000)) {
        //     while (true) {
        //         Socket socket = serverSocket.accept();
        //         ObjectOutputStream out = new ObjectOutputStream(socket.getOutputStream());
        //         out.writeObject(solution);
        //         out.flush();
        //         socket.close();
        //     }
        // }
    }

    public static int[] simulatedAnnealing(int[][] distances) {
        int[] currentSolution = new int[distances.length];
        // Initialize the solution randomly
        for (int i = 0; i < currentSolution.length; i++) {
            currentSolution[i] = i;
        }
        shuffleArray(currentSolution);
        int currentCost = calculateCost(currentSolution, distances);
        double temperature = 1000;
        double coolingRate = 0.003;
        while (temperature > 1) {
            int[] newSolution = currentSolution.clone();
            // Randomly select two indices to swap
            int index1 = new Random().nextInt(newSolution.length);
            int index2 = new Random().nextInt(newSolution.length);
            // Swap the values at the selected indices
            int temp = newSolution[index1];
            newSolution[index1] = newSolution[index2];
            newSolution[index2] = temp;
            int newCost = calculateCost(newSolution, distances);
            int delta = newCost - currentCost;
            if (delta < 0) {
                currentSolution = newSolution;
                currentCost = newCost;
            } else {
                double probability = Math.exp(-delta / temperature);
                if (probability > Math.random()) {
                    currentSolution = newSolution;
                    currentCost = newCost;
                }
            }
            temperature *= 1 - coolingRate;
        }
        return currentSolution;
    }

    // Function to calculate the cost of a given solution
    public static int calculateCost(int[] solution, int[][] distances) {
        int cost = 0;
        for (int i = 0; i < solution.length - 1; i++) {
            cost += distances[solution[i]][solution[i + 1]];
        }
        return cost;
    }

    // Function to randomly shuffle the array
    public static void shuffleArray(int[] array) {
        int index, temp;
        Random random = new Random();
        for (int i = array.length - 1; i > 0; i--) {
            index = random.nextInt(i + 1);
            temp = array[index];
            array[index] = array[i];
            array[i] = temp;
        }
    }
}