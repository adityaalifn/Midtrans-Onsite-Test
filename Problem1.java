import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

import static java.lang.Math.sqrt;

public class Problem1 {

    public static Map<Character, Integer> countLetter(String sentence){
        Map<Character, Integer> numChars = new HashMap<>(Math.min(sentence.length(), 26));

        for (int i = 0; i < sentence.length(); ++i) {
            char charAt = sentence.charAt(i);

            if (!numChars.containsKey(charAt)) {
                numChars.put(charAt, 1);
            }
            else {
                numChars.put(charAt, numChars.get(charAt) + 1);
            }
        }

        return numChars;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String address1 = sc.nextLine().toLowerCase();
        String address2 = sc.nextLine().toLowerCase();


        Map<Character, Integer> count1 = countLetter(address1);
        Map<Character, Integer> count2 = countLetter(address2);

        double sumEuclid = 0;

        for (Map.Entry<Character, Integer> entry : count1.entrySet()) {
            Character key = entry.getKey();
            int value1 = entry.getValue();
            int value2 = count2.get(key);
            sumEuclid = sumEuclid + Math.pow(value1 - value2,2);
        }

        double distance = sqrt(sumEuclid);

        System.out.println("Distance: " + distance);
        System.out.println("Similarity: " + (1-distance));
    }
}
