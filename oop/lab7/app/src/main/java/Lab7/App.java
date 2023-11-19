package Lab7;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
// import java.lang.reflect.Type;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

// import com.google.gson.Gson;
// import com.google.gson.GsonBuilder;
// import com.google.gson.reflect.TypeToken;

public class App {
    static void saveToFile(String filePath, List<Supermarket> supermarkets) throws IOException {
        FileWriter file = new FileWriter(filePath);

        String output = "";
        int size = supermarkets.size();
        for (int i = 0; i < size - 1; i++) {
            Supermarket supermarket = supermarkets.get(i);
            output += supermarket.name + "\n" + supermarket.country + "\n" + supermarket.nameOtdela + "\n"
                    + supermarket.namesource + "\n" + supermarket.productCode + "\n" + supermarket.retailPrice + "\n";
        }
        if (size != 0) {
            Supermarket supermarket = supermarkets.get(supermarkets.size() - 1);
            output += supermarket.name + "\n" + supermarket.country + "\n" + supermarket.nameOtdela + "\n"
                    + supermarket.namesource + "\n" + supermarket.productCode + "\n" + supermarket.retailPrice;
        }
        file.write(output);

        file.close();
    }

    static List<Supermarket> readFromFile(String filePath) throws IOException {
        String fileContents = readFile(filePath);
        List<Supermarket> supermarkets = new LinkedList<Supermarket>();

        Scanner scanner = new Scanner(fileContents);

        while (scanner.hasNext()) {
            String name = scanner.nextLine();
            System.out.println(name);
            String country = scanner.nextLine();
            String nameOtdela = scanner.nextLine();
            String namesource = scanner.nextLine();
            String productCode = scanner.nextLine();
            double retailPrice = Double.parseDouble(scanner.nextLine());

            Supermarket supermarket = new Supermarket(nameOtdela, productCode, name, country, retailPrice, namesource);
            supermarkets.add(supermarket);
            System.out.println(supermarket);
        }

        scanner.close();
        return supermarkets;
    }

    static String readFile(String filePath) throws IOException {
        FileReader file = new FileReader(filePath);
        String fileContents = "";
        char ch;
        while ((ch = (char) file.read()) != 65535)
            fileContents += ch;
        file.close();

        return fileContents;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("File path: ");
        String filePath = scanner.nextLine();

        while (true) {
            System.out.println(
                    "1: Read file\n2: Save collection to file and read from file\n3: Read from file to collection\n0: Exit");
            System.out.print("Choose action: ");
            int action = scanner.nextInt();
            switch (action) {
                case 0:
                    break;
                case 1:
                    try {
                        System.out.println("File contents:\n" + readFile(filePath));
                    } catch (IOException error) {
                        System.out.println("Faliure to read file");
                        error.printStackTrace();
                    }
                    continue;
                case 2:
                    try {
                        List<Supermarket> supermarkets = new LinkedList<Supermarket>();
                        // supermarkets.add(
                        //         new Supermarket("nameOtdela1", "productCode1", "name1", "country1", 1, "namesource1"));
                        // supermarkets.add(
                        //         new Supermarket("nameOtdela2", "productCode2", "name2", "country2", 2, "namesource2"));
                        // supermarkets.add(
                        //         new Supermarket("nameOtdela3", "productCode3", "name3", "country3", 3, "namesource3"));
                        // supermarkets.add(
                        //         new Supermarket("nameOtdela4", "productCode4", "name4", "country4", 4, "namesource4"));
                        saveToFile(filePath, supermarkets);
                        System.out.println("File contents:\n" + readFile(filePath));
                    } catch (IOException error) {
                        System.out.println("Faliure writing to file");
                        error.printStackTrace();
                    }
                    continue;
                case 3:
                    try {
                        List<Supermarket> supermarkets = readFromFile(filePath);
                        System.out.println(supermarkets);
                    } catch (IOException error) {
                        System.out.println("Faliure to read file");
                        error.printStackTrace();
                    }
                    continue;
                default:
                    continue;

            }
            break;
        }
        scanner.close();

    }
}
