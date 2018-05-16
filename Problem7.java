import java.util.ArrayList;
import java.util.Scanner;

public class Problem7 {

    private static ArrayList<String> costumers = new ArrayList<>();

    private static void parseCommand(String command){
        String[] cmd = command.split(" "); // split text by space
        if (cmd[0].equals("add")){
            costumers.add(cmd[1]);
        }
        else if (cmd[0].equals("find")) {
            int count = 0;
            for (String costumer: costumers){
                if (costumer.startsWith(cmd[1])){
                    count += 1;
                }
            }
            System.out.println(count);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int loop = sc.nextInt();

        for (int i = 0; i < loop; i++) {
            String command = sc.nextLine();
            parseCommand(command);
        }
    }
}
