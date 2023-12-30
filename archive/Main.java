import Output.Audio;
import Output.AllFrames;


public class Main {
    public static void main(String[] args) {

        String pythonFile = "main.py";

        try {
            System.out.println("Processing audio and video...");
            Process p = Runtime.getRuntime().exec("python3 " + pythonFile);
            p.waitFor();
            System.out.println("Done processing audio and video");

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        Audio.play();
        AllFrames.draw();

    }
}