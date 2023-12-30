package Output;

import java.io.*;

public class AllFrames {
    public static void draw() {
        try {
            String filePath = "resources/strings/frame_strings.txt";
            double fps = 30;
            String delimiter = "ARBITRARY_DELIMITER";

            // Load frame strings from file
            String[] frameStrings = loadFrameStrings(filePath, delimiter);

            // Display frames
            displayFrames(frameStrings, fps);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static String[] loadFrameStrings(String filePath, String delimiter) throws Exception {
        StringBuilder fileContent = new StringBuilder();
        BufferedReader reader = new BufferedReader(new FileReader(filePath));
        String line;

        while ((line = reader.readLine()) != null) {
            fileContent.append(line).append("\n");
        }
        reader.close();

        return fileContent.toString().split(delimiter);
    }

    private static void displayFrames(String[] frameStrings, double fps) throws IOException {
        long frameTime = (long) (1e9 / fps); // frame time in nanoseconds
        long nextFrameTime = System.nanoTime();

        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        for (String frame : frameStrings) {
            clearConsole();

            bufferedWriter.write(frame.trim()); // Write the trimmed frame
            bufferedWriter.newLine(); // Add a new line
            bufferedWriter.flush(); // Flush the buffer to ensure immediate output

            // Busy-wait loop until the next frame time
            while (System.nanoTime() < nextFrameTime) {}

            nextFrameTime += frameTime; // Set next frame time
        }

        bufferedWriter.close(); // Close the BufferedWriter at the end
    }


    private static void clearConsole() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

}
