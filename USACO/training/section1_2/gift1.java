package USACO.training.section1_2;

import java.io.*;
import java.util.*;

class gift1 {
    public static BufferedReader f;
    public static PrintWriter out;
    public static StringTokenizer st;
    
    private static void initializeIO(String filename) throws IOException {
        f = new BufferedReader(new FileReader(filename + ".in"));
        out = new PrintWriter(new BufferedWriter(new FileWriter(filename + ".out")));
    }
    
    private static class exchangeInfo {
        String name;
        int money;
        ArrayList<String> recipients;
        
        exchangeInfo() {
            recipients = new ArrayList<>();
        }
    }
    
    public static void main(String[] args) throws IOException {
        int number_of_recipients;
        int NP;
        ArrayList<String> friends = new ArrayList<>();
        ArrayList<exchangeInfo> gifts = new ArrayList<>();
        
        initializeIO("gift1");
        st = new StringTokenizer(f.readLine());
        NP = Integer.parseInt(st.nextToken());
        for (int i = 0; i < NP; i++) {
            st = new StringTokenizer(f.readLine());
            friends.add(st.nextToken());
        }
        for (int i = 0; i < NP; i++) {
            st = new StringTokenizer(f.readLine());
            exchangeInfo e = new exchangeInfo();
            e.name = st.nextToken();
            st = new StringTokenizer(f.readLine());
            e.money = Integer.parseInt(st.nextToken());
            number_of_recipients = Integer.parseInt(st.nextToken());
            for (int j = 0; j < number_of_recipients; j++) {
                st = new StringTokenizer(f.readLine());
                e.recipients.add(st.nextToken());
            }
            gifts.add(e);
        }
        
        netReceived(NP, friends, gifts);
        out.close();
    }
    
    private static void netReceived(int NP, ArrayList<String> friends,
            ArrayList<exchangeInfo> gifts) {
        Map<String, Integer> bank = new HashMap<>();
        for (int i = 0; i < NP; i++) {
            bank.put(friends.get(i), 0);
        }
        
        for (int i = 0; i < NP; i++) {
            exchangeInfo e = gifts.get(i);
            String giver = e.name;
            int numRecipients = e.recipients.size();
            int distribute = e.money / Math.max(1, numRecipients);
            int giverNet = numRecipients == 0 ? 2 * e.money : e.money - (distribute * numRecipients);
            
            bank.put(giver, bank.get(giver) + giverNet - e.money);
            for (int j = 0; j < numRecipients; j++) {
                bank.put(e.recipients.get(j), bank.get(e.recipients.get(j)) + distribute);
            }
        }
        
        for (int i = 0; i < NP; i++) {
            out.println(friends.get(i) + " " + bank.get(friends.get(i)));
        }
    }
}

/* http://train.usaco.org/usacoprob2?S=gift1&a=pUPQq8h2ZMx
 */
