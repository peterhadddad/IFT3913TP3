package tp3;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import static java.lang.Integer.parseInt;

public class ImportationDeDonneCSV {
    public static void main(String[] args) {
        String csvFile = "C:\\Users\\Aymen\\IdeaProjects\\TP3IFT3913\\jfreechart-test-stats.csv";
        String line = "";
        String csvDiviser = ",";

        List<Integer> tlocValeur = new ArrayList<>();
        List<Integer> wmcValeur = new ArrayList<>();
        List<Integer> tassertValeur = new ArrayList<>();
        boolean  skipHeader=true;
        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            while ((line = br.readLine()) != null) {
                if(skipHeader){
                    skipHeader=false;
                    continue;
                }

                String[] data=line.split(csvDiviser);
                if(data.length>=3){
                    try {
                        int tloc = parseInt(data[1].replaceAll("\\(Tloc\\)","").trim());
                        int wmc = parseInt(data[2].replaceAll("\\(wmc\\)","").trim());
                        int tassert = parseInt(data[3].replaceAll("\\(tassert\\)","").trim());

                        tlocValeur.add(tloc);
                        wmcValeur.add(wmc);
                        tassertValeur.add(tassert);
                    }catch (NumberFormatException e) {
                        // Gérer le cas où une conversion en entier échoue
                        System.err.println("Ligne ignorée : " + line);
                    }

                }
            }
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }
}


