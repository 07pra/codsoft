import java.util.Scanner;

public class CurrencyConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Currency Conversion Program");
        System.out.println("Available currencies: USD, EUR, GBP, JPY");

        System.out.print("Enter the base currency (e.g., USD): ");
        String baseCurrency = scanner.nextLine().toUpperCase();

        System.out.print("Enter the target currency (e.g., EUR): ");
        String targetCurrency = scanner.nextLine().toUpperCase();

        System.out.print("Enter the amount to convert: ");
        double amountToConvert = scanner.nextDouble();

        // Fetch exchange rates from API (not shown in this example)
        double exchangeRate = getExchangeRate(baseCurrency, targetCurrency);

        if (exchangeRate > 0) {
            double convertedAmount = amountToConvert * exchangeRate;

            System.out.println("Converted amount: " + convertedAmount + " " + targetCurrency);
        } else {
            System.out.println("Error fetching exchange rates. Please try again later.");
        }

        scanner.close();
    }

    private static double getExchangeRate(String baseCurrency, String targetCurrency) {

        if (baseCurrency.equals("USD") && targetCurrency.equals("EUR")) {
            return 0.85; // Simulated exchange rate for USD to EUR
        } else if (baseCurrency.equals("USD") && targetCurrency.equals("GBP")) {
            return 0.73; // Simulated exchange rate for USD to GBP
        } else if (baseCurrency.equals("USD") && targetCurrency.equals("JPY")) {
            return 110.21; // Simulated exchange rate for USD to JPY
        } else {
            return -1; // Indicate an error in fetching exchange rates
        }
    }
}
