package Lab7;

public class Supermarket {
    String nameOtdela;
    String productCode;
    String name;
    String country;
    double retailPrice;
    String namesource;

    Supermarket(String nameOtdela, String productCode, String name, String country, double retailPrice,
            String namesource) {
        this.name = name;
        this.country = country;
        this.nameOtdela = nameOtdela;
        this.namesource = namesource;
        this.productCode = productCode;
        this.retailPrice = retailPrice;
    }

    public String toString() {
        String out = "";

        out += this.name + ":\n";
        out += "\tcountry: " + this.country + ";\n";
        out += "\tnameOtdela: " + this.nameOtdela + ";\n";
        out += "\tnamesource: " + this.namesource + ";\n";
        out += "\tproductCode: " + this.productCode + ";\n";
        out += "\tretailPrice: " + this.retailPrice + ";\n";

        return out;
    }
}
