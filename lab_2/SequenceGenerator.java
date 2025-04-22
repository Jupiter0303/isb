import java.util.Random;
import java.util.ArrayList;


 class SequenceGenerator {
    public static ArrayList<Boolean> GenerateSequence(int size) {
        Random engine = new Random();
        ArrayList<Boolean> sequence = new ArrayList<Boolean>();
        for (int i = 0; i < size; i++){
                    sequence.add(engine.nextBoolean());
        }

        return sequence;
    }


    public static void main(String[] args) {
        ArrayList<Boolean> binary_sequence = GenerateSequence(128);
        System.out.print("A sequence of random 128 bits: ")
        for (boolean bit : binary_sequence) {
            System.out.print(bit ? '1' : '0');
        }
    }
}