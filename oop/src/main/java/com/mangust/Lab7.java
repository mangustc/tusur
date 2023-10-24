package com.mangust;

import java.util.List;
import java.util.LinkedList;
import java.util.Iterator;

import java.io.FileWriter;
import java.io.IOException;
// import org.json.simple.JSONArray; 
// import org.json.simple.JSONObject;

// import com.google.gson.Gson;
import com.google.gson.*;

public class Lab7 {
    // Saves to json
    static void saveToFile(String filePath, List<Supermarket> supermarkets) throws IOException {
        // Gson gson = new Gson();
        // String json = gson.toJson(supermarkets);
        // System.out.println(json);
        GsonBuilder builder = new GsonBuilder();
        builder.setPrettyPrinting();

        Gson gson = builder.create();

        FileWriter file = new FileWriter(filePath);
        file.write("Files in Java might be tricky, but it is fun enough!");
        file.close();
    }

    public static void main(String[] args) {
        List<Supermarket> supermarkets = new LinkedList<Supermarket>();
        supermarkets.add(new Supermarket("nameOtdela1", "productCode1", "name1", "country1", 1, "namesource1"));
        supermarkets.add(new Supermarket("nameOtdela2", "productCode2", "name2", "country2", 2, "namesource2"));
        supermarkets.add(new Supermarket("nameOtdela3", "productCode3", "name3", "country3", 3, "namesource3"));
        supermarkets.add(new Supermarket("nameOtdela4", "productCode4", "name4", "country4", 4, "namesource4"));

        Iterator<Supermarket> iterator = supermarkets.iterator();
        while (iterator.hasNext()) {
            Supermarket supermarket = iterator.next();
            if (supermarket.name == "name2")
                iterator.remove();
            System.out.println(supermarket);
        }

        for (int i = 0; i < supermarkets.size(); i++) {
            System.out.println(supermarkets.get(i));
        }

        supermarkets.forEach((supermarket) -> {
            System.out.println(supermarket);
        });

        try {
            saveToFile("./test.txt", supermarkets);
        } catch (IOException error) {
            System.out.println("Failed to write to a file");
            error.printStackTrace();
        }
    }
}
