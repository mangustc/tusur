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
        this.nameOtdela = nameOtdela;
        this.productCode = productCode;
        this.name = name;
        this.country = country;
        this.retailPrice = retailPrice;
        this.namesource = namesource;
    }

    public String toString() {
        String out = "";

        out += this.name + ":\n";
        out += "\tnameOtdela: " + this.nameOtdela + ";\n";
        out += "\tproductCode: " + this.productCode + ";\n";
        out += "\tcountry: " + this.country + ";\n";
        out += "\tretailPrice: " + this.retailPrice + ";\n";
        out += "\tnamesource: " + this.namesource + ";\n";

        return out;
    }
}
